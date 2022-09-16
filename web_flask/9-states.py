#!/usr/bin/python3
"""start a flask web application for HBNB project"""
from flask import Flask
from flask import render_template
from models import storage
from models import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def show_state(id=None):
    """show the states on the HTML page"""
    allStates = storage.all(State)
    if id is None:
        return render_template("9-states.html", allStates=allStates)
    else:
        state_id = 'State.' + id
        return render_template("9-states.html",
                               allStates=allStates, state_id=state_id)


@app.teardown_appcontext
def remove_currentsession(exc):
    """remove current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
