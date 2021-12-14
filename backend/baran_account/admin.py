from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BaranUser


class BaranUserAdmin(UserAdmin):
    search_fields = ('pk', 'username', 'first_name', 'last_name', 'email')


admin.site.register(BaranUser, BaranUserAdmin)
