from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from app.utils import PasswordConstants, EmailConstants

class LoginForm(FlaskForm):
    """Login form"""
    email = StringField('Your Email',
                        validators=[
                            DataRequired(message=EmailConstants.EMAIL_REQUIRED_MESSAGE),
                            Email(message=EmailConstants.EMAIL_ERROR_MESSAGE)
                            ],
                        render_kw={'placeholder': "name@mail.com"})
    password = PasswordField('Password',
                             validators=[
                                 Length(
                                     min=PasswordConstants.MIN_PASSWORD_LENGTH,
                                     message=PasswordConstants.PASSWORD_ERROR_MESSAGE),
                                 DataRequired(message=PasswordConstants.PASSWORD_REQUIRED_MESSAGE)
                                 ],
                             render_kw={'placeholder': "••••••••"})
    submit = SubmitField('Sign In')
