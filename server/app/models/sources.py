from extensions import db
from marshmallow import EXCLUDE

class Sources(db.Model):
    __tablename__ = "sources"

    unknown = EXCLUDE

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    method = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="sources", lazy=True)