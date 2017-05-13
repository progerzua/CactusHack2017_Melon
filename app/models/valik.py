# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:44:08 2017

@author: Easy1_000
"""
from flask import Flask, Blueprint, render_template, abort
#from flask import 
from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, MetaData, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import 
#from sql3 import 

#!
#engine = create_engine('sqlite:///:memory:', echo=True)
#!
#step_up child -> parent
#step_down parent -> child

Base = declarative_base()
class Team(Base):
    __tablename__ = 'Teams'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    step_down = relationship("Projects", back_populates="step_up")
    def __init__(self, id, name):
        self.id = id
        self.name = name
 #   def __repr__(self):

class Project(Base):
    __tablename__ = 'Projects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    team_id = Column(Integer, ForeignKey('Teams.id'))
    step_up = relationship("Teams", back_populates="step_down")
    step_down1 = relationship("Branches", back_populates="step_up")
    step_down2 = relationship("Users", back_populates="step_up")
    def __init__(self, id, name):
        self.id = id
        self.name = name
 #   def __repr__(self):
     
class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    password = Column(String)
    email = Column(String)
    joined = Column(DataTime)
    project_id = Column(Integer, ForeignKey('Projects.id'))
    status = Column(String)
    rating = Column(Integer)
    step_up = relationship("Projects", back_populates="step_down2")
    step_down = relationship("Tasks", back_populates="step_up2")
    def __init__(self, id, name):
        self.id = id
        self.name = name
 #   def __repr__(self):
     
class Branch(Base):
    __tablename__ = 'Branches'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    project_id = Column(Integer, ForeignKey("Projects.id"))
    created = Column(DateTime)
    status = Column(Integer)
    price_all = Column(Integer)
    step_up = relationship("Projects", back_populates="step_down1")
    step_down = relationship("Tasks", back_populates="step_up1")
    def __init__(self, id, name, project_id, created, status, price_all):
        self.id = id
        self.name = name
        self.project_id = project_id
        self.created = created
        self.status = status
        self.price_all = price_all
 #   def __repr__(self):
 #       return "<Branch('%s','%s', '%s', '%s')>" % (self.name, self.created, self.status, self.price_all)
class Task(Base):
    __tablename__ = 'Tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    created = Column(DateTime)
    modified = Column(DateTime)
    author_id = Column(Integer, ForeignKey("Users.id"))
    executor_id = Column(Integer)
    tags = Column(String)
    status = Column(Integer)
    price = Column(Integer)
    branch_id = Column(Integer, ForeignKey("Branches.id"))
    step_up1 = relationship("Branches", back_populates="step_down")
    step_up2 = relationship("Users", back_populates="step_down")
    def __init__(self, id, title, created, modified, author_id, executor_id, tags, status, price, branch_id):
        self.id = id
        self.title = title
        self.created = created
        self.modified = modified
        self.author_id = author_id
        self.executor_id = executor_id
        self.tags = tags
        self.status = status
        self.price = price
        self.branch_id = branch_id
   # def __repr__(self):
   #     return "<Task('%s','%s', '%s', '%s', '%s')>" % (self.title, self.created, self.modified, self.tags)
#class File(Base):
#    __tablename__ = 'Files'
#    id = Column(Integer, primary_key=True)
#    name = Column(String)
#    created = Column(DateTime)
#    descriprtion = Column(String)
#    author_id = Column(Integer)
#    path = Column(String)
#    task_id = Column(Integer)
#    def __init__(self, id, name, created, description, author_id, path, task_id):
#        self.id = id
#        self.name = name
#        self.created = created
#        self.description = description
#        self.author_id = author_id 
#        self.path = path
#        self.task_id = task_id
   # def __repr__(self):
   #     return "<Task('%s','%s', '%s', '%s', '%s')>" % (self.title, self.created, self.modified, self.tags)


