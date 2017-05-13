from flask import render_template,session,redirect,url_for,escape,request,flash,abort
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
