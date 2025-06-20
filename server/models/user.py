from werkzeug.security import generate_password_hash, check_password_hash
from ..app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def set_password(self, password):
        """Hash and set the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check a plain password against the hash."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Serialize user data."""
        return {
            'id': self.id,
            'username': self.username
        }
