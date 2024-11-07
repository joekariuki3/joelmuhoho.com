from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from app.utils import ProjectConstants

class ProjectForm(FlaskForm):
    title = StringField('Title',
                        validators=[DataRequired(message=ProjectConstants.PROJECT_NAME_REQUIRED_MESSAGE)],
                        render_kw={'placeholder': ProjectConstants.PROJECT_NAME_PLACEHOLDER})
    description = TextAreaField('Description',
                              validators=[DataRequired(message=ProjectConstants.PROJECT_DESCRIPTION_REQUIRED_MESSAGE)],
                              render_kw={'placeholder': ProjectConstants.PROJECT_DESCRIPTION_PLACEHOLDER})
    category_id = SelectField('Select Category',
                           choices=[],
                           validators=[DataRequired(message=ProjectConstants.PROJECT_CATEGORY_REQUIRED_MESSAGE)],
                           render_kw={'placeholder': ProjectConstants.PROJECT_CATEGORY_PLACEHOLDER})
    image_url = StringField('Image URL', render_kw={'placeholder': ProjectConstants.PROJECT_IMAGE_URL_PLACEHOLDER})
    demo_url = StringField('Demo URL', render_kw={'placeholder': ProjectConstants.PROJECT_DEMO_URL_PLACEHOLDER})
    github_url = StringField('GitHub URL', render_kw={'placeholder': ProjectConstants.PROJECT_GITHUB_URL_PLACEHOLDER})
    submit = SubmitField("Submit")