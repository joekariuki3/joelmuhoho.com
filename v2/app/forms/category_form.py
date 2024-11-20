from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from app.utils import CategoryConstants


class CategoryForm(FlaskForm):
    name = SelectField('Category Name',
                       choices=[],
                        validators=[DataRequired(message=CategoryConstants.CATEGORY_NAME_REQUIRED_MESSAGE)],
                        render_kw={'placeholder': CategoryConstants.CATEGORY_NAME_PLACEHOLDER})
    submit = SubmitField("Submit")