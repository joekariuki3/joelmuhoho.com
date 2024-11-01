from .basemodel import BaseModel, db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel, UserMixin):
    __tablename__ = 'users'

    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)

    # Relationships
    projects = db.relationship('Project', backref='users', lazy=True)

    def __init__(self, first_name, last_name, email, password):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.username = self.set_username(first_name, last_name)
        self.email = email
        self.password = generate_password_hash(password)
        self.active = True

    def set_username(self, first_name: str, last_name: str) -> str:
        """
        Set the username for the user.

        :param first_name: The first name of the user.
        :type first_name: str
        :param last_name: The last name of the user.
        :type last_name: str
        :return: The username for the user.
        :rtype: str
        """
        username = first_name[0] + '.' + last_name
        return username
    def check_password(self, password) -> bool:
        """
        Check if the provided password matches the user's password.

        :param password: The password to check.
        :type password: str
        :return: True if the password matches, False otherwise.
        :rtype: bool
        """
        return check_password_hash(self.password, password)

    def get_id(self):
        """
        Get the unique identifier for the user.

        :return: The unique identifier for the user.
        :rtype: str
        """
        return self.id