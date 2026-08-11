from extensions import db
from marshmallow import EXCLUDE

class Users(db.Model):
    __tablename__ = "users"

    unknown = EXCLUDE

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    sources = db.relationship("Sources", back_populates="user", lazy=True)
    transactions = db.relationship("Transactions", back_populates="user", lazy=True)
    savings = db.relationship("Savings", back_populates="user", lazy=True)