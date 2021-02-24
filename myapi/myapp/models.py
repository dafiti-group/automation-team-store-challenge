from django.db import models
from django.urls import reverse


class Shoe(models.Model):

    """Model representing the pair of shoes"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.CharField(max_length=50)
    style = models.CharField(max_length=100)
    type = models.CharField(max_length=15)
    color = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    post_date = models.DateField()

    PURCHASE_STATUS = (
        ('s', 'In Stock'),
        ('n', 'Non Available'),
        ('a', 'Available'),
    )

    status = models.CharField(
        max_length=1,
        choices=PURCHASE_STATUS,
        blank=True,
        default='a',
        help_text='Shoe availability',
    )

    image = models.ImageField(default='src/img/default.png')

    class Meta:
        # Ordering by the lastest products posted
        ordering = ['-post_date']
        db_table = 'table_shoes'
        managed = True

    def __str__(self):
        """String for representing the Model object"""
        return self.name
