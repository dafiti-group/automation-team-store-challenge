from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class PromotionalCampaign(models.Model):
    """ Responsible by define Color table fields """
    name = models.CharField(max_length=100, unique=True)
    percentage_discount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])

    class Meta:
        """ Define Color table name """
        db_table = "Promotional Campaings"

    def _str_(self):
        """ get _str_"""
        return self.name
