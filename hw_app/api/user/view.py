import subprocess

from flask import Blueprint, render_template, request
from models import db, User

import db_calls

users = Blueprint("user", __name__, url_prefix="/user")


@users.route("/", methods=["GET"])
def get():
    response = db_calls.get_users(db.Session())
    return render_template('user_get.html', response=response)


@users.route("/search-user-by-id", methods=["GET"])
def get_by_id():
    return render_template('user_by_id_form.html')


@users.route("/user-by-id", methods=["POST"])
def get_by_id_handler():
    user_id = request.form['user_id']
    user = db_calls.get_user_by_id(db.Session(), int(user_id))

    return render_template('user.html', user_name=user.username, name=user.name, email=user.email)


@users.route("/add-user", methods=["GET"])
def add_user():
    return render_template('user_create.html')


@users.route("/created", methods=["POST"])
def add_user_handler():
    user_name = request.form['username']
    name = request.form['name']
    email = request.form['email']
    user = User(username=user_name, name=name, email=email)
    db_calls.create_user(db.Session(), user)
    return render_template('user.html', user_name=user_name, name=name, email=email)

@users.route("/run-mok-script", methods=["GET"])
def add_mok_data():
    process = subprocess.run(['python', 'add_mok_data.py'])
    return render_template('index.html')
