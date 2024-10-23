# app/admin.py
from flask import Blueprint, render_template, redirect, url_for, request
from app import db
from app.models.project import Project
from app.models.category import Category

admin = Blueprint('admin', __name__)

@admin.route('/')
def admin_dashboard():
    categories = Category.query.all()
    category_project_counts = {category.id: Project.query.filter_by(category_id=category.id).count() for category in categories}
    return render_template('admin/dashboard.html', categories=categories, category_project_counts=category_project_counts)

@admin.route('/add_project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category_id = request.form['category_id']
        image_url = request.form['image_url']
        demo_url = request.form['demo_url']
        github_url = request.form['github_url']

        new_project = Project(
            title=title, description=description, category_id=category_id,
            image_url=image_url, demo_url=demo_url, github_url=github_url
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('admin.admin_dashboard'))

    categories = Category.query.all()
    return render_template('admin/add_project.html', categories=categories)

@admin.route('/categories/add', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('admin.manage_categories'))

    return render_template('admin/add_category.html')
@admin.route('/manage_categories')
def manage_categories():
    categories = Category.query.all()
    return render_template('admin/manage_categories.html', categories=categories)

@admin.route('/edit_category/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)

    if request.method == 'POST':
        category.name = request.form['name']
        db.session.commit()
        return redirect(url_for('admin.manage_categories'))

    return render_template('admin/edit_category.html', category=category)

@admin.route('/delete_category/<int:category_id>', methods=['POST'])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('admin.manage_categories'))

@admin.route('/manage_projects')
def manage_projects():
    projects = Project.query.all()
    return render_template('admin/manage_projects.html', projects=projects)

@admin.route('/edit_project/<int:project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == 'POST':
        project.title = request.form['title']
        project.description = request.form['description']
        project.category_id = request.form['category_id']
        project.image_url = request.form['image_url']
        project.demo_url = request.form['demo_url']
        project.github_url = request.form['github_url']

        db.session.commit()
        return redirect(url_for('admin.manage_projects'))

    categories = Category.query.all()
    return render_template('admin/edit_project.html', project=project, categories=categories)

@admin.route('/delete_project/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('admin.manage_projects'))

