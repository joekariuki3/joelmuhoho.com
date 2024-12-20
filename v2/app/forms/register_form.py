from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional
from app.utils import PasswordConstants, EmailConstants, NameConstants, RoleConstants, RegistrationConstants

class RegisterForm(FlaskForm):
    """Register form"""
    first_name = StringField('Your First Name',
                             validators=[DataRequired(message=NameConstants.FIRST_NAME_REQUIRED_MESSAGE)],
                             render_kw={'placeholder': "First Name"})
    last_name = StringField('Your Last Name',
                            validators=[DataRequired(message=NameConstants.LAST_NAME_REQUIRED_MESSAGE)],
                            render_kw={'placeholder': "Last Name"})
    username = StringField('Your Username',
                           validators=[Optional()],
                           render_kw={'placeholder': NameConstants.USERNAME_PLACEHOLDER})
    email = StringField('Your Email',
                        validators=[
                            DataRequired(message=EmailConstants.EMAIL_REQUIRED_MESSAGE),
                            Email(message=EmailConstants.EMAIL_ERROR_MESSAGE)],
                        render_kw={'placeholder': "name@mail.com"})
    role_id = SelectField('Role', choices=[],
                          validators=[DataRequired(message=RoleConstants.ROLE_REQUIRED_MESSAGE)],
                          render_kw={'placeholder': RoleConstants.ROLE_PLACEHOLDER})
    password = PasswordField('Password',
                             validators=[
                                 Length(
                                     min=PasswordConstants.MIN_PASSWORD_LENGTH,
                                     message=PasswordConstants.PASSWORD_ERROR_MESSAGE),
                                 EqualTo('confirm_password', message=PasswordConstants.CONFIRM_PASSWORD_ERROR_MESSAGE),
                                 DataRequired(message=PasswordConstants.PASSWORD_REQUIRED_MESSAGE)
                                 ],
                             render_kw={'placeholder': "••••••••"})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         Length(min=PasswordConstants.MIN_PASSWORD_LENGTH,
                                                message=PasswordConstants.PASSWORD_ERROR_MESSAGE),
                                         EqualTo('password', message=PasswordConstants.CONFIRM_PASSWORD_ERROR_MESSAGE),
                                         DataRequired(message=PasswordConstants.CONFIRM_PASSWORD_REQUIRED_MESSAGE)
                                         ],
                                     render_kw={'placeholder': "••••••••"})
    profession = StringField('Your Profession', render_kw={'placeholder': RegistrationConstants.PROFESSION_PLACEHOLDER})
    bio = TextAreaField('Your Bio', render_kw={'placeholder': RegistrationConstants.BIO_PLACEHOLDER})
    github_url = StringField('GitHub URL', render_kw={'placeholder': RegistrationConstants.GITHUB_URL_PLACEHOLDER})
    linkedin_url = StringField('LinkedIn URL', render_kw={'placeholder': RegistrationConstants.LINKEDIN_URL_PLACEHOLDER})
    twitter_url = StringField('Twitter URL', render_kw={'placeholder': RegistrationConstants.TWITTER_URL_PLACEHOLDER})
    profile_image_url = StringField('Profile Image URL', render_kw={'placeholder': RegistrationConstants.PROFILE_IMAGE_URL_PLACEHOLDER})
    submit = SubmitField('Create an account')

    def __init__(self, edit_mode=False, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        # If edit_mode is True, make password fields optional
        if edit_mode:
            self.password.validators = [Optional()]
            self.confirm_password.validators = [Optional()]
            self.username.validators = [DataRequired(message=NameConstants.USERNAME_REQUIRED_MESSAGE)]
