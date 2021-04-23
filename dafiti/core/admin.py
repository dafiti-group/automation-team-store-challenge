from django.contrib import admin

from dafiti.core.models import Produto


class ProdutoModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sku')
    list_filter = ('ativo', 'tipo')
    search_fields = ('nome', 'sku')
    save_on_top = True


admin.site.register(Produto, ProdutoModelAdmin)
