#!/usr/bin/python3
"""start a flask web application for HBNB project"""
from flask import Flask
from flask import render_template
from models import storage
from models import State, Amenity


app = Flask(__name__)


@app.route("/hbnb_filters/", strict_slashes=False)
def show_states_cities():
    """show states and cities to html page"""
    allStates = storage.all(State)
    allAmenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           allStates=allStates,
                           allAmenities=allAmenities)


@app.teardown_appcontext
def remove_currentsession(exc):
    """remove current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
