'''
Its shitty code. Don`t use it.
'''

from flask import render_template,session,redirect,url_for,escape,request,flash,abort
from app import app, db
from app.models import Team, Project, User, Task
from sqlalchemy.orm import sessionmaker
from flask import Flask,session, request, flash, url_for, redirect, render_template, abort
from app.forms import LoginForm

@app.route('/')
def index():
    # someteam = Team(name="testeam")
    # db.session.add(someteam)
    # someproject = Project(name="testproject", team = someteam)
    # db.session.add(someproject)
    # sometask = Task(title="testask", project = someproject)
    # db.session.add(sometask)
    # user = User(nickname="testuser", task = sometask)
    # db.session.add(user)
    # db.session.commit()
    return "Hello, World!"

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
