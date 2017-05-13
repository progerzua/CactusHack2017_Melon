# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:44:08 2017

@author: Easy1_000
"""
from flask import Flask, Blueprint, render_template, abort
#from flask import 
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import 
import sql3
#from sql3 import 

#!
engine = create_engine('sqlite:///:memory:', echo=True)
#!
metadata = MetaData()
branch_table = Table('Branch', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('created', DateTime)
    Column('price_all', Integer)
    Column('project_id', Integer)   
)
tasks_table = Table('Tasks', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('created', DateTime)
    Column('mofified', DateTime)
    Column('text', String),
    Column('author_id', Integer)
    Column('executor_id', Integer )
    Column('tags', String)
    Column('price', Integer)
    Column('branch_id', Integer)   
)
Files_table = Table('Files', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('created', DateTime)
    Column('Description', String),
    Column('task_id', Integer)
)
