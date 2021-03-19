from app import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from passlib.hash import pbkdf2_sha256 as sha256
from passlib.hash import sha256_crypt


class ClientModel(db.Model):
    __tablename__ = 'client'

    email = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    @classmethod
    def check_by_email(cls, email):
        return True if cls.query.filter_by(email = email).first() is not None else False
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        def to_json(x):
            return {
                'email': x.email,
                'nome': x.name
            }
        return {'clients': list(map(lambda x: to_json(x), ClientModel.query.all()))}
    
    @classmethod
    def delete_by_email(cls, email):
        cls.query.filter_by(email = email).delete()
        db.session.commit()
    
    @classmethod
    def update_by_email(cls, email, name):
        try:
            query = cls.query.filter_by(email = email).update({ClientModel.name: name})
            db.session.commit()
            return bool(query)
        
        except Exception as error:
            print("Ocorreu um erro na atualizacao de produtos. Motivo: {}".format(error))


class ProductModel(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    review_score = db.Column(db.Numeric)
    price = db.Column(db.Numeric, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def paginate_results(cls, page):
        print("Iniciando paginate")
        posts = ProductModel.query.paginate()
        print(posts.per_page)

    @classmethod
    def check_by_title(cls, title):
        return True if cls.query.filter_by(title = title).first() is not None else False
    
    @classmethod
    def check_by_id(cls, id):
        return True if cls.query.filter_by(id = id).first() is not None else False
    
    @classmethod
    def delete_by_id(cls, id):
        cls.query.filter_by(id = id).delete()
        db.session.commit()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()
        


class ClientProductModel(db.Model):
    __tablename__ = 'client_product'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete='CASCADE'), nullable=False)
    client_id = db.Column(db.String, db.ForeignKey('client.email', ondelete='CASCADE'), nullable=False)

    __table_args__ = (UniqueConstraint('product_id', 'client_id', name='client_product_unique_constraint'),)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def check_product_by_email(cls, product_id, email):
        return True if cls.query.filter_by(product_id = product_id, client_id = email).first() is not None else False

    @classmethod
    def find_by_email(cls, email):
        def to_json(x):
            return {
                'product_name': (ProductModel.find_by_id(x.product_id)).title
            }
        return {'product_list': list(map(lambda x: to_json(x), ClientProductModel.query.filter_by(client_id = email)))}

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
    
    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password
            }
        return {'users': list(map(lambda x: to_json(x), UserModel.query.all()))}
    
    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} linha(s) deletada(s)'.format(num_rows_deleted)}
        except:
            return {'message': 'Erro ao deletar discadores'}

class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String)
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)