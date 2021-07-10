from services.viacep import ViaCep
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    STATUS = [
        ('registered', 'registrado'),
        ('confirmed', 'confirmado')
    ]

    GENRE = [
        ('M', 'masculino'),
        ('F', 'feminino'),
        ('O', 'outro')
    ]

    status = models.CharField(default='registered', max_length=10, choices=STATUS)
    forget = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(_('e-mail'), unique=True, error_messages={'unique': 'O e-mail informado já está cadastrado'})
    genre = models.CharField(verbose_name='gênero', null=True, blank=True, max_length=1, choices=GENRE)
    datebirth = models.DateField(verbose_name='data de nascimento', null=True, blank=True)
    document = models.CharField(verbose_name='documento', null=True, blank=True, max_length=11, unique=True, error_messages={'unique': 'O CPF informado já está cadastrado'})
    photo = models.ImageField(verbose_name='foto', upload_to='images/user', null=True, blank=True)

    date_joined = None

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def save(self, *args, **kwargs):
        if self.id is not None:
            self.updated_at = timezone.now()

        return super().save(*args, **kwargs)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name='usuário', on_delete=models.CASCADE)
    zipcode = models.CharField(verbose_name='cep', max_length=9)
    street = models.CharField(verbose_name='logradouro', max_length=255, editable=False)
    district = models.CharField(verbose_name='bairro', max_length=255, editable=False)
    city = models.CharField(verbose_name='cidade', max_length=100, editable=False)
    uf = models.CharField(verbose_name='UF', max_length=2, editable=False)
    number = models.IntegerField(verbose_name='número')
    complement = models.CharField(verbose_name='complemento', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Endereço'
        db_table = 'address'

    def save(self, *args, **kwargs):
        if self.id is not None:
            self.updated_at = timezone.now()

        result = ViaCep().consult(self.zipcode)
        if result.erro:
            raise ValueError('CEP invádilo, tente novamente')

        self.zipcode = result.zipcode
        self.street = result.street
        self.district = result.district
        self.city = result.city
        self.uf = result.uf

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.street
