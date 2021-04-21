from django.db import models


class WomenShoes(models.Model):
    """
    Armazena as informacoes dos sapatos femininos
    """

    brand = models.CharField(max_length=255)
    categories = models.TextField(max_length=500)
    colors = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    dateAdded = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    dimension = models.CharField(max_length=255,blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True)
    name = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    weight = models.DecimalField(max_digits=9, decimal_places=2)

    def get_shoe(self):
        return self.name + ' is from manufacturer ' + self.manufacturer

    class Meta:
        ordering = ['id']
