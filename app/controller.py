'''
Its shitty code. Don`t use it.
'''

from flask import render_template,session,redirect,url_for,escape,request,flash,abort
from app import app, db
from app.models import Team, Project, User, Task
from sqlalchemy.orm import sessionmaker
from flask import Flask,session, request, flash, url_for, redirect, render_template, abort ,g

@app.route('/')
def index():
    team = Team(name="testeam")
    db.session.add(team)
    project = Project(name="testproject", Team = team)
    db.session.add(project)
    task = Task(title="testask", Project = project)
    db.session.add(task)
    user = User(nickname="testuser", Task = task)
    db.session.add(user)
    db.session.commit()
    #db.commit()
    return "Hello, World!"
