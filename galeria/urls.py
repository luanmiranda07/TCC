
from django.urls import path
from galeria.views import index, login


urlpatterns = [
    path('index/', index, name='index'),
    path('', login, name='login'),
]