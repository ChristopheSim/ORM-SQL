# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Maxime Bourguignon and Christophe Simon

""" This script contains the function to create the database. """

from utils import connect
from sqlalchemy import Column, ForeignKey, inspect
from sqlalchemy import Integer, String, Date
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base



try:
    Base = declarative_base()
    engine = connect()

    # Declare tables (classes)
    class Person(Base):
        __tablename__ = 'person'

        pk_person = Column(Integer, primary_key=True, nullable=False,
        autoincrement=True)
        firstname = Column(String(30))
        lastname = Column(String(30))
        birthdate = Column(Date, nullable=False)
        gender = Column(String(1), nullable=False)
        links = relationship("Link", back_populates="person")


    class Role(Base):
        __tablename__ = 'role'

        pk_role = Column(Integer, primary_key=True, nullable=False,
        autoincrement=True)
        name = Column(String(20), nullable=False)
        links = relationship("Link", back_populates="role")


    class Movie(Base):
        __tablename__ = 'movie'

        pk_movie = Column(Integer, primary_key=True, nullable=False,
        autoincrement=True)
        date = Column(Date, nullable=False)
        duration = Column(Integer, nullable=False, autoincrement=False)
        title = Column(String(30), nullable=False)
        links = relationship("Link", back_populates="movie")


    class Link(Base):
        __tablename__ = 'link'

        pk_link = Column(Integer, primary_key=True, nullable=False,
        autoincrement=True)
        fk_movie = Column(Integer, ForeignKey('movie.pk_movie'),
        nullable=False, autoincrement=False)
        fk_person = Column(Integer, ForeignKey('person.pk_person'),
        nullable=False, autoincrement=False)
        fk_role = Column(Integer, ForeignKey('role.pk_role'),
        nullable=False, autoincrement=False)
        movie = relationship("Movie", back_populates="links")
        role = relationship("Role", back_populates="links")
        person = relationship("Person", back_populates="links")

    # Check the existence of database
    if not database_exists(engine.url):
        create_database(engine.url)

        Base.metadata.create_all(bind=engine)

        # check table exists
        ins = inspect(engine)
        for _t in ins.get_table_names():
            print(_t)
        if ins.get_table_names() != None:
            print("The database was successfully created.")
        else:
            print("The database was not successfully created.")
    else:
        print("The database already exists.")
except:
    print("ERROR: the database was not successfully created.")
