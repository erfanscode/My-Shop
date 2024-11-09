from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from django.http import JsonResponse


@require_POST
def add_to_cart(request, product_id):
    # view for add product to cart
    try:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product)
        context = {
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
        }
        return JsonResponse(context)
    except:
        return JsonResponse({'error': 'درخواست نامعتبر'})
