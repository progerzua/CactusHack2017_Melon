# app.py

from flask import Flask
from app.models import Base
from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'development key'
db = SQLAlchemy(app)
Base.metadata.create_all(bind=db.engine)
from app import controller
