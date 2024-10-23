from flask import Blueprint, render_template
from app.models.project import Project
from app.models.category import Category
from sqlalchemy.exc import OperationalError

public = Blueprint('public', __name__)

@public.route('/')
def home():
    try:
        categories = Category.query.all()
        full_stack_category = categories[0]
        front_end_category = categories[1]
        email_category = categories[2]
        return render_template('index.html',full_stack_category=full_stack_category, front_end_category=front_end_category, email_category=email_category)
    except OperationalError as e:
        return handle_db_error(e)  # Call the custom error handler directly

def handle_db_error(error):
    return render_template('error.html', message="Oops! It seems there's an issue with the database. Please check if the tables are set up correctly."), 500
