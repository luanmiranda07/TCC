from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        senha = request.POST.get('senha', '')

        usuario = authenticate(request, username=email, password=senha)
        if usuario is not None:
            auth_login(request, usuario)
            return redirect('index')

        return render(request, 'login.html', {'error': 'Email ou senha inválidos'})

    return render(request, 'login.html')


def cadastrar_pessoa(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip()
        senha = request.POST.get('senha', '')

        if nome and email and senha and not User.objects.filter(username=email).exists():
            User.objects.create_user(
                username=email,
                email=email,
                password=senha,
                first_name=nome,
            )
            return redirect('login')

    return render(request, 'cadastrar.html')
