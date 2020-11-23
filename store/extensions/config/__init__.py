def init_app(app):
    app.config["SECRET_KEY"] = "Test"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///store.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    if app.config["DEBUG"] == True:
        app.config["FULL_URL"] = "localhost:5000"