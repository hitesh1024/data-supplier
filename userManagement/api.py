"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from .models import db, RegestrationForm, LoginForm, User
import json

api = Blueprint('userManagement', __name__)


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


bcrypt = Bcrypt()


@login_manager.user_loader
def load_user(user_id):
    print('helloWorld i reached here')
    return User.query.get(int(user_id))


@api.route('/')
@api.route('/home')
def home():
    return render_template('home.html')


@api.route('/register', methods=['get', 'post'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('userManagement.home'))
    form = RegestrationForm(csrf_enabled=False)
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        # create user
        user = User(username=form.username.data, email=form.email.data, password=hashed_pwd)
        print(user)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created!', 'success')
        return redirect(url_for('userManagement.login'))
    return render_template('register.html', title='Register', form=form)


@api.route('/login', methods=['get', 'post'])
def login():
    print(current_user)
    form = LoginForm(csrf_enabled=False)
    # data = json.loads(request.data)

    # print(data)

    if current_user.is_authenticated:
        return "redirect(url_for('userManagement.home'))"
    if form.validate_on_submit():
        # return 'i reached here'
        user = User.query.filter_by(email=form.email.data).first()
        # print(user)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            print(current_user.id)
            # return 'Login Successful'
            return jsonify(user.username)
        else:
            return 'Login unsuccessful please check email and password'

    return "jsonify(render_template('login.html', title='Login', form=form))"


@api.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')


@api.route('/about')
def about():
    return render_template('about.html')


@api.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('userManagement.home'))
