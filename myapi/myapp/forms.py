from django import forms
from .models import Shoe

class ShoeForm(forms.ModelForm):

    class Meta:
        model = Shoe
        fields = '__all__'
        labels = {'name': "Nome", 'price': "Preço", 'size': "Tamanho",
                  'style': "Estilo", 'type': "Tipo", 'color': "Cor",
                  'brand': "Marca", 'post_date': "Data", 'status':"Status", 'image':"Imagem"}
