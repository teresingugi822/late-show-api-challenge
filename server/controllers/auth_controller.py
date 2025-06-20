from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash
from ..app import db
from ..models.user import User

bp = Blueprint('auth', __name__)

@bp.route("/register", methods=["POST"])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Check required fields
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    # Check for duplicate username
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already taken"}), 400

    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully", "user": user.to_dict()}), 201


@bp.route("/login", methods=["POST"])
def login():
    """Log in an existing user and return a JWT."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
