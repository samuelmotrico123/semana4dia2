from django.shortcuts import render
from loja.forms import Pedido_Criar
# Create your views here.

def criar_pedido_view(request):
    formulario = Pedido_Criar(request.POST or None)
    if formulario.is_valid():
        formulario.save()
    contexto = {
        'form' : formulario
    }   
    return render(request,'formulario-pedido.html',contexto)
