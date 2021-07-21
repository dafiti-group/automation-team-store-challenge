from django.contrib import admin

from .models import Shoes


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    pass
