from django.contrib.auth.base_user import BaseUserManager

from . import models

class UserManager(BaseUserManager):
    def create_user(self, email,date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, date_of_birth,password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, date_of_birth):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.staff = True
        user.admin = True
        user.confirmed = True
        user.save(using=self._db)
        return user