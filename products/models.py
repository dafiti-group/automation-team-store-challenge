from django.db import models
from django.db.models.base import Model
from django.utils.translation import get_language_from_path
#Constantes
from assets.constants import CAMISA, CAMISETA, POLO, CALCA, BERMUDA, CASACO, \
    MASC, FEM, \
    TAM_PP, TAM_P, TAM_M, TAM_G, TAM_GG


class Brand(models.Model):
    name = models.CharField("Nome", max_length=255)
    logo = models.URLField("Logotipo", default="https://lh3.googleusercontent.com/proxy/tmW80bYKouP4BO3pUPYoCIVcW0rjJopBnkgPk_Vfi9SH6FVdQjqfOeG0TPOzXWuqlKUij9ICnlWiwSKOnpMIoTklBw")

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField("Nome", max_length=36)
    description = models.CharField("Descrição", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    TYPES = [
        (CAMISA, "Camisa"),
        (CAMISETA, "Camiseta"),
        (POLO, "Polo"),
        (CALCA, "Calça"),
        (BERMUDA, "Bermuda"),
        (CASACO, "Casaco"),
    ]

    GENDERS = [
        (MASC, "Masculino"),
        (FEM, "Feminino")
    ]

    SIZES = [
        (TAM_PP, "PP"),
        (TAM_P, "P"),
        (TAM_M, "M"),
        (TAM_G, "G"),
        (TAM_GG, "GG")
    ]

    name = models.CharField("Nome", max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    product_type = models.SmallIntegerField("Tipo", choices=TYPES)
    gender = models.SmallIntegerField("Gênero", choices=GENDERS)
    size = models.SmallIntegerField("Tamanho", choices=SIZES)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    color = models.CharField("Cor", max_length=50)
    price = models.DecimalField("Preço", max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name