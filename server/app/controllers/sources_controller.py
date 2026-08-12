from extensions import db
from utils import get_current_user_id
from models.sources import Sources
from schemas.sources_schema import source_schema, sources_schema

from flask import jsonify

class SourcesController:
    user = get_current_user_id()
    # Create a new source
    @classmethod
    def create_new_source(cls, data):
        payload = dict(data)
        new_source = Sources(**payload)
        db.session.add(new_source)
        db.session.commit()
        return jsonify({"message": "Source successfully created", "source": source_schema.dump(new_source)}), 201
    # Get one source by ID
    @classmethod
    def get_source(cls, source_id):
        source = Sources.query.filter_by(id=source_id).first()
        if not source:
            return jsonify({"message": "Source not found"}), 204
        return jsonify({"source": source_schema.dump(source)}), 200

    # Get all sources
    @classmethod
    def get_all_sources(cls):
        all_sources = Sources.query.all()
        if not all_sources:
            return jsonify({"message": "No source found"}), 204
        return jsonify({"sources": sources_schema.dump(all_sources)}), 200
    # Get all sources for a user
    @classmethod
    def get_sources_for_id(cls):
        all_sources = Sources.query.filter_by(user_id=cls.user).all()
        if not all_sources:
            return jsonify({"message": "Sources not found for user"})
        return jsonify({"sources": sources_schema.dump(all_sources)}), 200
    # update source
    @classmethod
    def update_source(cls, data, source_id):
        source = Sources.query.filter_by(id=source_id).first()
        if not source:
            return jsonify({"message": "Source not found"}), 404
        for key, value in data.items():
            setattr(source, key, value)
            db.session.commit()
        return jsonify({"message": "Source updated successfully", "source": source_schema.dump(source)}), 200
    # delete source
    @classmethod
    def delete_source(cls, source_id):
        source = Sources.query.filter_by(id=source_id).first()
        if not source:
            return jsonify({"message": "Source not found"}), 404
        db.session.delete(source)
        db.session.commit()
        return jsonify({"message": "Source deleted successfully"}), 200