#!/usr/bin/python3
"""start a flask web application for HBNB project"""
from flask import Flask
from flask import render_template
from models import storage
from models import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def show_state():
    """show all the states on the HTML page"""
    allStates = storage.all(State)
    return render_template("7-states_list.html", allStates=allStates)


@app.teardown_appcontext
def remove_currentsession(exc):
    """remove current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
