from django.db import models

# Used to generate URLs by reversing the URL urlpatterns
from django.urls import reverse

# Required for unique shoes instances
import uuid

class Color(models.Model):

    """Model representing the color of shoes"""
    name = models.CharField(max_length=30, help_text='Enter a color (e.g. blue)')

    def __str__(self):
        """String for representing the Model object"""
        return self.name


class Type(models.Model):

    """Model representing the type of shoes, feminine/masculine"""
    name = models.CharField(max_length=10, help_text='Feminine or masculine shoes')

    def __str__(self):
        """String for representing the Model object"""
        return self.name


class Style(models.Model):

    """Model representing the style of shoes"""
    name = models.CharField(max_length=50, help_text='Enter the style of shoes (e.g. sandals)')

    def __str__(self):
        """String for representing the Model object"""
        return self.name


class Brand(models.Model):

    """Model representing the brand of shoes"""
    name = models.CharField(max_length=100, help_text='Enter the brand of shoes')
    country = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object"""
        return self.name

class Shoe(models.Model):

    """Model representing the pair of shoes (not the product itself)"""
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    size = models.IntegerField()
    color = models.ManyToManyField('Color', help_text='Select a color for these shoes')
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    style = models.ForeignKey('Style', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this pair of shoes"""
        return reverse('shoes-detail', args=[str(self.id)])


class ShoeInstance(models.Model):

    """Model representing a specific pair of shoes"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular pair of shoes')
    shoe = models.ForeignKey('Shoe', on_delete=models.RESTRICT)
    post_date = models.DateField(null=True, blank=True)

    PURCHASE_STATUS = (
        ('a', 'Available'),
        ('s', 'In stock'),
        ('n', 'Not available'),
    )

    status = models.CharField(
        max_length=1,
        choices=PURCHASE_STATUS,
        blank=True,
        default='a',
        help_text="Shoes availability",
    )

    class Meta:
        # Ordering by the lastest products posted
        ordering = ['-post_date']

    def __str__(self):
        """String for representing the Model object"""
        return f'{self.id} ({self.shoe.name})'
