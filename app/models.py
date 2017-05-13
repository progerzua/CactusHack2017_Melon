# models.py
from flask import Flask, Blueprint, render_template, abort
from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, MetaData, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Team(Base):

    __tablename__ = 'Teams'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    joined = Column(DateTime)
    login = Column(String(32))
    password = Column(String(32))
    email = Column(String(128))
    info = Column(String(1000))

    projects = relationship("Project", backref="team", lazy = "dynamic")


class Project(Base):

    __tablename__ = 'Projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    team_id = Column(Integer, ForeignKey('Teams.id'))

    tasks = relationship("Task", backref="project", lazy = "dynamic")


class Task(Base):

    __tablename__ = 'Tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    created = Column(DateTime) #дата создания
    expected = Column(DateTime) #дата окончания
    info = Column(String(5000)) #информация про задание
    status = Column(Integer)
    project_id = Column(Integer, ForeignKey("Projects.id"))

    #authors = relationship("User", backref="task", lazy="dynamic")


class User(Base):

    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(32), unique=False)
    password = Column(String(32))
    email = Column(String(128), unique=False)
    joined = Column(DateTime)
    #task_id = Column(Integer, ForeignKey('Tasks.id'))
    task_id = Column(Integer)
    status = Column(String)
    rating = Column(Integer)   #!!!!!Скорость выполнения Пока так!!!!!

class TaskConnection(Base):
    '''
    To connect User and Task
    '''

    __tablename__ = 'TaskConnection'
