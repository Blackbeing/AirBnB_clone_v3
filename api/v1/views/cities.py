#!/usr/bin/python3
"""
This module defines the RESTFul API endpoints for city objects
>>> curl -X GET http://0.0.0.0:5000/states/a8a3-475e-bf74-ab0a066ca2af/cities
"""
from api.v1.views import app_views
from models.city import City
from models.state import State
from models import storage
from flask import jsonify, request


@app_views.route(
    "/states/<state_id>/cities", strict_slashes=False, methods=["GET"]
)
def get_cities(state_id: int):
    """
    Retrive all cities belonging to a state
    Raises 404 error if state_id does not exist
    """
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"})
    all_cities = state.cities
    return jsonify([city.to_dict() for city in all_cities])


@app_views.route("/cities/<city_id>", strict_slashes=False, methods=["GET"])
def get_city(city_id):
    """
    Retrive city object by id
    Returns city json object
    """
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({"error": "Not found"})
    return jsonify(city.to_dict())


@app_views.route("/cities/<city_id>", strict_slashes=False, methods=["DELETE"])
def delete_city(city_id):
    """
    Delete city by id
    Returns empty dictionary
    """
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({"error": "Not found"})
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route(
    "/states/<state_id>/cities", strict_slashes=False, methods=["POST"]
)
def create_city(state_id):
    """
    Create a city in a state with id as state_id
    Return json of new object
    """
    if state_id is None:
        return jsonify({"error": "Not found"})
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if not data.get("name", None):
        return jsonify({"error": "Missing name"}), 400

    new_city = City(state_id=state_id, **data)
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route("/cities/<city_id>", strict_slashes=False, methods=["PUT"])
def update_city(city_id):
    """
    Update city with id city_id
    Return json of updated city object
    """
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({"error": "Not found"})
    data = request.get_json()

    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    for k, v in data.items():
        if hasattr(city, k) and k not in [
            "id",
            "state_id",
            "created_at",
            "updated_at",
        ]:
            setattr(city, k, v)
    city.save()
    return jsonify(city.to_dict()), 200
