import pytest

from backend.product.models import Product


@pytest.fixture
def product_data():
    return {
        "id": 1,
        "uuid": "a5d8289a-f6b1-47fc-9c20-270f5ca84fb5",
        "title": "Kichute",
        "description": "Tênis clássico",
        "price": 120.0,
        "image": ""
    }


@pytest.fixture
def product(product_data):
    product = Product.objects.create(**product_data)
    return product
