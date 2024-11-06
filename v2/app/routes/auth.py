from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.models import User
from app.forms import LoginForm, RegisterForm

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
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            password = request.form.get('password')
            user = User( first_name=first_name, last_name=last_name, email=email, password=password)
            message, status = user.save()
            if status == 200:
                flash(message, 'success')
                return redirect(url_for('auth.login'))
            flash(message, 'danger')
        else:
            flash('Please correct the errors below and try again.', 'danger')
    return render_template('auth/register.html', form=form)
