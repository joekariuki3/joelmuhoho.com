from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, length

class LoginForm(FlaskForm):
    """Login form"""
    email = StringField('Your Email',
                        validators=[
                            DataRequired(message="Please enter your email address."),
                            Email(message="Please enter a valid email address.")],
                        render_kw={'placeholder': "name@mail.com"})
    password = PasswordField('Password',
                             validators=[
                                 Length(min=4, message="Password must be at least 4 characters long."),
                                 DataRequired(message="Password is required")
                                 ],
                             render_kw={'placeholder': "••••••••"})
    submit = SubmitField('Sign In')
