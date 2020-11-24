from .models import Color
from .serializers import ColorSerializer
from .apps import ColorsConfig
import pytest
import pdb
from django.urls import reverse


@pytest.mark.django_db
def test_get_by_id_success():
    color = Color.objects.create(name="preto", hex_code="#000000")
    assert color.pk == 1


@pytest.mark.django_db
def test_data_valid():
    data = {"name": "azul", "hex_code": "#12355"}
    serializer = ColorSerializer(data=data)
    assert serializer.is_valid()


@pytest.mark.django_db
def test_data_is_not_valid():
    data = {"wrong": "azul", "hex_code": "#12355"}
    with pytest.raises(Exception):
        serializer = ColorSerializer(data=data)
        assert serializer.is_valid()


@pytest.mark.django_db
def test_get_all_colors(client):
    url = reverse('color')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_all_colors(client):
    url = reverse('color')
    response = client.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_create_color_without_body(client):
    url = reverse('color')
    response = client.post(url)
    assert response.status_code == 412


@pytest.mark.django_db
def test_app_name_is_expected():
    assert ColorsConfig.name == "colors"
