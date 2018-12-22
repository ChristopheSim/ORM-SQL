# ORM-SQL
This project was created by Maxime Bourguignon and Christophe Simon.
Tha aim is to manage a database of movies. This file contains all the usefull informations about the application, the sources and how to run it.


## Sources
- Language: Python 3 ;
- Encoding: UTF-8 ;
- ORM: SQLAlchemy ;
- Doc: https://docs.sqlalchemy.org/en/latest/orm/tutorial.html.


## Installed packages
- python3-mysqldb ;
- sqlalchemy ;
- yaml.


## To Do
- To create the database (at least 2 tables) ;
- To create an app which use the created database.


## Informations about the application
Several files:
- 'config.yaml': useful informations to configure the app ;
- 'create_db.py': to create the database ;
- 'fill_db.py': to fill the database (example) ;
- 'link_crud.py': all the CRUD* functions for the link table ;
- 'movie_crud.py': all the CRUD* functions for the movie table ;
- 'person_crud.py': all the CRUD* functions for the person table ;
- 'role_crud.py': all the CRUD* functions for the role table ;
- 'utils.py': useful functions ;
- 'main.py': the main file of the application.

CRUD: Create, Reed, Update and Delete

This application can manage the movies database. There is a list of the available functions:
- To insert a link, a movie, a person or a role ;
- To search a link, a movie, a person or a role ;
- To display all links, movies, persons or roles ;
- To update a link, a movie, a person or a role ;
- To delete a link, a movie, a person or a role.


## Informations about the database
In the 'Document' repository, you can find the database diagram.


## How to run the application
1. To complete the 'config.yaml' file with the required informations ;
2. Operating system:
  - Linux: Nothing to do ;
  - Windows: in the 'main.py' file, replace "os.system('python3 create_db.py')" by "os.system('python create_db.py')" or to run the create_db.py file.
3. To run the 'main.py' file.
