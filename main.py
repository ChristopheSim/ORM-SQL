# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors: Maxime Bourguignon and Christophe Simon

import os
import utils
from role_crud import search_role, insert_role, update_role, delete_role
from movie_crud import search_movie, insert_movie, update_movie, delete_movie
from link_crud import search_link, insert_link, update_link, delete_link
from person_crud import search_person, insert_person, update_person, delete_person


help = """Please select what you would like to do:
    - create: to create the database;
    - movies: to display all movies;
    - roles: to display all roles;
    - movie: to search a movie with the name;
    - person: to search a person with firstname and lastname;
    - drop: to drop the database;
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
        for l in links:
            l[0] = search_movie(fk_movie=l[0])
            l[1] = search_person(fk_person=l[1])
            l[2] = search_role(fk_role=l[2])
        print(links)
    elif stdin == "roles":
        # search roles
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

    elif stdin == "movie":
        # search one movie
        print("search movie ...")
        print(menu_crud)
        stdin = ask()
        if stdin == "create":
            print("create")
            title = input("title :")
            duration = input("duration :")
            date = input("date :")
            insert_movie(title, duration, date)
        elif stdin == "read":
            print("read")
            title = input("title :")
            date = input("date :")
            print(search_movie(title=title, date=date))
        elif stdin == "update":
            print("update")
            pk_movie = input("pk_movie :")
            title = input("title :")
            duration = input("duration :")
            date = input("date :")
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
            birthdate = input("birthdate :")
            gender = input("gender :")
            insert_role(title, duration, birthdate, gender)
        elif stdin == "read":
            print("read")
            firstname = input("firtsname :")
            lastname = input("lastname :")
            birthdate = input("birthdate :")
            gender = input("gender :")
            print(search_role(firstname=firstname, lastname=lastname, birthdate=birthdate, gender=gender))
        elif stdin == "update":
            print("update")
            pk_person = input("pk_person :")
            firstname = input("firstname :")
            lastname = input("lastname :")
            birthdate = input("birthdate :")
            gender = input("gendpk_movieer :")
            print(update_role(pk_person, firstname, lastname, birthdate, gender))
        elif stdin == "delete":
            print("delete")
            pk_person = input("pk_person :")
            delete_role(pk_person)

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
