from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_create_cart(client, user, product):
    url = '/api/v1/shopping/carts'
    cart_data = {
        "product_id": product.id,
        "quantity": 1,
        "user_id": user.id
    }
    response = client.post(url, cart_data, content_type='application/json')
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_list_carts_status_code(client):
    url = '/api/v1/shopping/carts'
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_delete_cart(client, cart):
    url = '/api/v1/shopping/carts/1'
    response = client.delete(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_delete_cart_response(client, cart):
    url = '/api/v1/shopping/carts/1'
    response = client.delete(url)
    assert response.json() == {"success": True}


@pytest.mark.django_db
def test_complete_purchase(client, shop):
    url = '/api/v1/shopping/shops/1/purchase'
    response = client.put(url)
    assert response.json() == {"success": True}


@pytest.mark.django_db
def test_complete_is_purchased(client, shop):
    shop.purchased = True
    shop.save()
    assert shop.purchased == True
