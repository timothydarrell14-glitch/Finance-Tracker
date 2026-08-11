from extensions import db
from marshmallow import EXCLUDE

class Transactions(db.Model):
    __tablename__ = "transactions"

    unknown = EXCLUDE

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey("sources.id"), nullable=False)
    source = db.relationship("Sources", back_populates="transactions", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="transactions", lazy=True)