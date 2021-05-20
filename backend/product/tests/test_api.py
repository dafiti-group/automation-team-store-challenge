import json
from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_list_products_status_code(client):
    url = '/api/v1/product/products'
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_list_products_content(client, product, product_data):
    url = '/api/v1/product/products'
    response = client.get(url)
    result = json.loads(response.content)
    expected = [product_data]
    assert expected == result


@pytest.mark.django_db
def test_get_product_status_code(client, product):
    url = '/api/v1/product/products/1'
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_get_product_content(client, product, product_data):
    url = '/api/v1/product/products/1'
    response = client.get(url)
    result = json.loads(response.content)
    expected = product_data
    assert expected == result
