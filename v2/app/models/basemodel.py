from app.models import db
from uuid import uuid4
from datetime import datetime
from typing import Tuple, List, Optional

class BaseModel(db.Model):

    __abstract__ = True

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = db.Column(db.DateTime)
    restored_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.id}>'
    def __str__(self):
        return super().__str__()


    def customMessage(self, action: str, error=None) -> str:
        # Common success or failure message template
        """
        Return a string with a custom message describing the success or failure of an action.

        :param action: The action that was attempted (e.g. 'save', 'update', 'delete', etc.).
        :type action: str
        :param error: An error message if the action failed, or None if it was successful.
        :type error: str or None
        :return: A string describing the outcome of the action.
        :rtype: str
        """
        status = f"Failed: {error}" if error else "was successful"

        # Mapping of actions to user-friendly past tense verbs
        action_map = {
            'save': 'Creation',
            'update': 'Update',
            'soft delete': 'Soft Delete',
            'restore': 'Restoration',
            'delete': 'Deletion',
        }
        verb = action_map.get(action, action)

        # Use getattr to safely access attributes and fall back to 'id' if none are available
        identifier = (
            getattr(self, 'name', None) or
            getattr(self, 'title', None) or
            f"{getattr(self, 'first_name', '')} {getattr(self, 'last_name', '')}".strip() or
            getattr(self, 'id', 'Unknown')
        )
        return f"{self.__class__.__name__} {identifier} {verb} {status}."



    def save(self) -> Tuple[str, int]:
        """
        Save the model to the database.

        :return: A tuple containing a message and a status code.
        :rtype: Tuple[str, int]
        """
        try:
            db.session.add(self)
            db.session.commit()
            message: str =  self.customMessage( 'save')
            return message, 200
        except Exception as e:
            db.session.rollback()
            message: str = self.customMessage('save',error=e)
            return message, 500

    def update(self, data) -> Tuple[str, int]:
        """
        Update the model in the database.

        :return: A tuple containing a message and a status code.
        :rtype: Tuple[str, int]
        """
        try:
            for key, value in data.items():
                setattr(self, key, value)
            db.session.commit()
            message: str =  self.customMessage( 'update')
            return message, 200
        except Exception as e:
            db.session.rollback()
            message: str = self.customMessage('update',error=e)
            return message, 500
    def soft_delete(self) -> Tuple[str, int]:
        """
        Soft delete the model in the database.

        :return: A tuple containing a message and a status code.
        :rtype: Tuple[str, int]
        """
        try:
            self.deleted_at = datetime.now()
            db.session.commit()
            message: str =  self.customMessage( 'soft delete')
            return message, 200
        except Exception as e:
            db.session.rollback()
            message: str = self.customMessage('soft delete',error=e)
            return message, 500

    def delete(self) -> Tuple[str, int]:
        """
        Delete the model from the database.

        :return: A tuple containing a message and a status code.
        :rtype: Tuple[str, int]
        """
        try:
            db.session.delete(self)
            db.session.commit()
            message: str =  self.customMessage( 'delete')

            return message, 200
        except Exception as e:
            db.session.rollback()
            message: str = self.customMessage('delete',error=e)
            return message, 500

    def restore(self) -> Tuple[str, int]:
        """
        Restore the model from the deleted state.

        :return: A tuple containing a message and a status code.
        :rtype: Tuple[str, int]
        """
        try:
            self.deleted_at = None
            self.restored_at = datetime.now()
            db.session.commit()
            message: str =  self.customMessage( 'restore')

            return message, 200
        except Exception as e:
            db.session.rollback()
            message: str = self.customMessage('restore',error=e)
            return message, 500

    @classmethod
    def get_by_id(cls, id: int) -> Optional[List['Project']]:
        """
        Retrieve a model record from the database by its ID.

        :param id: The ID of the model to retrieve.
        :type id: int
        :return: The model object with the specified ID or None if an error occurs.
        :rtype: Model or None
        """
        try:
            return db.session.query(cls).get(id)
        except Exception as e:
            return None
    @classmethod
    def get_all(cls) -> Optional[List['Project']]:
        """
        Retrieve all model records from the database.

        :return: A list of all model objects or None if an error occurs.
        :rtype: List[Model] or None
        """
        try:
            return db.session.query(cls).all()
        except Exception as e:
            return None

    # get count
    @classmethod
    def get_count(cls) -> int:
        """
        Retrieve the total number of model records in the database.

        :return: The total number of model objects in the database.
        :rtype: int
        """
        return db.session.query(cls).count()