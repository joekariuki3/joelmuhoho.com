from flask import Blueprint, render_template
from app.models import Category, User
from sqlalchemy.exc import OperationalError
from config import Config
from app.utils import CategoryConstants
from typing import List

public = Blueprint('public', __name__)

@public.route('/')
def home() -> 'flask.Response':
    """
    The home page of the public site.
    Returns a rendered template of the home page.
    """
    try:
        # get all categories
        categories: List[Category] = Category.get_all()
        root_user = User.get_by_email(Config.ROOT_EMAIL)
        # Render the template
        return render_template('public/index.html',
                               categories=categories,
                               user=root_user)
    except OperationalError as e:
        # If there is an operational error, call the custom error handler
        return handle_db_error(e)

def handle_db_error(error: OperationalError) -> 'tuple[flask.Response, int]':
    """
    A custom error handler to handle database operational errors.
    Args:
        error: The error that is raised when there is an operational error.
    Returns:
        A rendered template of the error page with a 500 status code.
    """
    message="Oops! It seems there's an issue with the database. Please check if the tables are set up correctly."
    return render_template('public/error.html', message=message), 500

@public.route('/resume')
def resume() -> 'flask.Response':
    return render_template('public/resume.html')