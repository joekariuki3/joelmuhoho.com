from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Role
from app.forms import LoginForm, RegisterForm
from app.utils import RegistrationConstants

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()

            if user and user.check_password(password):
                login_user(user)
                flash('Logged in successfully!', 'success')
                return redirect(url_for('admin.admin_dashboard'))  # Redirect after successful login
            else:
                flash('Login failed. Please check your credentials and try again.', 'danger')
        else:
            flash('Please correct the errors below and try again.', 'danger')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    title = RegistrationConstants.TITLE.get('ADD')
    form = RegisterForm()
    roles = Role.get_all() or []
    if not roles:
        flash('No roles found. Please add some roles first.', 'warning')
    form.role_id.choices = [(role.id, role.name) for role in roles]
    if request.method == 'POST':
        if not current_user.is_root():
            flash('You are not authorized to register new users. contact your administrator', 'danger')
            return redirect(url_for('auth.register'))
        if form.validate_on_submit():
            data = form.data

            user = User(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email'),
                password=data.get('password'),
                role_id=data.get('role_id')
            )
            message, status = user.save()
            if status == 200:
                flash(message, 'success')
                return redirect(url_for('admin.manage_users'))
            flash(message, 'danger')
        else:
            flash('Please correct the errors below and try again.', 'danger')
    return render_template('auth/register.html', form=form, title=title)
