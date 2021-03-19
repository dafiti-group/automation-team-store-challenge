from flask import Flask
from flask import render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import datetime

import os
import logging

_basedir = os.path.abspath(os.path.dirname(__file__))

logging.basicConfig(filename='app.log', format='%(asctime)s - %(message)s', level=logging.INFO)


def create_app():
    return Flask(__name__)

app = create_app()
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dafiti:t3st@d4f1t1@postgres-server:5432/dafiti'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 't3st@d4f1t1'
app.config['REDIS_URI'] = 'redis://redis-server:6379/0'
app.config['JWT_SECRET_KEY'] = 't3st@d4f1t1'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = False
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False


cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': app.config['REDIS_URI']})

jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return models.models.RevokedTokenModel.is_jti_blacklisted(jti)


db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

from app.controllers import resources

api.add_resource(resources.Client, '/api/clients', resource_class_kwargs={
    'logging': logging
})

api.add_resource(resources.Product, '/api/products', resource_class_kwargs={
    'logging': logging
})

api.add_resource(resources.ClientProduct, '/api/favorites', resource_class_kwargs={
    'logging': logging
})

api.add_resource(resources.UserRegistration, '/api/users', resource_class_kwargs={
    'logging': logging
})

api.add_resource(resources.UserLogin, '/api/login', resource_class_kwargs={
    'logging': logging
})

api.add_resource(resources.TokenRefresh, '/api/refresh', resource_class_kwargs={
    'logging': logging
})

api.add_resource(resources.SecretResource, '/api/secret', resource_class_kwargs={
    'logging': logging
})