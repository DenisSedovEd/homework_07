from flask import Flask, render_template, request, redirect, url_for, session

from api import users

app = Flask(__name__)

app.register_blueprint(users)

@app.route('/')
def index():
    return render_template('index.html')


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
