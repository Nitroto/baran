from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


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

    def ensure_default_system_user(self):
        username = self.get_system_username()
        default_system_user, _ = self.get_or_create(
            username=username,
            defaults={'username': username})
        return default_system_user

    def get_system_username(self):
        return getattr(settings, 'USER_SYSTEM_USERNAME', 'default-system')

    def get_system_user(self):
        return self.get(username=self.get_system_username())

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


class BaranUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=254,
                              verbose_name="Email address")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    objects = BaranUserManager()
