# app.py

from flask import Flask
from app.models import Base
from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
Base.metadata.create_all(bind=db.engine)

from app import controller
