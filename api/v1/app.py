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
<<<<<<< HEAD
    """ Closes session """
=======
    """Remove a session"""
>>>>>>> f37f7b1f2f4d7104d129db1f511a7f1235e85370
    storage.close()


if __name__ == "__main__":
    from os import getenv
<<<<<<< HEAD
    app.run(host = getenv("HBNB_API_HOST", default="0.0.0.0") , port = getenv("HBNB_API_PORT", default="5000"), threaded=True)
=======

    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)
>>>>>>> f37f7b1f2f4d7104d129db1f511a7f1235e85370
