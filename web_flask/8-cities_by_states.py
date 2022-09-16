#!/usr/bin/python3
"""start a flask web application for HBNB project"""
from flask import Flask
from flask import render_template
from models import storage
from models import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def show_cities_by_states():
    """show cities by states on the HTML page"""
    allStates = storage.all(State)
    return render_template("8-cities_by_states.html", allStates=allStates)


@app.teardown_appcontext
def remove_currentsession(exc):
    """remove current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
