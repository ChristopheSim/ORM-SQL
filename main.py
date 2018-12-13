import os

os.system('clear')
print("""
-------------------------------------------------
Welcome to your movies database
-------------------------------------------------
\n
Please select what you would like to do:
    - movies: to display all movies;
    - roles: to display all roles;
    - movie: to search a movie with the name;
    - person: to search a person with firstname and lastname;
""")

inputString = input()
print("your input string is", inputString)
