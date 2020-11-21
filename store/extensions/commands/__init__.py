from store.extensions.database import db
from store.extensions.database import models

def init_app(app):
    @app.cli.command()
    def create_database():
        """Initialization from database"""
        db.create_all()