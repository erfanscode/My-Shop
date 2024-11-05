from django.db import models
from django_jalali.db import models as jmodels


class Category(models.Model):
    # Category model
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name


class Product(models.Model):
    # Product model
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE, verbose_name='دسته بندی')
    name = models.CharField(max_length=250, verbose_name='نام محصول')
    slug = models.SlugField(max_length=250, verbose_name='اسلاگ')
    description = models.TextField(max_length=1200, verbose_name='توضیحات')
    inventory = models.PositiveIntegerField(default=0, verbose_name='موجودی')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    off = models.PositiveIntegerField(default=0, verbose_name='میزان تخفیف')
    new_price = models.PositiveIntegerField(default=0, verbose_name='قیمت پس از تخفیف')
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name


class Image(models.Model):
    # Product images model
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    file = models.ImageField(upload_to='images/%Y/%m/%d')
    title = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(max_length=250, null=True, blank=True)
    created = jmodels.jDateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, related_name='features', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name='نام ویژگی')
    value = models.CharField(max_length=250, verbose_name='مقدار ویژگی')

    def __str__(self):
        return self.name + ': ' + self.value
