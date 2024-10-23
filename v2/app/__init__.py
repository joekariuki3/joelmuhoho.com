from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig, ProductionConfig
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load environment variables based on the environment
    environment = os.getenv('FLASK_ENV', 'development')
    if environment == 'development':
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)

    # Initialize the database
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register Blueprints
    from app.routes.public import public
    from app.routes.admin import admin
    app.register_blueprint(public)
    app.register_blueprint(admin, url_prefix='/admin')  # Prefix all admin routes


    return app
