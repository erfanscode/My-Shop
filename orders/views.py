from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PhoneVerificationForm
from cart.common.KaveSms import *
import random


def verify_phone(request):
    if request.user.is_authenticated:
        return redirect("orders:order-create")
    if request.method == "POST":
        form = PhoneVerificationForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            tokens = {'token': ''.join(random.sample('0123456789', 6))}
            request.session['verification-code'] = tokens['token']
            request.session['phone'] = phone
            send_sms_with_template(phone, tokens, 'verification-code')
            messages.success(request, 'کد تایید با موفقیت ارسال شد')
            return redirect("orders:verify-code")
    else:
        form = PhoneVerificationForm()
    return render(request, 'forms/verify-phone.html', {'form': form})

def verify_code(request):
    pass