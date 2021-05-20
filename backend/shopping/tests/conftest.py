import pytest
from django.contrib.auth.models import User

from backend.product.models import Product
from backend.shopping.models import Cart, Shop


@pytest.fixture
def user():
    data = {
        "first_name": "Regis",
        "last_name": "Santos",
        "email": "regis@email.com"
    }
    user = User.objects.create(**data)
    return user


@pytest.fixture
def product():
    data = {
        "uuid": "e946cced-94c6-4e9a-8921-6dafd36a1517",
        "title": "Kichute",
        "description": "Tênis clássico",
        "price": 119.99
    }
    product = Product.objects.create(**data)
    return product


@pytest.fixture
def shop(user):
    data = {
        "uuid": "d3cb71f4-2567-4966-815d-569dbe2101df",
        "user": user
    }
    shop = Shop.objects.create(**data)
    return shop


@pytest.fixture
def cart(shop, product):
    data = {
        "id": 1,
        "uuid": "7c4389d3-4f7a-4700-8a52-ef3b3c6fb03d",
        "shop_id": shop.id,
        "product_id": product.id,
        "quantity": 1,
        "price": product.price
    }
    cart = Cart.objects.create(**data)
    return cart


@pytest.fixture
def cart_data(shop, product):
    return {
        "id": 1,
        "uuid": "7c4389d3-4f7a-4700-8a52-ef3b3c6fb03d",
        "shop": shop.id,
        "product": product.id,
        "quantity": 1,
        "price": str(product.price)
    }
