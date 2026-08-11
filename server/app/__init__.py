import os

from flask import Flask
from flask_migrate import Migrate

from extensions import db, jwt, cors, ma

def create_app():
    app = Flask(__name__)

    migrate = Migrate(app, db)

    migrate.init_app(app, db)
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    ma.init_app(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL") or "sqlite:///finance_tracker.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY") or "jwt_secret_key_"
    return app