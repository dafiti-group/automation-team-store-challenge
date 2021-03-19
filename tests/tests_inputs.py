import unittest
import json
from app import app, db, cache
import time


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        db.create_all()
    
    def test_create_user(self):
        payload = {"username":"victor", "password": "1234"}
        response = self.app.post('/api/users', data=json.dumps(payload), content_type='application/json')
        json_return = json.loads(response.data)

        assert response.status_code == 201
    
    def test_login(self):
        payload = {"username":"victor", "password": "1234"}
        response = self.app.post('/api/login', data=json.dumps(payload), content_type='application/json')
        json_return = json.loads(response.data)

        headers = {
            'Authorization': 'Bearer ' + str(json_return['access_token']),
            'Content-Type': 'application/json'
        }

        assert response.status_code == 200

        return headers, response.status_code

    def test_product_insert(self):
        headers, status_code = self.test_login()
        payload = {
            "title": "Produto XYZ",
            "brand": "In Brasil",
            "price": 348.90,
            "image": "https://a-static.mlcdn.com.br/618x463/panela-de-pressao-eletrica-4-litros-in-brasil/zdok/576083400/34c93193fdbfc261a54211f30d4f52e8.jpg",
            "reviewScore": 4.1
        }
        response = self.app.post('/api/products', data=json.dumps(payload), headers=headers, content_type='application/json')

        assert status_code == 200
        assert response.status_code == 201

    def test_product_insert_invalid(self):
        headers, status_code = self.test_login()
        payload = {
            "title": "Produto XYZ",
            "brand": "In Brasil",
            "price": "348.90",
            "image": "https://a-static.mlcdn.com.br/618x463/panela-de-pressao-eletrica-4-litros-in-brasil/zdok/576083400/34c93193fdbfc261a54211f30d4f52e8.jpg",
            "reviewScore": 4.1
        }
        response = self.app.post('/api/products', data=json.dumps(payload), headers=headers, content_type='application/json')

        assert status_code == 200
        assert response.status_code == 400

    def test_insert_favorite(self):
        headers, status_code = self.test_login()
        
        response = self.app.get('/api/products', headers=headers, content_type='application/json')
        json_return = json.loads(response.data)

        assert response.status_code == 200
        assert 'products' in json_return
        assert 'title' in json_return['products'][0]

        product = json_return['products'][0]['id']

        response = self.app.get('/api/clients', headers=headers, content_type='application/json')
        json_return = json.loads(response.data)

        assert response.status_code == 200
        assert 'clients' in json_return
        assert 'nome' in json_return['clients'][0]

        email = json_return['client'][0]['email']

        payload = {
            "product_id": product,
            "email": email 
        }

        response = self.app.get('/api/favorites', data=json.dumps(payload), headers=headers, content_type='application/json')

        assert response.status_code == 201