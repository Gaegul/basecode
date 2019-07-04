from flask import Blueprint

api = Blueprint(__name__, __name__)


@api.route('/')
def hello():
    return "hello"
