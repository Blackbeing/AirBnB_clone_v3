#!/usr/bin/python3
"""
This module defines a flask blueprint route
Route returns json object
"""
from api.v1.views import app_views
from flask import jsonify


<<<<<<< HEAD
@app_views.route("/status")
=======
@app_views.route("/status", strict_slashes=False, methods=["GET"])
>>>>>>> f37f7b1f2f4d7104d129db1f511a7f1235e85370
def status():
    """Return a json object of dummy status code"""
    return jsonify({"status": "OK"}), 200


<<<<<<< HEAD
@app_views.route("/stats")
def stats():
    statDict = {}
    from models import storage_t, storage
    if storage_t == "db":
        from models.engine.db_storage import classes
    else:
        from models.engine.file_storage import classes

    for cls in classes.keys():
        statDict[cls] = storage.count(cls)
    return jsonify(statDict)
=======
@app_views.route("/stats", strict_slashes=False, methods=["GET"])
def stats():
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
>>>>>>> f37f7b1f2f4d7104d129db1f511a7f1235e85370
