from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
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
    from app.models import User, Project, Category
    with app.app_context():
        db.create_all()

    # Register Blueprints
    from app.routes.public import public
    from app.routes.admin import admin
    from app.routes.auth import auth
    app.register_blueprint(public)
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(auth, url_prefix='/auth')

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    # Redirect to login page if not authenticated
    login_manager.login_view = 'auth.login'
    # Flash message category for unauthenticated access
    login_manager.login_message_category = 'warning'

    @login_manager.user_loader
    def load_user(user_id):
        return User.get_by_id(user_id)

    return app
