from django import forms
from .models import Shoe

class ShoeForm(forms.ModelForm):

    """
    Form created to populate the model Shoe during user's data input
    """

    class Meta:
        model = Shoe
        fields = '__all__'
        labels = {'name': "Nome", 'price': "Preço (R$)", 'size': "Tamanho",
                  'style': "Estilo", 'type': "Tipo", 'color': "Cor",
                  'brand': "Marca", 'post_date': "Data", 'status':"Status", 'image':"Imagem"}
