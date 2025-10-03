
from presentation.app_flask.extended_flask import Blueprint, request


blueprint = Blueprint("home", __name__, url_prefix="/home")

@blueprint.route("/hello-world", methods=["GET"])
def hello_world():
    """ ToDo: DocString """
    return {"message": "Hello World, from extended Flask!"}