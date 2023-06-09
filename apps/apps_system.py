import os
from flask import Flask
from blueprints import app1, app2
from flask_cors import CORS


# choose apps from blueprints to register
def register_blueprints(app: Flask):
    app.register_blueprint(app1.bp)
    app.register_blueprint(app2.bp)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.config["JSON_AS_ASCII"] = False

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    register_blueprints(app)
    cors = CORS(app)

    return app
