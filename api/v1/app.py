#!/usr/bin/python3
"""
This module defines a flask app and registers blueprint
It serves at HBNB_API_HOST or 0.0.0.0, port HBNB_API_PORT or 5000
"""
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def purge_session(req):
    """ Closes session """
    storage.close()


if __name__ == "__main__":
    from os import getenv
    host = getenv("HBNB_API_HOST", default="0.0.0.0")
    port = getenv("HBNB_API_PORT", default="5000")
    app.run(host=host, port=port, threaded=True, load_dotenv=True)
