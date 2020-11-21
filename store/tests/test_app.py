def test_app_created(app):
    """Asserts that app name is Store"""
    assert app.name == "store.app"

def test_debug_mode(config):
    """Asserts that app in production is not in Debug Mode"""
    assert config["DEBUG"] is False

def test_request_returns_404(client):
    assert client.get("/").status_code == 404