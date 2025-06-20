from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..app import db
from ..models.appearance import Appearance

bp = Blueprint('appearance', __name__)

@bp.route("/appearances", methods=["POST"])
@jwt_required()
def create_appearance():
    """Create a new Appearance. Requires JWT."""
    data = request.get_json()
    guest_id = data.get("guest_id")
    episode_id = data.get("episode_id")
    rating = data.get("rating")

    if not guest_id or not episode_id or rating is None:
        return jsonify({"error": "Missing required fields"}), 400

    if not Appearance.validate_rating(rating):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    new_appearance = Appearance(guest_id=guest_id, episode_id=episode_id, rating=rating)
    db.session.add(new_appearance)
    db.session.commit()
    return jsonify(new_appearance.to_dict()), 201
