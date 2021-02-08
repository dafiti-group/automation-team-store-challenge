"""
No column names for 10 columns
 A django model generated with django-csvimport csvinspect
    which used OKN messytables to guess data types - may need some manual tweaks!
"""
from django.db import models

class Shoe(models.Model):

    """Model representing the pair of shoes"""

    name = models.CharField(primary_key=True, max_length=150)
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

    class Meta:
            # Ordering by the lastest products posted
        ordering = ['-post_date']
        db_table = 'table_shoes'
        managed = True

    def __str__(self):
        """String for representing the Model object"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this pair of shoes"""
        return reverse('shoes-detail', args=[str(self.id)]), f'{self.id} ({self.shoe.name})'
