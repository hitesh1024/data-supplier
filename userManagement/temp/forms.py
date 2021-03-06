# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField, BooleanField
# from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
#
#
# class RegestrationForm(FlaskForm):
#     username = StringField('Username',
#                            validators=[DataRequired(), Length(min=2, max=20)])
#
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#
#     password = PasswordField('Password',
#                              validators=[DataRequired()])
#
#     confirm_password = PasswordField('Confirm Password',
#                                      validators=[DataRequired(), EqualTo('password')])
#
#     submit = SubmitField('Sign up')
#
#     def validate_username(self, username):
#         print('inside username validator\n')
#         from application import User
#         user = User.query.filter_by(username=username.data).first()
#         if user:
#             raise ValidationError('Username is taken please chose another one')
#
#     def validate_email(self, email):
#         print("inside email validator\n")
#         from application import User
#         email = User.query.filter_by(email=email.data).first()
#         if email:
#             raise ValidationError('Email already regestered')
#
#
# class LoginForm(FlaskForm):
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#
#     password = PasswordField('Password',
#                              validators=[DataRequired()])
#
#     remember = BooleanField('Remember Me')
#
#     submit = SubmitField('Login')
