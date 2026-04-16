
from django.urls import path
from galeria.views import index, login, excluir_produto, editar_produto


urlpatterns = [
    path('', login, name='login'),
    path('index/excluir/<int:produto_id>/', excluir_produto, name='excluir_produto'),
    path('index/editar/<int:produto_id>/', editar_produto, name='editar_produto'),
    path('index/', index, name='index'),
    
]