from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('detail/', views.cart_detail, name='cart-detail'),
    path('update_quantity/', views.update_quantity, name='update-quantity'),
    path('remove_item/', views.remove_item, name='remove-item'),
]