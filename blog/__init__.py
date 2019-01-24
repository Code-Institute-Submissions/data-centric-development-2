from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from blog.config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

"""
Bcrypt is being used to generate user passwords and encrypt
them in the database for sercurity.

"""

bcrypt = Bcrypt(app)

"""
below is the instance for the login manager and
login required

"""

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'warning'

"""
below is the route import from blog the reason its below the 
code above is so that the app will aviod circular imports that
will through errors when trying to run the app.

Now the app has been made into blueprints the routes have changed
below

"""

from blog.users.routes import users
from blog.posts.routes import posts
from blog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)