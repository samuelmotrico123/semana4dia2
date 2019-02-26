from django import forms
from loja.models import Pedido

class Pedido_Criar(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'nome',
            'email',
            'endereco',
            'complemento',
            'cliente',
            'cartao'
        ]