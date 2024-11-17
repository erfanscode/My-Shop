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

def cart_detail(request):
    # show all user cart products
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart-detail.html', context)

@require_POST
def update_quantity(request):
    # add or decrease a product in cart
    item_id = request.POST.get('item_id')
    action = request.POST.get('action')
    try:
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(request)
        if action == 'add':
            cart.add(product)
        elif action == 'decrease':
            cart.decrease(product)
        context = {
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
            'quantity': cart.cart[item_id]['quantity'],
            'total': cart.cart[item_id]['quantity'] * cart.cart[item_id]['price'],
            'final_price': cart.get_final_price(),
            'success': True,
        }
        return JsonResponse(context)

    except:
        context = {
            'success': False,
            'error': 'درخواست نامعتبر',
        }
        return JsonResponse(context)

@require_POST
def remove_item(request):
    # remove a product complete
    item_id = request.POST.get('item_id')
    try:
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(request)
        cart.remove(product)
        context = {
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
            'final_price': cart.get_final_price(),
            'success': True,
        }
        return JsonResponse(context)

    except:
        context = {
            'success': False,
            'error': 'درخواست نامعتبر',
        }
        return JsonResponse(context)
