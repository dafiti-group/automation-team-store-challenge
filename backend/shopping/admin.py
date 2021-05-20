from django.contrib import admin

from .models import Cart, Shop


class CartInline(admin.TabularInline):
    model = Cart
    extra = 0


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = [CartInline]
    list_display = ('__str__', 'user', 'purchased')
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    list_filter = ('purchased',)
    date_hierarchy = 'created'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'product', 'quantity', 'price')
    search_fields = ('product__title', 'product__description')
    list_filter = ('product',)
