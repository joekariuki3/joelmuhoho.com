from app.models import BaseModel, db
from typing import  List, Optional

class Category(BaseModel):
    __tablename__ = 'categories'
    name = db.Column(db.String(50), unique=True, nullable=False)

    # relationships
    projects = db.relationship('Project', backref='categories', lazy=True)

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f'<Category {self.name}>'

    @classmethod
    def get_by_name(cls, name: str) -> Optional[List['Category']]:
        """
        Retrieve a category record from the database by its name.

        :param name: The name of the category to retrieve.
        :type name: str
        :return: The Category object with the specified name or None if an error occurs.
        :rtype: Category or None
        """
        try:
            return cls.query.filter_by(name=name).first()
        except Exception as e:
            return None