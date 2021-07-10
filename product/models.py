from django.utils import timezone
from django.template.defaultfilters import slugify
from django.db import models


class ProductModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(null=True, blank=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.id is not None:
            self.updated_at = timezone.now()

        return super().save(*args, **kwargs)


class Department(ProductModel):
    name = models.CharField(verbose_name='Nome', max_length=100)
    uri = models.SlugField(max_length=255, editable=False)

    class Meta:
        verbose_name = 'Departamento'

    def save(self, *args, **kwargs):
        self.uri = slugify(self.name)
        return super(Department, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(ProductModel):
    department = models.ForeignKey(Department, verbose_name='departamento', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='nome', max_length=100)
    uri = models.SlugField(max_length=255, editable=False)

    class Meta:
        verbose_name = 'Categoria'

    def save(self, *args, **kwargs):
        self.uri = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Brand(ProductModel):
    name = models.CharField(verbose_name='nome', max_length=100)
    uri = models.SlugField(max_length=255, editable=False)
    image = models.ImageField(verbose_name='imagem', upload_to='images/brand', null=True, blank=True)

    class Meta:
        verbose_name = 'Marca'

    def save(self, *args, **kwargs):
        self.uri = slugify(self.name)
        return super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(ProductModel):
    category = models.ForeignKey(Category, verbose_name='categoria', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name='marca', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='título', max_length=255)
    uri = models.SlugField(max_length=255, editable=False)
    price = models.DecimalField(verbose_name='preço', max_digits=10, decimal_places=2)
    details = models.TextField(verbose_name='detalhes')
    information = models.TextField(verbose_name='informações')

    class Meta:
        verbose_name = 'Produto'

    def save(self, *args, **kwargs):
        self.uri = slugify(self.title)
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductColor(ProductModel):
    product = models.ForeignKey(Product, verbose_name='produto', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='nome', max_length=100)

    class Meta:
        verbose_name = 'Cor do Produto'

    def color_exists(self):
        try:
            find = self.__class__.objects.get(product_id=self.product_id, name__contains=self.name)
        except self.__class__.DoesNotExist:
            return None
        except self.__class__.MultipleObjectsReturned:
            return None
        else:
            return find

    def save(self, *args, **kwargs):
        color_exists = self.color_exists()
        if color_exists is not None:
            raise ValueError('Está cor já foi cadastrada para este produto')

        super(ProductColor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductSize(ProductModel):
    product = models.ForeignKey(Product, verbose_name='produto', on_delete=models.CASCADE)
    color = models.ForeignKey(ProductColor, verbose_name='cor', on_delete=models.CASCADE)
    size = models.CharField(verbose_name='tamanho', max_length=2)
    stock = models.IntegerField(verbose_name='estoque')

    class Meta:
        verbose_name = 'Tamanho do Produto'

    def size_exists(self):
        try:
            find = self.__class__.objects.get(color__product_id=self.color.product_id, color_id=self.color_id, size__contains=self.size)
        except self.__class__.DoesNotExist:
            return None
        except self.__class__.MultipleObjectsReturned:
            return None
        else:
            return find

    def save(self, *args, **kwargs):
        size_exists = self.size_exists()
        if size_exists is not None:
            raise ValueError('Este tamanho já foi cadastrado para este produto com está cor')

        return super(ProductSize, self).save(*args, **kwargs)

    def __str__(self):
        return self.size


class ProductImages(ProductModel):
    product = models.ForeignKey(Product, verbose_name='produto', on_delete=models.CASCADE)
    color = models.ForeignKey(ProductColor, verbose_name='cor', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='imagem', upload_to='images/product')

    class Meta:
        verbose_name = 'Imagens do Produto'

    def __str__(self):
        return self.image
