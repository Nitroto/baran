from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class BaranUserManager(BaseUserManager):
    def create_user(self, username, password=None, is_active=False, **kwargs):
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(username=username, is_active=is_active)
        if not password:
            password = None
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


class BaranUser(AbstractUser):
    objects = BaranUserManager()
