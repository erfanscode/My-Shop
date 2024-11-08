from .cart import Cart


def cart(request):
    # context processor for show cart items count
    return {'cart': Cart(request)}