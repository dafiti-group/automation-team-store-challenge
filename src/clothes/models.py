from django.db import models
from django.core.validators import MinValueValidator
from src.colors.models import Color
from src.promotional_campaigns.models import PromotionalCampaign

GENRE_ENUM = (
    ("M", "male"),
    ("F", "female"),
    ("U", "unissex")
)

COLLECTION_ENUM = (
    ("AW", "autumn-winter"),
    ("SS", "sprint-summer")
)


RELEASE_ADJUST_PRICE = 30


class Clothes(models.Model):
    """ Responsible by define Clothes table fields """
    name = models.CharField(max_length=100, unique=True)
    base_price = models.DecimalField(null=False, decimal_places=2,
                                     max_digits=10,
                                     validators=[
                                         MinValueValidator(0.1)])
    final_price = models.DecimalField(null=True, decimal_places=2,
                                      max_digits=10,
                                      validators=[
                                          MinValueValidator(0.1)])
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    promotional_campaign = models.ForeignKey(PromotionalCampaign,
                                             on_delete=models.PROTECT,
                                             null=True)
    genre = models.CharField(null=False, max_length=100, choices=GENRE_ENUM)
    collection = models.CharField(null=False, max_length=100,
                                  choices=COLLECTION_ENUM)
    release = models.BooleanField(default=False)

    class Meta:
        db_table = "Clothes"

    def _str_(self):
        """ get _str_ """
        return self.name

    # pylint: disable=arguments-differ
    # pylint: disable=signature-differs
    def save(self, *args, **kwargs):
        discount_promotional = self.promotional_campaign.percentage_discount\
         if self.promotional_campaign else 0
        release_adjust_price = RELEASE_ADJUST_PRICE if self.release else 0
        self.final_price = float(self.base_price) \
            * ((100-discount_promotional)/100
               + float(release_adjust_price)/100)
        super().save(*args, **kwargs)
