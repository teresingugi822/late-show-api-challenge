from ..app import db

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')

    def to_dict(self, include_appearances=False):
        """Serialize episode data."""
        data = {
            'id': self.id,
            'date': str(self.date),
            'number': self.number
        }
        if include_appearances:
            data['appearances'] = [app.to_dict() for app in self.appearances]
        return data
