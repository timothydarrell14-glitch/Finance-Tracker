from extensions import db
from marshmallow import EXCLUDE

class Savings(db.Model):
    __tablename__ = "savings"

    unknown = EXCLUDE

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    amount = db.Column(db.Integer, nullable=False)
    goal = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="savings", lazy=True)