from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('verify-phone/', views.verify_phone, name="verify-phone"),
    path('verify-code/', views.verify_code, name="verify-code"),
    path('order-create/', views.order_create, name="order-create"),
]