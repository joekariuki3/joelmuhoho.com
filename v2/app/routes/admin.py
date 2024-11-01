# app/admin.py
from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models import Project, Category, User
from typing import List
from flask_login import login_required, current_user

admin = Blueprint('admin', __name__)


@admin.route('/')
@login_required
def admin_dashboard() -> 'flask.Response':
    """
    Renders the admin dashboard
    :return: A rendered template of the admin dashboard
    """
    categories: List[Category] = Category.get_all()
    if not categories:
        categories = []
        flash('No categories found. Please add some categories first.', 'warning')
    projects_count = Project.get_by_user(current_user.id)
    if not projects_count:
        projects_count = 0
        flash('No projects found. Please add some projects first.', 'warning')
    return render_template('admin/dashboard.html', categories=categories, projects_count=len(projects_count))

@admin.route('/add_project', methods=['GET', 'POST'])
@login_required
def add_project() -> 'flask.Response':
    """
    Add a new project to the database.
    :return: A redirect to the manage projects page or a rendered template of the add project page.
    """
    if request.method == 'POST':
        data: dict = request.form.to_dict()
        print(data)
        new_project: Project = Project(
            title=data.get('title'),
            description=data.get('description'),
            category_id=data.get('category_id'),
            image_url=data.get('image_url'),
            demo_url=data.get('demo_url'),
            github_url=data.get('github_url'),
            user_id=current_user.id
        )
        message, status = new_project.save()
        if status != 200:
            flash(message, 'danger')
            return redirect(url_for('admin.add_project'))
        flash(message, 'success')
        return redirect(url_for('admin.manage_projects'))

    categories: List[Category] = Category.get_all()
    return render_template('admin/add_project.html', categories=categories)

@admin.route('/categories/add', methods=['GET', 'POST'])
@login_required
def add_category() -> 'flask.Response':
    """
    Add a new category to the database.
    :return: A redirect to the manage categories page or a rendered template of the add category page.
    """
    if request.method == 'POST':
        name: str = request.form.get('name')
        new_category = Category(name=name)
        message, status = new_category.save()
        if status == 200:
            flash(message, 'success')
            return redirect(url_for('admin.manage_categories'))
        flash(message, 'danger')
    return render_template('admin/add_category.html')

@admin.route('/manage_categories')
@login_required
def manage_categories():
    categories = Category.get_all()
    if not categories:
        categories = []
        flash('No categories found. Please add some categories first.', 'warning')
    return render_template('admin/manage_categories.html', categories=categories)

@admin.route('/edit_category/<category_id>', methods=['GET', 'POST'])
@login_required
def edit_category(category_id: str) -> 'flask.Response':
    """
    Edit an existing category.
    :param category_id: The ID of the category to edit.
    :return: A redirect to the manage categories page or a rendered template of the edit category page.
    """
    category: Category = Category.get_by_id(category_id)
    if not category:
        category = []
        flash('Category not found.', 'danger')
    if request.method == 'POST':
        data: dict = request.form.to_dict()
        message, status = category.update(data)
        if status == 200:
            flash(message, 'success')
            return redirect(url_for('admin.manage_categories'))
        flash(message, 'danger')
    return render_template('admin/edit_category.html', category=category)

@admin.route('/delete_category/<category_id>', methods=['POST'])
@login_required
def delete_category(category_id: str) -> 'flask.Response':
    """
    Delete a category from the database.
    :param category_id: The ID of the category to delete.
    :return: A redirect to the manage categories page.
    """
    category: Category = Category.get_by_id(category_id)
    message, status = category.delete()
    if status == 200:
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('admin.manage_categories'))

@admin.route('/manage_projects')
@login_required
def manage_projects() -> 'flask.Response':
    """
    Renders the manage projects page
    :return: A rendered template of the manage projects page, with categories and their projects
    """
    categories: List[Category] = Category.get_all()
    if not categories:
        categories = []
        flash('No categories found. Please add some categories first.', 'warning')
    return render_template('admin/manage_projects.html', categories=categories)

@admin.route('/edit_project/<project_id>', methods=['GET', 'POST'])
@login_required
def edit_project(project_id: str) -> 'flask.Response':
    """
    Edit an existing project.
    :param project_id: The ID of the project to edit.
    :return: A redirect to the manage projects page or a rendered template of the edit project page.
    """
    categories: List[Category] = Category.get_all()
    project: Project = Project.get_by_id(project_id)
    if not categories:
        categories = []
        flash('No categories found. Please add some categories first.', 'warning')
        return redirect(url_for('admin.manage_projects'))
    if request.method == 'POST':
        data: dict = request.form.to_dict()
        message, status = project.update(data)
        if status == 200:
            flash(message, 'success')
            return redirect(url_for('admin.manage_projects'))
        flash(message, 'danger')
    return render_template('admin/edit_project.html', project=project, categories=categories)

@admin.route('/delete_project/<project_id>', methods=['POST'])
@login_required
def delete_project(project_id: str) -> 'flask.Response':
    """
    Delete a project from the database.
    :param project_id: The ID of the project to delete.
    :return: A redirect to the manage projects page.
    """
    project: Project = Project.get_by_id(project_id)
    message, status = project.delete()
    if status == 200:
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('admin.manage_projects'))