from email.policy import default

from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    phone = models.CharField(max_length=11, verbose_name="موبایل")
    address = models.CharField(max_length=250, verbose_name="آدرس")
    postal_code = models.CharField(max_length=10, verbose_name="کد پستی")
    province = models.CharField(max_length=50, verbose_name="استان")
    city = models.CharField(max_length=50, verbose_name="شهر")

    paid = models.BooleanField(default=False, verbose_name="وضعیت پرداخت")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_post_cost(self):
        total_weight = sum(item.get_weight() for item in self.items.all())

        if total_weight == 0:
            return 0
        elif total_weight <= 1000:
            return 20000
        elif 1000 < total_weight <= 10000:
            return 40000
        else:
            return 60000

    def get_final_cost(self):
        return self.get_total_cost() + self.get_post_cost()

    def __str__(self):
        return f'order: {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')

    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    weight = models.PositiveIntegerField(default=0, verbose_name='وزن')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')

    def get_cost(self):
        return self.price * self.quantity

    def get_weight(self):
        return self.weight * self.quantity

    def __str__(self):
        return f'{self.id}'
