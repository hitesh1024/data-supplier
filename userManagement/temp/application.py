from flask import Flask, render_template, flash, redirect, url_for, request
from forms import RegestrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'Disaster'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_app0.db'
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'

# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)


# class User(db.Model, UserMixin):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#
#     def __repr__(self):
#         return f'User({self.username}, {self.email})'


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
#
#
# @app.route('/')
# @app.route('/home')
# def home():
#     return render_template('home.html')
#
#
# @app.route('/register', methods=['get', 'post'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = RegestrationForm()
#     if form.validate_on_submit():
#         hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#
#         create user
        # user = User(username=form.username.data, email=form.email.data, password=hashed_pwd)
        # db.session.add(user)
        # db.session.commit()
        #
        # flash(f'Account created!', 'success')
        # return redirect(url_for('login'))
    # return render_template('register.html', title='Register', form=form)
#
#
# @app.route('/login', methods=['get', 'post'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             login_user(user, remember=form.remember.data)
#             next_page = request.args.get('next')
#             return redirect(next_page) if next_page else redirect(url_for('home'))
#         else:
#             flash('Login unsuccessful please check email and password', 'danger')
#     return render_template('login.html', title='Login', form=form)
#
#
# @app.route('/account')
# @login_required
# def account():
#     return render_template('account.html', title='Account')
#
#
# @app.route('/about')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('home'))
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
