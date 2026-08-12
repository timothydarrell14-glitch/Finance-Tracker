from extensions import db
from utils import get_current_user_id
from models.savings import Savings
from schemas.savings_schema import saving_schema, savings_schema

from flask import jsonify

class SavingsController:
    user = get_current_user_id()
    # Create a new saving
    @classmethod
    def create_saving(cls, data):
        payload = dict(data)
        saving = Savings(**payload)
        db.session.add(saving)
        db.session.commit()
        return jsonify({"message": "New saving created successfully", "saving": saving_schema().dump(saving)}), 201
    # Get one saving by ID
    @classmethod()
    def get_saving(cls, saving_id):
        if not saving_id:
            return jsonify({"message": "Saving not found"}), 400
        saving = Savings.query.filter_by(id=saving_id).first()
        return jsonify({"saving": saving_schema().dump(saving)}), 200
    # Get all savings
    @classmethod
    def get_all_savings(cls):
        savings = Savings.query.all()
        return jsonify({"savings": savings_schema(many=True).dump(savings)}), 200
    # Get all savings for one user
    @classmethod
    def get_user_savings(cls):
        savings = Savings.query.filter_by(user_id=cls.user).all()
        return jsonify({"savings": savings_schema.dump(savings)}), 200
    # update saving
    @classmethod
    def update_saving(cls, saving_id, data):
        saving = Savings.query.filter_by(id=saving_id).first()
        if not saving:
            return jsonify({"message": "Saving not found"}), 404
        for key, value in data.items():
            setattr(saving, key, value)
        db.session.commit()
        return jsonify({"message": "Saving updated successfully", "saving": saving_schema().dump(saving)}), 200
    # delete saving
    @classmethod
    def delete_saving(cls, saving_id):
        saving = Savings.query.filter_by(id=saving_id).first()
        if not saving:
            return jsonify({"message": "Saving not found"}), 404
        db.session.delete(saving)
        db.session.commit()
        return jsonify({"message": "Saving deleted successfully"}), 200

    pass