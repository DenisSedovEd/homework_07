from flask import Flask, render_template, request, redirect, url_for, session

from api import users

app = Flask(__name__)

app.register_blueprint(users)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
