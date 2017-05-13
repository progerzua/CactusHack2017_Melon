from flask import render_template,session,redirect,url_for,escape,request,flash,abort
from app import app, db

@app.route('/')
def index():
    return "Hello, World!"
