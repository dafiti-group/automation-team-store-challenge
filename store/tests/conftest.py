import pytest
from store.app import create_app

@pytest.fixture(scope="module")
def app():
    """ Instance of Main App"""
    return create_app()