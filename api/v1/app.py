#!/usr/bin/python3
"""
This module defines a flask app and registers blueprint
It serves at HBNB_API_HOST or 0.0.0.0, port HBNB_API_PORT or 5000
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def purge_session(req):
    """Remove/close a session at end of request"""
    storage.close()


if __name__ == "__main__":

    try:
        host = environ['HBNB_API_HOST']
    except KeyError:
        host = '0.0.0.0'

    try:
        port = environ['HBNB_API_PORT']
    except KeyError:
        port = 5000

    app.run(host, int(port), threaded=True)
