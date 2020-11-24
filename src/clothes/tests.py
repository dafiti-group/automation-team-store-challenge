from .models import Clothes
from .apps import ClothesConfig
import pytest
import pdb
from django.urls import reverse


@pytest.mark.django_db
def test_app_name_is_expected():
    assert ClothesConfig.name == "clothes"
