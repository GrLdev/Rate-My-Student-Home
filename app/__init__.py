from flask import Flask
from secret_keys import config_secret_key
from flask_login import LoginManager

# app
app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = config_secret_key

# database (used SingletonThreadPool to handle concurrent requests to the database in update_review_rent())
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.pool import SingletonThreadPool

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], poolclass=SingletonThreadPool)

db = SQLAlchemy(app, engine_options={'pool_pre_ping': True})

# login manager
login_manager = LoginManager()
login_manager.init_app(app)

from app import routes, models