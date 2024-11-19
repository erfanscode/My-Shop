from dataclasses import fields

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(ShopUser)
class ShopUserAdmin(UserAdmin):
    ordering = ['phone']
    list_display = ['phone', 'first_name', 'last_name', 'is_active', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {'fields': ('address',)}
        ),
    )
