from django.contrib import admin
from .models import *


class ImageInline(admin.TabularInline):
    # Show add image when create a product
    model = Image
    extra = 0


class FeatureInline(admin.TabularInline):
    # Show add product feature when create a product
    model = ProductFeature
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Show category table and add category
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Show product table and add new product
    list_display = ['name', 'inventory', 'new_price', 'created', 'updated']
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ImageInline, FeatureInline]
