#!/usr/bin/python3
"""reviews.py"""

from api.v1.views import app_views
from flask import abort
from flask import jsonify
from flask import make_response
from flask import request
from models import storage
from models.review import Review
from models.user import User
from models.place import Place


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews(place_id):
    """get reviews for a specified place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    reviews = [review.to_dict() for review in place.reviews]
    return make_response(jsonify(reviews), 200)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    """get review information for specified review"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return make_response(jsonify(review.to_dict()), 200)


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """deletes a review based on ites review_id"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def post_review(place_id):
    """create a new review"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if not request.get_json().get("user_id"):
        return make_response(jsonify({'error': 'Missing user_id'}), 400)
    user = storage.get(User, request.get_json().get("user_id"))
    if not user:
        abort(404)
    if not request.get_json().get("text"):
        return make_response(jsonify({'error': 'Missing text'}), 400)
    review = Review(**request.get_json())
    review.place_id = place_id
    review.save()
    return make_response(jsonify(review.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def put_review(review_id):
    """update a review"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'user_id', 'place_id',
                        'created_at', 'updated_at']:
            setattr(review, attr, val)
    review.save()
    return make_response(jsonify(review.to_dict()), 200)
