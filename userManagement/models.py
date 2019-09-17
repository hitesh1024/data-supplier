"""
models.py
- Data classes for the surveyapi application
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# from flask_bcrypt import check_password_hash, generate_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # @classmethod
    # def authenticate(cls, **kwargs):
    #     email = kwargs.get('email')
    #     password = kwargs.get('password')
    #
    #     if not email or not password:
    #         return None
    #
    #     user = cls.query.filter_by(email=email).first()
    #     if not user or not check_password_hash(user.password, password):
    #         return None
    #
    #     return user
    #
    # def to_dict(self):
    #     return dict(id=self.id, email=self.email)
    #
    # def __init__(self, username, email, password):
    #     self.username = username
    #     self.email = email
    #     self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return f'User({self.username}, {self.email})'


class RegestrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
                             validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign up')

    def validate_username(self, username):
        print('inside username validator\n')
        # from application import User
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken please chose another one')

    def validate_email(self, email):
        print("inside email validator\n")
        # from application import User
        email = User.query.filter_by(email=email.data).first()
        if email:
                raise ValidationError('Email already regestered')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
                             validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')
