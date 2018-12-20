# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Maxime Bourguignon and Christophe Simon

import os

help = """Please select what you would like to do:
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
    # We can do swith case
    if stdin == "movies":
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
