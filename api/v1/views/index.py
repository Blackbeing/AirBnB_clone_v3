#!/usr/bin/python3
"""
This module defines a flask blueprint route
Route returns json object
"""
from flask import Flask
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
    #return jsonify({"port": get_proc(5050)})
    return jsonify({"status": "OK"})

@app_views.route("/stats", strict_slashes=False)
def stats():
    """ Return the statistics of all class instances """
    statDict = {}
    from models import storage_t, storage
    if storage_t == "db":
        from models.engine.db_storage import classes
    else:
        from models.engine.file_storage import classes

    for cls in classes.keys():
        statDict[cls] = storage.count(cls)
    return jsonify(statDict)
