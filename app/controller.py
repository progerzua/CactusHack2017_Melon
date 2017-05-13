from flask import render_template,session,redirect,url_for,escape,request,flash,abort
from app import app, db
from app.models import Team, Project

@app.route('/')
def index():
    o_team = Team(name="teamname4")
    db.session.add(o_team)
    db.session.commit()
    project = Project(name="projectname", team = o_team)
    
    db.session.add(project)
    db.session.commit()
    #db.commit()
    return "Hello, World!"
