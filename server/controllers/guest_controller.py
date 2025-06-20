from flask import Blueprint, jsonify
from ..models.guest import Guest

bp = Blueprint('guest', __name__)

@bp.route("/guests", methods=["GET"])
def get_guests():
    """List all guests."""
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200
