#!/usr/bin/python3
"""Start flask web app with dinamic route with html template
"""
from flask import Flask, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        option = "even"
        return render_template("6-number_odd_or_even.html",
                               n=n, option=option)
    else:
        option = "odd"
        return render_template("6-number_odd_or_even.html",
                               n=n, option=option)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
