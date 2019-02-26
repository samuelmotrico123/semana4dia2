from django.contrib import admin
from loja.models import Produto
from loja.models import Pedido

# Register your models here.
admin.site.register(Produto)

admin.site.register(Pedido)