from django.urls import path
from . import models, views

app_name = 'shop'

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<slug:category_slug>', views.product_list, name='product-list-by-category'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product-detail'),
]