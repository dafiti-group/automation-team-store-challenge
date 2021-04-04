from django.contrib import admin
from .models import Produto, CompareProduto
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ('descricao','loja')
    list_display = ('descricao', 'preco_original','preco_promocional', 'promocao', 'loja')
    list_filter = ['created']
    list_per_page = 30
    
class CompareProdutoAdmin(admin.ModelAdmin):
    search_fields = ('produto', 'loja')
    list_display = ('produto', 'preco_produto','loja', 'promocao')
    list_filter = ['created']
    list_per_page = 30    

admin.site.register(Produto, ProdutoAdmin)    
admin.site.register(CompareProduto, CompareProdutoAdmin)    
