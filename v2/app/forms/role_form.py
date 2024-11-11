from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from app.utils import RoleConstants

class RoleForm(FlaskForm):
    name = SelectField('Role', choices=[(role, role) for role in RoleConstants.ROLES], validators=[DataRequired()])
    submit = SubmitField("Submit")