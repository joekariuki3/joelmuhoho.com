from app import db
from typing import Tuple, List, Optional

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    demo_url = db.Column(db.String(200), nullable=False)
    github_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Project {self.title}>'

    def save(self) -> Tuple[str, int]:
        """
        Save the project to the database.

        :return: A tuple containing a message and a status code.
        :rtype: Tuple[str, int]
        """
        try:
            db.session.add(self)
            db.session.commit()
            message: str = f'Project {self.title} saved successfully.'
            return message, 200
        except Exception as e:
            db.session.rollback()
            message: str = f'Failed to save project {self.title}: {str(e)}'
            return message, 500

    def delete(self) -> Tuple[str, int]:
        """
        Delete the project from the database.

        :return: A tuple containing a message and a status code.
        :rtype: Tuple[str, int]
        """
        try:
            db.session.delete(self)
            db.session.commit()
            message = f'Project {self.title} deleted successfully.'
            return message, 200
        except Exception as e:
            db.session.rollback()
            message = f'Failed to delete project {self.title}: {str(e)}'
            return message, 500

    def update(self, data):
        try:
            for key, value in data.items():
                setattr(self, key, value)
            db.session.commit()
            message = f'Project {self.title} updated successfully.'
            return message, 200
        except Exception as e:
            db.session.rollback()
            message = f'Failed to update project {self.title}: {str(e)}'
            return message, 500

    @classmethod
    def get_all(cls) -> Optional[List['Project']]:
        """
        Retrieve all project records from the database.

        :return: A list of all Project objects or None if an error occurs.
        :rtype: List[Project] or None
        """
        try:
            return cls.query.all()
        except Exception as e:
            return None

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
    def get_by_id(cls, id: int) -> Optional[List['Project']]:
        """
        Retrieve a project record from the database by its ID.

        :param id: The ID of the project to retrieve.
        :type id: int
        :return: The Project object with the specified ID or None if an error occurs.
        :rtype: Project or None
        """
        try:
            return cls.query.get_or_404(id)
        except Exception as e:
            return None
