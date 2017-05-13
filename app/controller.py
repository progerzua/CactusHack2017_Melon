'''
Its shitty code. Don`t use it.
'''

from flask import render_template,session,redirect,url_for,escape,request,flash,abort
from app import app, db
from app.models import Acc, Team, Project, User, Task, association_table
from sqlalchemy.orm import sessionmaker
from flask import Flask,session, request, flash, url_for, redirect, render_template, abort ,g

@app.route('/')
def index():
    someacc = Acc(nickname="admin")
    db.session.add(someacc)
    someteam = Team(name="testeam", acc = someacc)
    db.session.add(someteam)
    someproject = Project(name="testproject", team = someteam)
    db.session.add(someproject)
    sometask = Task(title="testask", project = someproject)
    db.session.add(sometask)
    sometask1 = Task(title="task", project = someproject)
    db.session.add(sometask)
    user = User(rating=0, acc = someacc)
    db.session.add(user)
    user.tasks.append(sometask)
    user.tasks.append(sometask1)
    db.session.add(sometask)
    db.session.commit()
    
    
    result= db.session.query(association_table).filter_by(Users_id=2).first()

    return "Base works, all good"
