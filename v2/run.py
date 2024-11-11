#!/usr/bin/env python3
from app import create_app

app = create_app()
def add_root():
    from app.models import User, db
    from app.models import Role
    from app.utils import RoleConstants
    from config import Config

    # add root role and default role
    # make sure role root does not exist 1st before creating it
    root_role = Role.query.filter_by(name=RoleConstants.ROOT).first()
    default_role = Role.query.filter_by(name=RoleConstants.DEFAULT).first()
    if not root_role:
        root_role = Role(name=RoleConstants.ROOT)
        db.session.add(root_role)
        db.session.commit()
    if not default_role:
        default_role = Role(name=RoleConstants.DEFAULT)
        db.session.add(default_role)
        db.session.commit()

    # add root user
    root_user = User.query.filter_by(email=Config.ROOT_EMAIL).first()
    if not root_user:
        # raise value error if root info missing in .env file
        if not Config.ROOT_FIRST_NAME or not Config.ROOT_LAST_NAME or not Config.ROOT_EMAIL or not Config.ROOT_PASSWORD:
            raise ValueError(RoleConstants.ROOT_USER_REQUIRED_MESSAGE)
        else:
            root_user = User(
                first_name=Config.ROOT_FIRST_NAME,
                last_name=Config.ROOT_LAST_NAME,
                email=Config.ROOT_EMAIL,
                role_id=root_role.id,
                password=Config.ROOT_PASSWORD
            )
            db.session.add(root_user)
            db.session.commit()
if __name__ == '__main__':
    with app.app_context():
        add_root()
    # Get the host from the configuration (SERVER_HOST)
    host = app.config.get('SERVER_HOST', '127.0.0.1')  # Default to 127.0.0.1 if not set
    app.run(host=host, debug=app.config['DEBUG'])