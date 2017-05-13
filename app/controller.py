from flask import render_template,session,redirect,url_for,escape,request,flash,abort
from app import app, db
from app.models import Team, Project, User
from sqlalchemy.orm import sessionmaker
from flask import Flask,session, request, flash, url_for, redirect, render_template, abort ,g
from flask.ext.login import login_user , logout_user , current_user , login_required
@app.route('/')
def index():
    o_team = Team(name="teamname18")
    db.session.add(o_team)
    project = Project(name="projectname", team = o_team)
    db.session.add(project)
    user = User(nickname="admin9", password="admin",project = project)
    db.session.add(user)
    db.session.commit()

    if request.method == 'GET':
        return render_template('layout.html')
    


 
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    nickname = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(nickname=nickname,password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))
#@app.route("/logout")
#@login_required
#def logout():
#    logout_user()
#    return redirect(somewhere)