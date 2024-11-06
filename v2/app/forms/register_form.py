from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    """Register form"""
    first_name = StringField('Your First Name',
                             validators=[DataRequired(message="Please enter your first name.")],
                             render_kw={'placeholder': "First Name"})
    last_name = StringField('Your Last Name',
                            validators=[DataRequired(message="Please enter your last name.")],
                            render_kw={'placeholder': "Last Name"})
    email = StringField('Your Email',
                        validators=[
                            DataRequired(message="Please enter your email address."),
                            Email(message="Please enter a valid email address.")],
                        render_kw={'placeholder': "name@mail.com"})
    password = PasswordField('Password',
                             validators=[
                                 Length(min=4, message="Password must be at least 4 characters long."),
                                 EqualTo('confirm_password', message="Passwords do not match."),
                                 DataRequired(message="Password is required")
                                 ],
                             render_kw={'placeholder': "••••••••"})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[
                                         Length(min=4, message="Password must be at least 4 characters long."),
                                         EqualTo('password', message="Passwords do not match."),
                                         DataRequired(message="Confirm password is required")
                                         ],
                                     render_kw={'placeholder': "••••••••"})
    submit = SubmitField('Create an account')
