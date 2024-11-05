from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    # Show all products and products by category
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'shop/list.html', context)

def product_detail(request, id, slug):
    # Show detail post using product id and slug
    product = get_object_or_404(Product, id=id, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'shop/detail.html', context)
