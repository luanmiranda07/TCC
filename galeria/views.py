from decimal import Decimal, InvalidOperation

from django.contrib.auth.models import User
from django.db.models import Q, Sum
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404, redirect, render

from galeria.models import Produto


def montar_contexto(produtos, busca='', produto_edicao=None):
    todos_produtos = Produto.objects.all()
    return {
        'produtos': produtos,
        'busca': busca,
        'produto_edicao': produto_edicao,
        'total_produtos': todos_produtos.count(),
        'total_estoque': todos_produtos.aggregate(
            total=Coalesce(Sum('quantidade'), 0)
        )['total'],
        'baixo_estoque': todos_produtos.filter(quantidade__gt=0, quantidade__lte=5).count(),
        'total_categorias': todos_produtos.values('categoria').distinct().count(),
    }


def index(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        categoria = request.POST.get('categoria', '').strip()
        quantidade = request.POST.get('quantidade', '').strip()
        preco = request.POST.get('preco', '').strip().replace('R$', '').replace(' ', '').replace(',', '.')
        codigo_barras = request.POST.get('codigo_barras', '').strip()

        if nome and categoria and quantidade and preco and codigo_barras:
            try:
                usuario = User.objects.first()
                if usuario is not None:
                    Produto.objects.create(
                        nome=nome,
                        categoria=categoria,
                        quantidade=int(quantidade),
                        preco=Decimal(preco),
                        codigo_barras=codigo_barras,
                        usuario=usuario,
                    )
                    return redirect('index')
            except (ValueError, InvalidOperation):
                pass

    busca = request.GET.get('busca', '').strip()
    produtos = Produto.objects.all()
    if busca:
        produtos = produtos.filter(
            Q(nome__icontains=busca)
            | Q(categoria__icontains=busca)
            | Q(codigo_barras__icontains=busca)
        )

    dados = montar_contexto(produtos, busca=busca)
    return render(request, 'index.html', dados)


def excluir_produto(request, produto_id):
    if request.method == 'POST':
        produto = get_object_or_404(Produto, id=produto_id)
        produto.delete()
    return redirect('index')


def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        categoria = request.POST.get('categoria', '').strip()
        quantidade = request.POST.get('quantidade', '').strip()
        preco = request.POST.get('preco', '').strip().replace('R$', '').replace(' ', '').replace(',', '.')
        codigo_barras = request.POST.get('codigo_barras', '').strip()

        if nome and categoria and quantidade and preco and codigo_barras:
            try:
                produto.nome = nome
                produto.categoria = categoria
                produto.quantidade = int(quantidade)
                produto.preco = Decimal(preco)
                produto.codigo_barras = codigo_barras
                produto.save()
                return redirect('index')
            except (ValueError, InvalidOperation):
                pass

    produtos = Produto.objects.all()
    dados = montar_contexto(produtos, produto_edicao=produto)
    return render(request, 'index.html', dados)
