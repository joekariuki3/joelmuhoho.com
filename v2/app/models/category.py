from app import db
from typing import Tuple, List, Optional

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    # relationships
    projects = db.relationship('Project', backref='categories', lazy=True)

    def __repr__(self):
        return f'<Category {self.name}>'
    def save(self) -> Tuple[str, int]:
        """
        Save the category to the database.

        :return: A tuple containing a message and a status code.
        :rtype: Tuple[str, int]
        """
        try:
            db.session.add(self)
            db.session.commit()
            message: str = f'Category {self.name} saved successfully.'
            return message, 200
        except Exception as e:
            db.session.rollback()
            message: str = f'Failed to save category {self.name}: {str(e)}'
            return message, 500

    def delete(self) -> Tuple[str, int]:
        """
        Delete the category from the database.

        :return: A tuple containing a message and a status code.
        :rtype: Tuple[str, int]
        """
        try:
            db.session.delete(self)
            db.session.commit()
            message = f'Category {self.name} deleted successfully.'
            return message, 200
        except Exception as e:
            db.session.rollback()
            message = f'Failed to delete category {self.name}: {str(e)}'
            return message, 500

    def update(self, data: dict) -> Tuple[str, int]:
        """
        Update the category with new data.

        :param data: The new data to update the category with.
        :type data: dict
        :return: A tuple containing a message and a status code.
        :rtype: Tuple[str, int]
        """
        try:
            for key, value in data.items():
                setattr(self, key, value)
            db.session.commit()
            message = f'Category {self.name} updated successfully.'
            return message, 200
        except Exception as e:
            db.session.rollback()
            message = f'Failed to update category {self.name}: {str(e)}'
            return message, 500

    @classmethod
    def get_all(cls) -> Optional[List['Category']]:
        """
        Retrieve all category records from the database.

        :return: A list of all Category objects or None if an error occurs.
        :rtype: List[Category] or None
        """
        try:
            return cls.query.all()
        except Exception:
            return None

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

    @classmethod
    def get_by_id(cls, id: int) -> Optional[List['Category']]:
        """
        Retrieve a category record from the database by its ID.

        :param id: The ID of the category to retrieve.
        :type id: int
        :return: The Category object with the specified ID or None if an error occurs.
        :rtype: Category or None
        """
        try:
            return cls.query.get_or_404(id)
        except Exception as e:
            return None
