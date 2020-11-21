from store.extensions.database import db

class Shoes(db.Model):
    __tablename__ = "shoes"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100), unique=True)
    price = db.Column('price', db.Float())
    description = db.Column('description', db.String(200))