import uuid

from django.db import models
from django.utils.text import slugify

from dafiti.core import choices


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    criado_em = models.DateTimeField('criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('última atualização', auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Marca(BaseModel):
    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('slug')

    def __str__(self):
        return f'{self.nome}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Marca, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Produto(BaseModel):
    nome = models.CharField('Nome', max_length=200)
    sku = models.CharField('SKU', max_length=15, blank=True)
    descricao = models.TextField('Descrição', null=True)
    quantidade = models.PositiveIntegerField('Quantidade estoque', default=0)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=10)
    tipo = models.CharField('Tipo', max_length=50, choices=choices.TIPO_PRODUTO, default=choices.TIPO_PRODUTO_NORMAL)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.sku} - {self.nome}'

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
