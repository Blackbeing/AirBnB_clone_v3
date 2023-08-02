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
import socket


def get_proc(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("0.0.0.0", port))
            name = "socket.getservbyport({})".format(port)
    except socket.timeout:
        name = "No service running on {port}"
    finally:
        return name


@app_views.route("/status", strict_slashes=False, methods=["GET"])
def status():
    """Return a json object of dummy status code"""
    return jsonify({"port": get_proc(5050)})
    # return jsonify({"status": "OK"}), 200


@app_views.route("/stats", strict_slashes=False, methods=["GET"])
def stats():
    """Return stats of each object as a json"""
    classes = {
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User,
    }
    return (
        jsonify({k.lower(): storage.count(v) for k, v in classes.items()}),
        200,
    )
