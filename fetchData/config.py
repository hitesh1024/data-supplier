"""
    config.py
    - settings for the flask application object
"""


class BaseConfig(object):
    SECRET_KEY = 'MySecretKey'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flask_app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
