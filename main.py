# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Maxime Bourguignon and Christophe Simon

import os
import utils
from role_crud import search_role, insert_role, update_role, delete_role
from movie_crud import search_movie, insert_movie, update_movie, delete_movie
from link_crud import search_link, insert_link, update_link, delete_link
from person_crud import search_person, insert_person, update_person, delete_person
from fill_db import populate
import datetime

help = """Please select what you would like to do:
    - create: to create the database;
    - movies: to display all movies;
    - link: to search a link;
    - roles: to display all roles;
    - movie: to search a movie with the name;
    - person: to search a person with firstname and lastname;
    - drop: to drop the database;
    - fill: populate the db with examples;
    - help: show the help menu;
    - quit: quit the application;
    """

title = """-------------------------------------------------
Welcome to your movies database
-------------------------------------------------
\n"""

state = True

menu_crud ="""Please select what you would like to do:
    - create: to create;
    - read: to show;
    - update: to update;
    - delete: to delete;
    """

def init():
    os.system('clear')
    print(title)
    print(help)

def ask():
    print("input string >>> ", end='')
    stdin = input()
    return stdin

def execute(stdin):
    global state

    if stdin == "create":
        # create the database
        print("create database...")
        try:
            os.system('python3 create_db.py')
        except:
            print("Please run manually the file create_db.py")
            execute("quit")
    elif stdin == "movies":
        # search movies
        print("Menu movies")
        links = search_link()
        print(links)
        for l in links:
            l.fk_movie = search_movie(pk_movie=l.fk_movie)
            l.fk_person = search_person(pk_person=l.fk_person)
            l.fk_role = search_role(pk_role=l.fk_role)
        print(links)
        for l in links:
            print((l.fk_movie.title, l.fk_person.firstname, l.fk_person.lastname, l.fk_role.name))
    elif stdin == "link":
        # search links
        print("Menu link")
        print(menu_crud)
        stdin = ask()
        if stdin == "create":
            print("create")
            fk_movie = input("fk_movie :")
            fk_person = input("fk_person :")
            fk_role = input("fk_role :")
            insert_link(fk_movie, fk_person, fk_role)
        elif stdin == "read":
            print("read")
            fk_movie = input("fk_movie :")
            fk_person = input("fk_person :")
            fk_role = input("fk_role :")
            print(search_link(fk_movie=fk_movie, fk_person=fk_person, fk_role=fk_role))
        elif stdin == "update":
            print("update")
            pk_role = input("pk_role :")
            fk_movie = input("fk_movie :")
            fk_person = input("fk_person :")
            fk_role = input("fk_role :")
            print(update_link(pk_role, fk_movie, fk_person, fk_role))
        elif stdin == "delete":
            print("delete")
            pk_role = input("pk_role :")
            delete_link(pk_role)

    elif stdin == "roles":
        # search roles
        try:
            print("Menu roles")
            print(menu_crud)
            stdin = ask()
            if stdin == "create":
                print("create")
                name = input("name :")
                insert_role(name)
            elif stdin == "read":
                print("read")
                name = input("name :")
                print(search_role(name=name))
            elif stdin == "update":
                print("update")
                pk_role = input("pk_role :")
                name = input("name :")
                print(update_role(pk_role, name))
            elif stdin == "delete":
                print("delete")
                pk_role = input("pk_role :")
                delete_role(pk_role)
        except:
            print("EROOR: no role in the database.")

    elif stdin == "movie":
        # search one movie
        print("search movie ...")
        print(menu_crud)
        stdin = ask()
        if stdin == "create":
            print("create")
            title = input("title :")
            duration = input("duration :")
            day = int(input("day (1 or 2 number(s)) :"))
            month = int(input("month (1 or 2 number(s)) :"))
            year = int(input("year (4 numbers) :"))
            date = datetime.date(year, month, day)
            insert_movie(title, duration, date)
        elif stdin == "read":
            print("read")
            title = input("title :")
            duration = input("duration :")
            date = input("date :")
            print(search_movie(title=title, duration=duration, date=date))
        elif stdin == "update":
            print("update")
            pk_movie = input("pk_movie :")
            title = input("title :")
            duration = input("duration :")
            day = int(input("day (1 or 2 number(s)) :"))
            month = int(input("month (1 or 2 number(s)) :"))
            year = int(input("year (4 numbers) :"))
            date = datetime.date(year, month, day)
            print(update_movie(pk_movie, title, duration, date))
        elif stdin == "delete":
            print("delete")
            pk_movie = input("pk_movie :")
            delete_movie(pk_movie)

    elif stdin == "person":
        # search person
        print("search person ...")
        print(menu_crud)
        stdin = ask()
        if stdin == "create":
            print("create")
            firstname = input("firstname :")
            lastname = input("lastname :")
            day = int(input("day (1 or 2 number(s)) :"))
            month = int(input("month (1 or 2 number(s)) :"))
            year = int(input("year (4 numbers) :"))
            birthdate = datetime.date(year, month, day)
            gender = input("gender (M/F) :")
            insert_person(firstname, lastname, birthdate, gender)
        elif stdin == "read":
            print("read")
            firstname = input("firtsname :")
            lastname = input("lastname :")
            birthdate = input("birthdate :")
            gender = input("gender (M/F) :")
            print(search_person(firstname=firstname, lastname=lastname, birthdate=birthdate, gender=gender))
        elif stdin == "update":
            print("update")
            pk_person = input("pk_person :")
            firstname = input("firstname :")
            lastname = input("lastname :")
            day = int(input("day (1 or 2 number(s)) :"))
            month = int(input("month (1 or 2 number(s)) :"))
            year = int(input("year (4 numbers) :"))
            birthdate = datetime.date(year, month, day)
            gender = input("gender (M/F) :")
            print(update_person(pk_person, firstname, lastname, birthdate, gender))
        elif stdin == "delete":
            print("delete")
            pk_person = input("pk_person :")
            delete_person(pk_person)

    elif stdin == "fill":
        # test the db
        print("test database ...")
        populate()
    elif stdin == "drop":
        # drop he database
        print("drop database ...")
        utils.drop_db()
    elif stdin == "help":
        # print help
        print(help)
    elif stdin == "quit":
        # quit
        print("quit")
        state = False
    else:
        # ERROR
        print("incorrect input")


if __name__ == "__main__":
    init()
    while state:
        stdin = ask()
        execute(stdin)
    quit()
