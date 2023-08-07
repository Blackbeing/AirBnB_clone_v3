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


@app_views.route('/status', strict_slashes=False, methods=['GET'])
def status():
    """Return a json object of dummy status code"""
    # return jsonify({"port": get_proc(5050)})
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stats():
    """ Return the statistics of all class instances """
    statDict = {}
    clsNames = ["amenities", "cities", "places", "reviews", "states", "users"]
    classes = [Amenity, City, Place, Review, State, User]
    for i in range(len(classes)):
        statDict[clsNames[i]] = storage.count(classes[i])
    return jsonify(statDict)
