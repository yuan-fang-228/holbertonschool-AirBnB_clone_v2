#!/usr/bin/python3
"""start a flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hnbn():
    """display Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def show_hnbn():
    """display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_ctext(text):
    """display C followed by the value of text"""
    string = text.replace("_", " ")
    return "C {}".format(string)


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def show_pythontext(text):
    """display Python followed by the value of text"""
    string = text.replace("_", " ")
    return "Python {}".format(string)


@app.route("/number/<int:n>", strict_slashes=False)
def show_number(n):
    """display n is a number only if i is an integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
