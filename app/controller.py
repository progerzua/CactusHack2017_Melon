from flask import render_template,session,redirect,url_for,escape,request,flash,abort
from app import app, db
from app.models import User, Team, Project, Branch, Task

@app.route('/')
def index():
    team = Team("teamname")
    db.session.add(team)
    project = Project("projectname", step_up = team)
    db.commit()
    return "Hello, World!"
