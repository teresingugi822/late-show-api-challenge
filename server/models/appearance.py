from ..app import db

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)

    guest = db.relationship('Guest', back_populates='appearances')
    episode = db.relationship('Episode', back_populates='appearances')

    def to_dict(self):
        """Serialize appearance data."""
        return {
            'id': self.id,
            'rating': self.rating,
            'guest_id': self.guest_id,
            'episode_id': self.episode_id
        }

    @staticmethod
    def validate_rating(rating):
        """Ensure rating is between 1 and 5."""
        return rating in range(1, 6)
