from django import forms


class PhoneVerificationForm(forms.Form):
    phone = forms.CharField(max_length=11, label="شماره موبایل")

    def clean_phone(self):
        # Check phone field is correct
        phone = self.cleaned_data.get('phone')

        if not phone.isdigit():
            raise forms.ValidationError('شماره موبایل فقط باید عدد باشد')
        if not phone.startswith('09'):
            raise forms.ValidationError('شماره موبایل حتما باید با 09 شروع شود')
        if len(phone) != 11:
            raise forms.ValidationError('شماره تلفن باید 11 رقم باشد')

        return phone