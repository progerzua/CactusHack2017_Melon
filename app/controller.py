'''
Its shitty code. Don`t use it.
'''

from flask import render_template,session,redirect,url_for,escape,request,flash,abort
from app import app, db
from datetime import datetime
from app.models import Acc, Team, Project, User, Task, association_table
from sqlalchemy.orm import sessionmaker
from flask import Flask,session, request, flash, url_for, redirect, render_template, abort
from app.forms import LoginForm
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker, scoped_session
import json

@app.route('/')
def index():
    return render_template('landing.html')


@app.route('/registration', methods=(['GET','POST']))
def registration():
    if request.method == 'POST':
        nickname = request.form['name']
        passw = request.form['pass']
        cpassw = request.form['cpass']
        email = request.form['email']
        status = request.form['status']
        now = datetime.now()
        if passw == cpassw:
            post_entry = Acc(nickname=nickname,password=passw,email=email,status=status,joined=now)
            if status == "Head":
                post_pod=Team(name=nickname,joined=now,acc=post_entry)
            else:
                post_pod=User(acc=post_entry,rating=0)
            db.session.add(post_entry)
            db.session.add(post_pod)
            db.session.commit()
            return "Registration Succesfull"
        else:
            return "Password doesnt match"
    else:
        mess = "Bad request"
        return render_template('registration.html')
        #return "Bad request"

@app.route('/login', methods=(['POST']))
def login():
    if 'ajax' in request.form:
        if 'nickname' in request.form and 'password' in request.form:
            login = request.form['nickname']
            password = request.form['password']

            acc = db.session.query(Acc).filter_by(nickname=login).first()
            if acc:
                if acc.password == password:
                    session["username"] = login
                    session["id"] = acc.id
                    session["status"] = acc.status
                    if acc.status == "Head":
                        #result = db.session.query(Team).filter_by(acc_id='1').all()
                        session["company_name"] = "Melon"
                        session["team_id"] = 2
                        return "Head"
                    else:
                        return "Slave"
                else:
                    return "Wrong password"
            else:
                return "Account doesn`t exist"



@app.route('/create_task',methods=(['GET', 'POST']))
def create_task():
    if request.method == 'POST':
        title_task = request.form['title']
        info_task = request.form['info']
        expected_task = request.form['expected_time']
        from datetime import datetime
        expected=expected_task.split('-')
        expected=datetime(int(expected[0]),int(expected[1]),int(expected[2]))
        post_entry = Task(title=title_task, info=info_task, expected=expected)
        db.session.add(post_entry)
        db.session.commit()

        return title_task + " " + info_task + " " + expected_task

    else:
        mess = "Bad request"
        return render_template('create_task.html')
        #return "Bad request"

@app.route('/create_project',methods=(['GET', 'POST']))
def create_project():
    if request.method == 'POST':
        name_project = request.form['name']
        post_entry = Project(name=name_project)
        db.session.add(post_entry)
        db.session.commit()
        return name_project

    else:
        mess = "Bad request"
        return render_template('create_project.html')
        #return "Bad request"

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('id', None)
    session.pop('status', None)
    return redirect('/')

@app.route('/hh_home')
def hh_home():
    if ('status' in session) and (session['status'] == 'Head'):
        Session = scoped_session(sessionmaker(bind=db.engine))
        s = Session()
        result = s.execute('SELECT * FROM Projects WHERE team_id = :val', {'val': session["team_id"]})
        return render_template('indexHR.html', company_name=session["company_name"], projects=result)
    else:
        return redirect('/')

@app.route('/hh/project/<projectid>')
def hh_project(projectid):
    if ('status' in session) and (session['status'] == 'Head'):
        Session = scoped_session(sessionmaker(bind=db.engine))
        s = Session()
        result = s.execute('SELECT * FROM Tasks WHERE project_id = :val', {'val': projectid})
        return render_template('indexHR_one.html', company_name=session["company_name"], tasks=result)
    else:
        return redirect('/')

@app.route('/test')
def test():
    Session = scoped_session(sessionmaker(bind=db.engine))
    s = Session()
    tmp = ""
    result = s.execute("SELECT * FROM Users")
    for i in result:
        tmp = i
    return str(tmp)
