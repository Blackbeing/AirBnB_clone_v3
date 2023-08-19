#!/usr/bin/python3
"""
This module defines the RESTFul API endpoints for State objects

"""
from api.v1.views import app_views
from models.state import State
from models import storage
from flask import jsonify, request


@app_views.route("/states", strict_slashes=False, methods=["GET", "POST"])
def get_states():
    """
    Create state, Get all states
    Return json of new object if created or list of json objects if get
        """

    if request.method == "GET":
        states = storage.all(State)
        return jsonify([state.to_dict() for _id, state in states.items()])

    elif request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"error": "Not a JSON"}), 400
        if not data.get("name", None):
            return jsonify({"error": "Missing name"}), 400

        new_state = State(**data)
        new_state.save()
        return jsonify(new_state.to_dict()), 201


@app_views.route(
    "/states/<state_id>",
    strict_slashes=False,
    methods=["GET", "DELETE", "PUT"],
)
def get_state(state_id):
    """Get/Delete/Update a state object"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"})

    if request.method == "GET":
        return jsonify(state.to_dict())

    elif request.method == "DELETE":
        storage.delete(state)
        storage.save()
        return jsonify({}), 200

    elif request.method == "PUT":
        data = request.get_json()
        if not data:
            return jsonify({"error": "Not a JSON"}), 400
        for k, v in data.items():
            if hasattr(state, k) and k not in [
                "id",
                "created_at",
                "updated_at",
            ]:
                setattr(state, k, v)
        state.save()
        return jsonify(state.to_dict()), 200
