import time
import uuid
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser)
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .libs import send_email
from .managers import UserManager

CONFIRMATION_TIME = 3600

class CountryModel(models.Model):
    country_name = models.CharField(max_length=10, null=False, blank=False, unique=True)
    country_code = models.CharField(max_length=10, null=False, blank=False, unique=True)

    def __str__(self):
        return self.country_name

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True)
    date_of_birth = models.DateField(default="1990-01-01", null=False)
    admin = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def get_email(self):
        return self.email

    @classmethod
    def find_user_by_email(cls, email):
        return cls.objects.filter(email=email).first()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def most_recent_confirmation(self):
        return ConfirmationModel.objects.select_related('user').order_by('-expire_at').first()

    objects = UserManager()

    def set_confirmed(self):
        self.confirmed = True
        self.save()

class ConfirmationModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4(), unique=True)
    expire_at = models.IntegerField(default=int(time.time() + CONFIRMATION_TIME))
    confirmed = models.BooleanField(default=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.id)
    @classmethod
    def find_by_id(cls, _id):
        return cls.objects.filter(id=_id).first()

    @property
    def expired(self):
        return time.time() > self.expire_at

    def force_to_expire(self):
        if not self.expired:
            self.expire_at = int(time.time())
            self.save()

    def set_confirmed(self):
        user = self.objects.select_related("user").all()
        if self.confirmed:
            user.confirmed = True
            user.save()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        confirm_profile = ConfirmationModel(user=instance)
        confirm_profile.save()

        link = f"http://127.0.0.1:8080/api/confirmation/{instance.most_recent_confirmation}"
        send_email(recipient=instance.email, text=link, subject="Confirmation to the mail")

@receiver(pre_save, sender=ConfirmationModel)
def confirmation_handler(sender, instance, *args, **kwargs):
    if instance.id is not None:
        if instance.confirmed:
            user = ConfirmationModel.objects.select_related("user").get(id=instance.id)
            user.user.set_confirmed()

