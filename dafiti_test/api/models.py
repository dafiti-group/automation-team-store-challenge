from django.db import models

# Create your models here.

class Product(models.Model):
    title   = models.CharField(max_length=100,db_column='product')
    price   = models.DecimalField(max_digits=10,decimal_places=2,db_column='price')
    img_src = models.TextField(max_length=300,db_column='photo_src')
    
    class Meta:
        db_table = 'products'
    