#!/usr/bin/python3
"""
This module defines a flask blueprint route
Route returns json object
"""
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


@app_views.route("/status", methods=["GET"])
def status():
    """Return a json object of dummy status code"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"])
def stats():
    classes = {
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User,
    }
    return jsonify({k.lower(): storage.count(v) for k, v in classes.items()})
