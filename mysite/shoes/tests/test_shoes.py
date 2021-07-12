import json
from unittest import TestCase

from django.test import Client
from django.urls import reverse
import pytest

from shoes.models import Shoes

shoes_url = reverse("shoes-list")
pytestmark = pytest.mark.django_db

# ------------- Test Get Shoes ---------------------


def test_zero_shoes_should_return_empty_list(client) -> None:

    response = client.get(shoes_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []

def test_one_shoes_exists_should_succedd(client) -> None:
    test_shoes = Shoes.objects.create(modelo="amazonshoes")
    response = client.get(shoes_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("modelo") == test_shoes.modelo
    assert response_content.get("status") == "Disponivel"
    assert response_content.get("marca") == ""
    assert response_content.get("quantidade") == 10


# ------------- Test Post Shoes ---------------------

def test_create_shoes_without_arguments_should_fail(client) -> None:
    response = client.post(path=shoes_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"modelo": ["This field is required."], "marca":["This field is required."]}

#@pytest.mark.skip
def test_create_existing_shoes_should_fail(client) -> None:
    Shoes.objects.create(modelo="Googleshoes", marca="google")
    response = client.post(path=shoes_url, data={"modelo": "Googleshoes", "marca":"google"})
    assert response.status_code == 400
    assert json.loads(response.content) == {
         "modelo": [
        "shoes with this modelo already exists."
    ]
    }

#@pytest.mark.skip
def test_create_existing_shoes_without_marca_should_fail(client) -> None:
    Shoes.objects.create(modelo="Googleshoes")
    response = client.post(path=shoes_url, data={"modelo": "Googleshoes"})
    assert response.status_code == 400
    assert json.loads(response.content) == {
         "modelo": [
        "shoes with this modelo already exists."
    ],
        "marca": [
            "This field is required."
        ]
    }

#@pytest.mark.skip
def test_create_shoes_with_only_modelo_all_fields_should_be_default(client) -> None:
    response = client.post(path=shoes_url, data={"modelo": "teste shoes", "marca":"shoes"})
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("modelo") == "teste shoes"
    assert response_content.get("status") == "Disponivel"
    assert response_content.get("marca") == "shoes"
    assert response_content.get("quantidade") == 10

def test_create_shoes_with_esgotado_status_should_succeed(client) -> None:

    response = client.post(
        path=shoes_url, data={"modelo": "teste shoes", "status": "Esgotado","marca":"shoes"}
    )
    assert response.status_code == 201

    response_content = json.loads(response.content)
    assert response_content.get("modelo") == "teste shoes"
    assert response_content.get("status") == "Esgotado"
    assert response_content.get("marca") == "shoes"
    assert response_content.get("quantidade") == 10

