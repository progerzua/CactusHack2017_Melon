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

@app.route('/login', methods=(['POST']))
def login():
    form = LoginForm()
    # if request.method == "GET":
    #     return render_template('login.html',form = form)
    # else:
    #     mess = ""
    #     if form.validate_on_submit():
    #         user = db.session.query(User).filter_by(nickname=form.login.data).first()
    #         if user:
    #             if user.password == form.password.data:
    #                 return redirect(url_for('index'))
    #             else :
    #                 mess = "Wrong password"
    #         else :
    #             mess = "User doesn`t exist"
    #     else:
    #         mess = "Validation error"
    #     return render_template('login.html',form = form, message = mess)

#GET, RABOTAET
#@app.route('/create_task',methods=(['GET', 'POST']))
#def create_task():
#    if request.method == 'GET':
#        title_task = request.args.get('title')
#        info_task = request.args.get('info')
#        expected_task = request.args.get('expected_time')
#        post_entry = Task(title=title_task, info=info_task)
#        db.session.add(post_entry)
#        db.session.commit()
#        #db.session.query(Task).append(title=title_task)
#        #db.session.query(Task).append(info=info_task)
#        #db.session.query(Task).append(expected=expected_task)
#        #for i in session.query(Task):
#        #   query.append((i.title, i.info, i.expected))
#        #return redirect(url_for('index.html'))
#        return title_task + " " + info_task + " " + expected_task
#        #db.session.query(Task).append(title=title_task)
#        #db.session.query(Task).append(info=info_task)
#        #db.session.query(Task).append(expected=expected_task)
#        return title_task + " " + info_task + " " + expected_task
#    else:
#        mess = "Bad request"
#        return render_template('create_task.html')
#        #return "Bad request"

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
        #db.session.query(Task).append(title=title_task)
        #db.session.query(Task).append(info=info_task)
        #db.session.query(Task).append(expected=expected_task)
        #for i in session.query(Task):
        #   query.append((i.title, i.info, i.expected))
        #return redirect(url_for('index.html'))
        return title_task + " " + info_task + " " + expected_task
        #return title_task
        #db.session.query(Task).append(title=title_task)
        #db.session.query(Task).append(info=info_task)
        #db.session.query(Task).append(expected=expected_task)
    else:
        mess = "Bad request"
        return "Bad request"
        #return "Bad request"
@app.route('/create_project',methods=(['GET', 'POST']))
def create_project():
    if request.method == 'POST':
        name_project = request.form['name']
        post_entry = Project(name=name_project)
        db.session.add(post_entry)
        db.session.commit()
        #db.session.query(Task).append(title=title_task)
        #db.session.query(Task).append(info=info_task)
        #db.session.query(Task).append(expected=expected_task)
        #for i in session.query(Task):
        #   query.append((i.title, i.info, i.expected))
        #return redirect(url_for('index.html'))
        return name_project
        #return title_task
        #db.session.query(Task).append(title=title_task)
        #db.session.query(Task).append(info=info_task)
        #db.session.query(Task).append(expected=expected_task)
    else:
        mess = "Bad request"
        return render_template('create_project.html')
        #return "Bad request"
