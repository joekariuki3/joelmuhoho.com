from .basemodel import BaseModel, db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils import RoleConstants
from config import Config


class User(BaseModel, UserMixin):
    __tablename__ = 'users'

    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    profession = db.Column(db.String(100))
    bio = db.Column(db.Text)
    github_url = db.Column(db.String(200))
    linkedin_url = db.Column(db.String(200))
    twitter_url = db.Column(db.String(200))
    profile_image_url = db.Column(db.String(200))

    # Foreign keys
    role_id = db.Column(db.String, db.ForeignKey('roles.id'), nullable=False)

    # Relationships
    projects = db.relationship('Project', backref='users', lazy=True)
    role = db.relationship('Role', backref='users', lazy=True)

    def __init__(self, first_name, last_name, email, role_id, password, profession=None, bio=None, github_url=None, linkedin_url=None, twitter_url=None, profile_image_url=None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.username = self.set_username(first_name, last_name)
        self.email = email
        self.role_id = role_id
        self.password = generate_password_hash(password)
        self.active = True
        self.profession = profession
        self.bio = bio
        self.github_url = github_url
        self.linkedin_url = linkedin_url
        self.twitter_url = twitter_url
        self.profile_image_url = profile_image_url if profile_image_url else Config.DEFAULT_PROFILE_IMAGE_URL

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
    def is_root(self):
        """
        Check if the user is a root user.

        :return: True if the user is a root user, False otherwise.
        :rtype: bool
        """
        return self.role.name == RoleConstants.ROOT

    @classmethod
    def get_by_email(cls, email):
        """
        Retrieve a user record from the database by their email.

        :param email: The email of the user to retrieve.
        :type email: str
        :return: The User object with the specified email or None if not found.
        :rtype: User or None
        """
        return cls.query.filter_by(email=email).first()