from .models import (Department, Category, Brand, Product, ProductColor, ProductSize, ProductImages)
from django.contrib import admin


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('size', 'stock', 'color', )


@admin.register(ProductImages)
class ProductImages(admin.ModelAdmin):
    list_display = ('image', )
