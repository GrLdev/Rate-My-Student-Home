from flask import Flask
from secret_keys import config_secret_key

app = Flask(__name__)
app.config['SECRET_KEY'] = config_secret_key

from app import routes