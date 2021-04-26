from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from dafiti.core.models import Marca


class TestApi(TestCase):
    def test_marca(self):
        """
        Ensure we can create a new marca object.
        """
        token = Token.objects.get(user__username='admin')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        data = {'nome': 'marca teste'}
        response = self.client.post('/api/v1/marcas/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Marca.objects.count(), 1)
