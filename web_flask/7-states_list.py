#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a list of all State objects sorted by name (A->Z)"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
