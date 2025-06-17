from flask import Blueprint

users = Blueprint("user", __name__, url_prefix="/user")


@users.route("/", methods=["GET"])
def get():
    return "Метод get из user.view"


@users.route("/<user_id>", methods=["GET"])
def get_by_id(user_id):
    return f"Метод get_by_id из user.view. Ищем user с {user_id}"


@users.route("/<user_name>/<name>/<email>", methods=["POST"])
def create(user_name, name, email):
    return f"Метод post из user.view. {user_name}, {name}, {email}"
