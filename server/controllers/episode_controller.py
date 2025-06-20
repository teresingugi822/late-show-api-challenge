from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..app import db
from ..models.episode import Episode

bp = Blueprint('episode', __name__)

@bp.route("/episodes", methods=["GET"])
def get_episodes():
    """List all episodes."""
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200

@bp.route("/episodes/<int:id>", methods=["GET"])
def get_episode_by_id(id):
    """Get an episode by ID including its appearances."""
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(episode.to_dict(include_appearances=True)), 200

@bp.route("/episodes/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    """Delete an episode and its appearances."""
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"message": "Episode deleted successfully"}), 200
