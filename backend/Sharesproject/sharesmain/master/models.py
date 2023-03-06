from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.response import Response
from datetime import datetime
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

User = get_user_model()
class SharesMaster(models.Model):
    company = models.CharField(max_length=150, unique=True, null=False)
    ticker = models.CharField(max_length=50, unique=True, null=True)
    volume = models.FloatField(null=False, default=0.00, blank=False)
    current_price = models.FloatField(null=False, blank=False)
    last_price = models.FloatField(null=False, blank=False, default=0.00)
    industry = models.CharField(max_length=200, blank=True, null=True)
    change = models.FloatField(blank=True, null=True, default=0.00)
    date_created = models.DateField(default=timezone.now)
    last_updated = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    date_archived = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.company + " " + str(self.current_price)

    def archive_share(self):
        self.is_active = False
        self.is_archived = True
        self.date_archived = datetime.now()

        self.save()

    def activate_share(self):
        self.is_active = True
        self.is_archived = False
        self.date_archived = None

        self.save()

    def update_share(self, current_price):
        new_change = current_price - float(self.current_price)
        self.last_updated = datetime.now()
        self.change = float(new_change)
        self.last_price = self.current_price
        self.save()

        return Response({"msg":"updated"})

    @property
    def share_value(self):
        return self.volume * self.current_price

    @property
    def share_is_active(self):
        return self.is_active

    @property
    def share_is_archived(self):
        return self.is_archived


class UserSharesMaster(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    share = models.ForeignKey(SharesMaster, null=False, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, blank=True)
    remaining_quantity = models.PositiveIntegerField(default=0, null=False)
    purchase_price = models.FloatField(null=False, default=0.00)
    quantity_bought = models.PositiveIntegerField(blank=True, null=True)
    date_bought = models.DateField(blank=True, null=True)
    quantity_sold = models.PositiveIntegerField(blank=True, null=True, default=0)
    selling_price = models.FloatField(blank=True, null=True, default=0.00)
    selling_date = models.DateField(blank=True, null=True)
    total_purchase = models.FloatField(null=True, blank=True, default=0.00)
    total_sale = models.FloatField(null=True,blank=True, default=0.00)
    margin = models.FloatField(null=True, blank=True, default=0.00)

    def __str__(self):
        return self.user.email + " " + self.share.company
    @classmethod
    def find_user(cls):
        user = cls.objects.select_related("user")
        return user
    @classmethod
    def find_share(cls):
        shares = cls.objects.all().select_related("share")
        for share in shares:
            return share

    def sort_transactions(self):
        self.total_purchase = self.purchase_price * float(self.quantity_bought)
        self.remaining_quantity += self.quantity_bought
        self.total_sale = float(self.quantity_sold) * self.selling_price
        self.remaining_quantity = self.quantity_bought - self.quantity_sold
        self.margin = self.total_sale - self.total_purchase
    @property
    def is_profit(self)->bool:
        return self.margin > 0


class UserShareWatchlist(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    share = models.ForeignKey(SharesMaster, null=False, on_delete=models.CASCADE)
    watched_price = models.FloatField(default=0)
    date_added = models.DateField(default=timezone.now)
    is_watched = models.BooleanField(default=True)
    date_removed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.email +" " + self.share.company

    @classmethod
    def find_share(cls):
        share = cls.objects.select_related("share").all()
        return share

    def remove_from_watchlist(self):
        self.date_removed = timezone.now
        self.is_watched = False
        self.save()

    def readd_to_watchlist(self):
        self.date_added = timezone.now
        self.is_watched = True
        self.save()

    @property
    def price_change(self):
        return self.watched_price - self.find_share().share.current_price

    @property
    def is_increased(self):
        return self.find_shares().current_price > self.watched_price

@receiver(pre_save, sender=UserSharesMaster)
def share_start_handler(sender, instance,  *args,**kwargs):
    if instance.id is not None:
        instance.sort_transactions()

@receiver(post_save, sender=UserSharesMaster)
def share_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        if instance.purchase_price == 0 or instance.selling_price == 0:
            shares = UserSharesMaster.objects.select_related("share").get(id=instance.id)
            instance.purchase_price = shares.share.current_price
            instance.selling_price = shares.share.current_price
        instance.save()
        print("done")

@receiver(post_save, sender=UserShareWatchlist)
def watchlist_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        if instance.watched_price == 0:
            share= UserShareWatchlist.objects.select_related("share").get(id=instance.id)
            instance.watched_price = share.share.current_price
            instance.save()

@receiver(pre_save, sender=UserShareWatchlist)
def watchlist_view_handler(sender, instance, *args, **kwargs):
    if instance.id is not None:
        share = UserShareWatchlist.objects.select_related("share").get(id=instance.id)
        instance.watched_price = share.share.current_price