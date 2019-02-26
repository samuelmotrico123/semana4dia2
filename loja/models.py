from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=120)
    preco = models.DecimalField(decimal_places=2, max_digits=1000, default=0)
    descricao = models.TextField(blank=True,null=True)
    cor = models.CharField(max_length=10)
    data_de_fabricacao = models.DateField(auto_now=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    CLIENTE_NOVO = 'CN'
    CLIENTE_RECORRENTE = 'CR'
    CLIENTE_ESTADO = [
        (CLIENTE_NOVO , 'Cliente Novo'),
       ( CLIENTE_RECORRENTE , 'Cliente Recorrente')
    ]

    nome = models.CharField(max_length=120)
    email = models.EmailField()
    endereco = models.CharField(max_length=240)
    complemento = models.CharField(blank=True,null=True,max_length=240)
    cartao = models.IntegerField()
    cliente = models.CharField(max_length=2, choices=CLIENTE_ESTADO, default=CLIENTE_NOVO)
