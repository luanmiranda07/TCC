from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_barras = models.CharField(max_length=50, unique=True)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome