from django.db import models


class WomenShoes(models.Model):
    """
    Armazena as informacoes dos sapatos femininos
    """

    brand = models.CharField(max_length=50)
    categories = models.TextField()
    colors = models.CharField(max_length=50)
    count = models.IntegerField(default=0)
    dateAdded = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateField(auto_now=True)
    dimension = models.CharField(max_length=50,blank=True, null=True)
    manufacturer = models.CharField(max_length=50, blank=True)
    name = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    weight = models.DecimalField(max_digits=9, decimal_places=2)
    