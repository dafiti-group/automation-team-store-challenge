from flask import Flask

def create_app():
    """Main Factory"""
    app = Flask(__name__)
    return app