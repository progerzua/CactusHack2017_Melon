from flask import Flask
from datetime import timedelta

app = Flask(__name__)
app.config.from_object('config')
app.permanent_session_lifetime = timedelta(hours=24)

from app import controller
