from django.conf import settings
from django.core.management.base import BaseCommand

from backend.product.models import Product
from backend.utils.progress_bar import progressbar
from backend.utils.utils import csv_to_list


def get_product(item):
    data = dict(
        title=item['title'],
        description=item['description'],
        price=item['price'],
        image=item['image'],
    )
    return data


def create_products():
    path = settings.BASE_DIR.joinpath('backend/product/fix')
    products = csv_to_list(f'{path}/products.csv')
    aux = []
    for item in progressbar(products, 'Products'):
        data = get_product(item)
        obj = Product(**data)
        aux.append(obj)
    Product.objects.bulk_create(aux)


class Command(BaseCommand):
    help = 'Create data.'

    def handle(self, *args, **options):
        self.stdout.write('Create data.')
        create_products()
