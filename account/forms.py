from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ShopUser


class ShopUserCreationForm(UserCreationForm):
    # Form for create new user in admin panel
    class Meta(UserCreationForm.Meta):
        model = ShopUser
        fields = ('phone', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'date_joined')

    def clean_phone(self):
        # Check phone field is correct
        phone = self.cleaned_data.get('phone')

        if ShopUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError('شماره موبایل از قبل وجود دارد')
        if not phone.isdigit():
            raise forms.ValidationError('شماره موبایل فقط باید عدد باشد')
        if not phone.startswith('09'):
            raise forms.ValidationError('شماره موبایل حتما باید با 09 شروع شود')
        if len(phone) != 11:
            raise forms.ValidationError('شماره تلفن باید 11 رقم باشد')

        return phone


class ShopUserChangeForm(UserChangeForm):
    # Form for edit a user in admin panel
    class Meta(UserChangeForm.Meta):
        model = ShopUser
        fields = ('phone', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')

    def clean_phone(self):
        # Check phone field is correct
        phone = self.cleaned_data.get('phone')

        if ShopUser.objects.exclude(id=self.instance.id).filter(phone=phone).exists():
            raise forms.ValidationError('شماره موبایل از قبل وجود دارد')
        if not phone.isdigit():
            raise forms.ValidationError('شماره موبایل فقط باید عدد باشد')
        if not phone.startswith('09'):
            raise forms.ValidationError('شماره موبایل حتما باید با 09 شروع شود')
        if len(phone) != 11:
            raise forms.ValidationError('شماره تلفن باید 11 رقم باشد')

        return phone