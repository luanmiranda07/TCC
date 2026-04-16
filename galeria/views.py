from django.shortcuts import render

from galeria.models import Produto


def login(request):
    return render(request, 'login.html')

def index(request):
    produtos = Produto.objects.all()
    dados = {
        'produtos': produtos
    }
    return render(request, 'index.html', dados)
