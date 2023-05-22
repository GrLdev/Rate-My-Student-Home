from flask import Flask
from secret_keys import config_secret_key

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = config_secret_key

# database
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

from app import routes, models