"""
This module defines a flask blueprint route
Route returns json object
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=["GET"])
def status():
    """Return a json object of dummy status code"""
    return jsonify({"status": "OK"})
