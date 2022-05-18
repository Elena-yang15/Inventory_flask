from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
app.config['SQLALCHEMY'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

from flaskinventory import routes
