from flask import Flask

from code.api import api


def create_app():
    _app = Flask(__name__)

    _app.register_blueprint(api)

    return _app
