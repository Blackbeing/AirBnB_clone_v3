#!/usr/bin/python3
"""
This module defines a flask blueprint route
Route returns json object
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    """Return a json object of dummy status code"""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def stats():
    statDict = {}
    from models import storage_t, storage
    if storage_t == 'db':
        from models.engine.db_storage import classes
    else:
        from models.engine.file_storage import classes

    for cls in classes.keys():
        statDict[cls] = storage.count(cls)
    return jsonify(statDict)
