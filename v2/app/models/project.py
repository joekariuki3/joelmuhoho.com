from .basemodel import BaseModel, db
from typing import Tuple, List, Optional

class Project(BaseModel):
    __tablename__ = 'projects'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200))
    demo_url = db.Column(db.String(200))
    github_url = db.Column(db.String(200))

    # Foreign keys
    category_id = db.Column(db.String, db.ForeignKey('categories.id'), nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, title, description, category_id, image_url, demo_url, github_url, user_id):
        super().__init__()
        self.title = title
        self.description = description
        self.category_id = category_id
        self.image_url = image_url
        self.demo_url = demo_url
        self.github_url = github_url
        self.user_id = user_id

    def __repr__(self):
        return f'<Project {self.title}>'


    @classmethod
    def get_by_category(cls, category_id: int) -> Optional[List['Project']]:
        """
        Retrieve all project records from the database that belong to the specified category.

        :param category_id: The ID of the category to retrieve projects for.
        :type category_id: int
        :return: A list of all Project objects that belong to the specified category or None if an error occurs.
        :rtype: List[Project] or None
        """
        try:
            return cls.query.filter_by(category_id=category_id).all()
        except Exception as e:
            return None

    @classmethod
    def get_by_user(cls, user_id: int) -> Optional[List['Project']]:
        """
        Retrieve all project records from the database that belong to the specified user.

        :param user_id: The ID of the user to retrieve projects for.
        :type user_id: int
        :return: A list of all Project objects that belong to the specified user or None if an error occurs.
        :rtype: List[Project] or None
        """
        try:
            return cls.query.filter_by(user_id=user_id).all()
        except Exception as e:
            return None