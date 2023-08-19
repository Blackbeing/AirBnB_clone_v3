#!/usr/bin/python3
"""
This module defines a flask app and registers blueprint
It serves at HBNB_API_HOST or 0.0.0.0, port HBNB_API_PORT or 5000
"""
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import environ


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def purge_session(req):
    """Remove/close a session at end of request"""
    storage.close()


@app.errorhandler(404)
def notfound(err):
    """handler for 404 errors
        returns a JSON-formatted 404 status code response """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":

    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, debug=True, threaded=True)
