# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Maxime Bourguignon and Christophe Simon

import os
import utils


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

def init():
    os.system('clear')
    print(title)
    print(help)

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
        print("search movies ...")
    elif stdin == "roles":
        # search roles
        print("search roles...")
    elif stdin == "movie":
        # search one movie
        print("search movie ...")
    elif stdin == "person":
        # search person
        print("search person ...")
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
        print("input string >>> ", end='')
        stdin = input()
        execute(stdin)
    quit()
