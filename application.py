"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_cors import CORS


def create_app(app_name='User'):
    app = Flask(app_name)
    app.config.from_object('userManagement.config.BaseConfig')

    cors = CORS(app, resources={r"/user/*": {"origins": "*"}})

    from userManagement.api import api, login_manager, bcrypt
    app.register_blueprint(api, url_prefix="/user")
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from stripeApi.api import server
    app.register_blueprint(server, url_prefix='/stripe')

    from fetchData.api import api
    app.register_blueprint(api, url_prefix='/fetchdata')

    from userManagement.models import db
    db.init_app(app)

    return app
