# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Maxime Bourguignon and Christophe Simon

""" This script creates the mysql database. """



from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, ForeignKey, inspect
from sqlalchemy import Integer, String, Date
from utils import get
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import relationship, mapper
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

username = get("db", "login")
password = get("db", "password")
port = get("db", "port")
database = get("db", "name")
url = get("db", "url")

engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(username,
                                                        password,
                                                        url,
                                                        port,
                                                        database),
                       echo=True)

# Check the existence of database
if not database_exists(engine.url):
    create_database(engine.url)
else:
    print("The database already exists.")

# Declare tables
class Person(Base):
    __tablename__ = 'person'

    pk_person = Column(Integer, primary_key=True, nullable=False)
    firstname = Column(String(30))
    lastnamename = Column(String(30))
    birthdate = Column(Date, nullable=False)
    gender = Column(String(1), nullable=False)
    links = relationship("Link", back_populates="person")


class Role(Base):
    __tablename__ = 'role'

    pk_role = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(20), nullable=False)
    links = relationship("Link", back_populates="role")

class Movie(Base):
    __tablename__ = 'movie'

    pk_movie = Column(Integer, primary_key=True, nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Integer, nullable=False)
    title = Column(String(30), nullable=False)
    links = relationship("Link", back_populates="movie")


class Link(Base):
    __tablename__ = 'link'

    pk_link = Column(Integer, primary_key=True, nullable=False)
    fk_movie = Column(Integer, ForeignKey('movie.pk_movie'), nullable=False)
    fk_person = Column(Integer, ForeignKey('person.pk_person'), nullable=False)
    fk_role = Column(Integer, ForeignKey('role.pk_role'), nullable=False)
    movie = relationship("Movie", back_populates="links")
    role = relationship("Role", back_populates="links")
    person = relationship("Person", back_populates="links")

Base.metadata.create_all(bind=engine)

# check table exists
ins = inspect(engine)
for _t in ins.get_table_names():
    print(_t)
