from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workshops_ptk.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
appDB = SQLAlchemy(app)
login_manager = LoginManager(app)

from application.views import index, signin

appDB.create_all()