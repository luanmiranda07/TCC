from django.contrib import admin
from .models import Produto, Fornecedor

# Register your models here.

admin.site.register(Fornecedor)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'quantidade', 'preco', 'codigo_barras')
    search_fields = ('nome', 'categoria', 'codigo_barras')
    list_filter = ('categoria',)

admin.site.register(Produto, ProdutoAdmin)    