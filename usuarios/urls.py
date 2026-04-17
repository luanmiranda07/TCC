from django.urls import path

from usuarios.views import cadastrar_pessoa, login


urlpatterns = [
    path('', login, name='login'),
    path('cadastrar/', cadastrar_pessoa, name='cadastrar_pessoa'),
]
