#!/usr/bin/python3
"""Start flask web app with dinamic number route
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_routes(text):
    return "C %s" % text.replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_routes(text="is cool"):
    return "Python %s" % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "%d is a number" % int(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
