from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ShopUser


class ShopUserCreationForm(UserCreationForm):
    # Form for create new user in admin panel
    class Meta(UserCreationForm.Meta):
        model = ShopUser
        fields = ('phone', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'date_joined')


class ShopUserChangeForm(UserChangeForm):
    # Form for edit a user in admin panel
    class Meta(UserChangeForm.Meta):
        model = ShopUser
        fields = ('phone', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')