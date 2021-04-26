from django.contrib import admin

from dafiti.core.models import Produto, Marca


class ProdutoModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sku')
    list_filter = ('ativo', 'tipo')
    search_fields = ('nome', 'sku')
    save_on_top = True


class MarcaModelAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('ativo',)
    search_fields = ('nome',)
    save_on_top = True


admin.site.register(Produto, ProdutoModelAdmin)
admin.site.register(Marca, MarcaModelAdmin)
