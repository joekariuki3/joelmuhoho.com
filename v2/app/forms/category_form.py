from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from app.utils import CategoryConstants


class CategoryForm(FlaskForm):
    name = StringField('Category Name',
                        validators=[DataRequired(message=CategoryConstants.CATEGORY_NAME_REQUIRED_MESSAGE)],
                        render_kw={'placeholder': CategoryConstants.CATEGORY_NAME_PLACEHOLDER})
    submit = SubmitField("Submit")