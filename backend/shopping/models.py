from django.contrib.auth.models import User
from django.db import models

from backend.core.models import TimeStampedModel, UuidModel
from backend.product.models import Product


class Shop(UuidModel, TimeStampedModel):
    user = models.ForeignKey(
        User,
        related_name='users',
        on_delete=models.CASCADE,
    )
    purchased = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'compra'
        verbose_name_plural = 'compras'

    def __str__(self):
        return str(self.uuid)


class Cart(UuidModel):
    shop = models.ForeignKey(
        Shop,
        related_name='shops',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='products',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'carrinho'
        verbose_name_plural = 'carrinhos'

    def __str__(self):
        if self.shop:
            return f'{self.shop.uuid.hex[:5]}-{self.pk}-{self.product}'
        return str(self.uuid)

    def get_subtotal(self):
        return self.price * (self.quantity or 0)
