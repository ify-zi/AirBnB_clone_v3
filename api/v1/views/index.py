#!/usr/bin/python3
"""
    index module
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route("/status", methods=['GET'],
                 strict_slashes=False)
def status():
    """send a 200 reponse to cliet with format 'status': 'ok'"""
    return jsonify(status="OK")


@app_views.route('/stats', methods=['GET'],
                 strict_slashes=False)
def stat():
    """returns the number of each objects by type"""
    return jsonify(
        amenities=storage.count('Amenity'),
        cities=storage.count('City'),
        places=storage.count('Place'),
        reviews=storage.count('Review'),
        states=storage.count('State'),
        users=storage.count('User')
    )
