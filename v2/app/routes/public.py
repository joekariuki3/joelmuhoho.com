from flask import Blueprint, render_template
from app.models.project import Project
from app.models.category import Category
from sqlalchemy.exc import OperationalError

public = Blueprint('public', __name__)

@public.route('/')
def home() -> 'flask.Response':
    """
    The home page of the public site.
    Returns a rendered template of the home page.
    """
    try:
        # Get the categories
        full_stack_category: Category = Category.get_by_id(1)
        front_end_category: Category = Category.get_by_id(2)
        email_category: Category = Category.get_by_id(3)

        # Render the template
        return render_template('index.html',
                               full_stack_category=full_stack_category,
                               front_end_category=front_end_category,
                               email_category=email_category)
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
    return render_template('error.html', message="Oops! It seems there's an issue with the database. Please check if the tables are set up correctly."), 500
