# app/admin.py
from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models import Project, Category, User, Role
from typing import List
from flask_login import login_required, current_user
from app.forms import ProjectForm, CategoryForm, RoleForm, RegisterForm
from app.utils import ProjectConstants, CategoryConstants, RoleConstants, RegistrationConstants

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
    projects_count = len(Project.get_by_user(current_user.id) or [])
    if projects_count == 0:
        flash('No projects found. Please add some projects first.', 'warning')
    users = User.get_all() or []
    users_count = len(users)
    return render_template('admin/dashboard.html', categories=categories, projects_count=projects_count, users_count=users_count, users=users)

@admin.route('/add_project', methods=['GET', 'POST'])
@login_required
def add_project() -> 'flask.Response':
    """
    Add a new project to the database.
    :return: A redirect to the manage projects page or a rendered template of the add project page.
    """
    form: ProjectForm = ProjectForm()
    form.category_id.choices = [(category.id, category.name) for category in Category.get_all() or []]
    title: str = ProjectConstants.TITLE.get('ADD')
    if request.method == 'POST' and form.validate_on_submit():
        data: dict = request.form.to_dict()
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
        else:
            flash(message, 'success')
            return redirect(url_for('admin.manage_projects'))
    return render_template('admin/add_project.html', form=form, title=title)

@admin.route('/categories/add', methods=['GET', 'POST'])
@login_required
def add_category() -> 'flask.Response':
    """
    Add a new category to the database.
    :return: A redirect to the manage categories page or a rendered template of the add category page.
    """
    form: CategoryForm = CategoryForm()
    title: str = CategoryConstants.TITLE.get('ADD')
    if request.method == 'POST':
        name: str = request.form.get('name')
        new_category = Category(name=name)
        message, status = new_category.save()
        if status == 200:
            flash(message, 'success')
            return redirect(url_for('admin.manage_categories'))
        flash(message, 'danger')
    return render_template('admin/add_category.html', form=form, title=title)

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
    form: CategoryForm = CategoryForm()
    title: str = CategoryConstants.TITLE.get('EDIT')
    form.name.data = category.name
    if request.method == 'POST':
        if form.validate_on_submit():
            data: dict = request.form.to_dict()
            message, status = category.update(data)
            if status == 200:
                flash(message, 'success')
                return redirect(url_for('admin.manage_categories'))
            flash(message, 'danger')
        else:
             # Print or log the form errors
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in {getattr(form, field).label.text}: {error}")
            flash('correct the errors below and try again.', 'danger')
    return render_template('admin/edit_category.html', form=form, title=title, category_id=category.id)

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
    form: ProjectForm = ProjectForm()
    title: str = ProjectConstants.TITLE.get('EDIT')

    project: Project = Project.get_by_id(project_id)
    categories: List[Category] = Category.get_all()
    if not project:
        flash('Project not found.', 'danger')
        return redirect(url_for('admin.manage_projects'))

    if not categories:
        categories = []
        flash('No categories found. Please add some categories first.', 'warning')
        return redirect(url_for('admin.manage_projects'))

    form.title.data = project.title
    form.description.data = project.description
    form.category_id.data = project.category_id
    form.category_id.choices = [(category.id, category.name) for category in categories]
    form.image_url.data = project.image_url
    form.demo_url.data = project.demo_url
    form.github_url.data = project.github_url
    if request.method == 'POST':
        if form.validate_on_submit():
            data: dict = request.form.to_dict()
            message, status = project.update(data)
            if status == 200:
                flash(message, 'success')
                return redirect(url_for('admin.manage_projects'))
            flash(message, 'danger')
        else:
            flash('Please correct the errors below and try again.', 'danger')
    return render_template('admin/edit_project.html', project_id=project_id, form=form, title=title)

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

@admin.route('/manage_roles')
@login_required
def manage_roles() -> 'flask.Response':
    if current_user.is_root():
        roles = Role.get_all() or []
    # If the user is not a root user, only show the roles that the user has access to
    else:
        roles = [current_user.role] or []
    if not roles:
        flash('No roles found. Please add some roles first.', 'warning')
    return render_template('admin/manage_roles.html', roles=roles)

@admin.route('/add_role', methods=['GET', 'POST'])
@login_required
def add_role() -> 'flask.Response':
    title = RoleConstants.TITLE.get('ADD')
    form = RoleForm()
    roles_from_db = Role.get_all() or []
    if request.method == 'POST':
        name = request.form.get('name')
        if name in [role.name for role in roles_from_db]:
            flash('Role already exists.', 'danger')
            return redirect(url_for('admin.add_role'))
        new_role = Role(name=name)
        message, status = new_role.save()
        if status == 200:
            flash(message, 'success')
            return redirect(url_for('admin.manage_roles'))
        flash(message, 'danger')
    return render_template('admin/add_role.html', form=form, title=title)

@admin.route('/delete_role/<role_id>', methods=['POST'])
@login_required
def delete_role(role_id: str) -> 'flask.Response':
    role: Role = Role.get_by_id(role_id)
    if role.name == RoleConstants.ROOT or role.name == RoleConstants.DEFAULT:
        flash('Cannot delete root or default role.', 'danger')
        return redirect(url_for('admin.manage_roles'))
    message, status = role.delete()
    if status == 200:
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('admin.manage_roles'))

@admin.route('/manage_users')
@login_required
def manage_users() -> 'flask.Response':
    if current_user.is_root():
        users = User.get_all() or []
    else:
        users = [current_user]
    if not users:
        flash('No users found. Please add some users first.', 'warning')
    return render_template('admin/manage_users.html', users=users)

@admin.route('/edit_user/<user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id: str) -> 'flask.Response':
    form = RegisterForm(edit_mode=True)
    title = RegistrationConstants.TITLE.get('EDIT')
    roles = Role.get_all() or []
    if not roles:
        flash('No roles found. Please add some roles first.', 'warning')
    user = User.query.filter_by(id=user_id).first()
    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('admin.manage_users'))

    if user.role.name != RoleConstants.DEFAULT:
        form.role_id.data = str(user.role_id)

    form.first_name.data = user.first_name
    form.last_name.data = user.last_name
    form.username.data = user.username
    form.email.data = user.email
    form.profession.data = user.profession
    form.bio.data = user.bio
    form.github_url.data = user.github_url
    form.linkedin_url.data = user.linkedin_url
    form.twitter_url.data = user.twitter_url
    form.profile_image_url.data = user.profile_image_url
    form.role_id.choices = [(role.id, role.name) for role in roles]
    if request.method == 'POST':
        if form.validate_on_submit():
            data = request.form.to_dict()
            message, status = user.update(data)
            if status == 200:
                flash(message, 'success')
                return redirect(url_for('admin.manage_users'))
            flash(message, 'danger')
        else:
            print(form.errors)
            flash(f'Please correct the errors below and try again.{form.errors}', 'danger')
    return render_template('admin/edit_user.html', user_id=user.id, form=form, title=title)

@admin.route('/delete_user/<user_id>', methods=['POST'])
@login_required
def delete_user(user_id: str) -> 'flask.Response':
    user: User = User.get_by_id(user_id)
    if user.role.name == RoleConstants.ROOT:
        flash('Cannot delete user with root role.', 'danger')
        return redirect(url_for('admin.manage_users'))
    message, status = user.delete()
    if status == 200:
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('admin.manage_users'))