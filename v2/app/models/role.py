from .basemodel import BaseModel, db
from app.utils import RoleConstants
from app.models import User

class Role(BaseModel):
    __tablename__ = 'roles'

    name = db.Column(db.String(80), unique=True, nullable=False)

    def __str__(self):
        return self.name.capitalize()

    # get roles except root
    @classmethod
    def get_all(cls):
        return cls.query.filter(Role.name != RoleConstants.ROOT, Role.name != RoleConstants.DEFAULT).all()

    # when deleting a role set users with roles that is being deleted to role default
    def delete(self):
        users = User.query.filter_by(role_id=self.id).all()
        default_role = Role.query.filter_by(name=RoleConstants.DEFAULT).first()
        for user in users:
            user.role_id = default_role.id
            db.session.add(user)
        db.session.commit()
        return super().delete()