from .models import PromotionalCampaign
from .serializers import PromotionalCampaignSerializer
from .apps import PromotionalCampaignsConfig
import pytest
import pdb
from django.urls import reverse

# Create your tests here.
@pytest.mark.django_db
def test_get_by_id_success():
    promo_camp = PromotionalCampaign.\
                        objects.create(
                            name="preto",
                            percentage_discount=-2)
    assert promo_camp.pk == 1


@pytest.mark.django_db
def test_data_valid():
    data = {"name": "azul", "percentage_discount": 10}
    serializer = PromotionalCampaignSerializer(data=data)
    assert serializer.is_valid()


@pytest.mark.django_db
def test_data_is_not_valid():
    data = {"wrong": "azul", "percentage_discount": -2}
    with pytest.raises(Exception):
        serializer = PromotionalCampaignSerializer(data=data)
        assert serializer.is_valid()


@pytest.mark.django_db
def test_get_all_promotional_campaigns(client):
    url = reverse('promotional_campaign')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_all_promotional_campaigns(client):
    url = reverse('promotional_campaign')
    response = client.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
def test_create_promotional_campaigns_without_body(client):
    url = reverse('promotional_campaign')
    response = client.post(url)
    assert response.status_code == 412


@pytest.mark.django_db
def test_app_name_is_expected():
    assert PromotionalCampaignsConfig.name == "promotional_campaigns"
