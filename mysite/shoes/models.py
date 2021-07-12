from django.contrib.postgres.fields import IntegerRangeField
from django.db import models

from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator

class Shoes(models.Model):
    class ShoesStatus(models.TextChoices):
        ESGOTADO = "Esgotado"
        DISPONIVEL = "Disponivel"

    modelo = models.CharField(max_length=30, unique=True)
    status = models.CharField(
        choices=ShoesStatus.choices, default=ShoesStatus.DISPONIVEL, max_length=30
    )
    data_de_lancamento = models.DateTimeField(default=now, editable=True)
    marca = models.CharField(max_length=30)
    quantidade = models.IntegerField(default=10)
    preco = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)
    tamanho = models.IntegerField(validators=[MinValueValidator(0),
                                           MaxValueValidator(50)],
                                  default=40)

    def __str__(self) -> str:
        return f"{self.modelo}"

