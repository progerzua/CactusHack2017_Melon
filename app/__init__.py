# app.py

from flask import Flask
from app.models import Base
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
Base.metadata.create_all(bind=db.engine)
login_manager = LoginManager()
login_manager.setup_app(app)

from app import controller
