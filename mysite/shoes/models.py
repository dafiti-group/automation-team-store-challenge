from django.db import models

from django.db import models
from django.utils.timezone import now


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

    def __str__(self) -> str:
        return f"{self.modelo}"

