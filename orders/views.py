from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Order, OrderItem
from account.models import ShopUser
from .forms import PhoneVerificationForm, OrderCreateForm
from cart.cart import Cart
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
    if request.method == "POST":
        code = request.POST.get('code')
        if code:
            verification_code = request.session['verification-code']
            phone = request.session['phone']
            if code == verification_code:
                characters = "QWERT123456789!@#$"
                user_password = ''.join(random.sample(characters, 8))
                user = ShopUser.objects.create_user(phone=phone)
                user.set_password(user_password)
                user.save()
                send_data = {'token1': phone, 'token2': user_password}
                send_sms_with_template(phone, send_data, 'your-template-name')
                login(request, user)
                del request.session['verification-code']
                del request.session['phone']
                return redirect("orders:order-create")
            else:
                messages.error(request, 'کد وارد شده صحیح نمی باشد')
    return render(request, 'forms/verify-code.html')

@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                    weight=item['weight'],
                )
            cart.clear()
            return redirect("shop:product-list")
    else:
        form = OrderCreateForm()
    return render(request, 'forms/order-create.html', {'form': form, 'cart': cart})
