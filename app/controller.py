'''
Its shitty code. Don`t use it.
'''

from flask import render_template,session,redirect,url_for,escape,request,flash,abort
from app import app, db
from app.models import Acc, Team, Project, User, Task, association_table
from sqlalchemy.orm import sessionmaker
from flask import Flask,session, request, flash, url_for, redirect, render_template, abort
from app.forms import LoginForm

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/login', methods=(['GET', 'POST']))
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template('login.html',form = form)
    else:
        mess = ""
        if form.validate_on_submit():
            user = db.session.query(User).filter_by(nickname=form.login.data).first()
            if user:
                if user.password == form.password.data:
                    return redirect(url_for('index'))
                else :
                    mess = "Wrong password"
            else :
                mess = "User doesn`t exist"
        else:
            mess = "Validation error"
        return render_template('login.html',form = form, message = mess)
