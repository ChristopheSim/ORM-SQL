# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Maxime Bourguignon and Christophe Simon

""" This script creates the mysql database (deprecated). """


import utils
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, ForeignKey
from sqlalchemy import Integer, String, Date
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import relationship

engine = utils.connect()

# Check the existence of database
if not database_exists(engine.url):
    create_database(engine.url)
else:
    print("The database already exists.")

# Create a metadata instance
metadata = MetaData(engine)

# Declare tables
person = Table('person', metadata,
              Column('pk_person', Integer, primary_key=True, nullable=False),
              Column('firstname', String(30)),
              Column('lastname', String(30)),
              Column('birthdate', Date, nullable=False),
              Column('gender', String(1), nullable=False))

role = Table('role', metadata,
              Column('pk_role', Integer, primary_key=True, nullable=False),
              Column('role_name', String(20), nullable=False))

movie = Table('movie', metadata,
              Column('pk_movie', Integer, primary_key=True, nullable=False),
              Column('date', Date, nullable=False),
              Column('time', Integer, nullable=False),
              Column('title', String(30), nullable=False))

link = Table('link', metadata,
              Column('pk_link', Integer, primary_key=True, nullable=False),
              Column('fk_movie', Integer, ForeignKey('movie.pk_movie'), nullable=False),
              Column('fk_person', Integer, ForeignKey('person.pk_person'), nullable=False),
              Column('fk_role', Integer, ForeignKey('role.pk_role'), nullable=False))

# Create all tables
metadata.create_all()

# Print tables for test
for _t in metadata.tables:
   print("Table: ", _t)
