from flask import Flask

from store.extensions import config
from store.extensions import commands
from store.extensions import database
from store.extensions import serealizer

from store.blueprints import api

def create_app():
    """Main Factory"""
    app = Flask(__name__)
    config.init_app(app)
    database.init_app(app)
    serealizer.init_app(app)
    commands.init_app(app)

    api.init_app(app)
    return app