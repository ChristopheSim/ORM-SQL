from role_crud import insert_role
from movie_crud import insert_movie
from link_crud import insert_link
from person_crud import insert_person

def populate():
    insert_movie("ECAM-4MIN", "365", "01/09/2018")
    insert_movie("Sushi vengeur", "2:45", "63/87/3532")

    insert_person("Mr", "Lorge", "23/73/2987", "male")
    insert_person("Mr", "Dekympe", "63/74/9836", "male")
    insert_person("Student", "A", "64/48/3947", "male")
    insert_person("Sushi", "Saumon", "23/74/9374", "female")
    insert_person("Japonais", "Pacontent", "64/84/2937", "male")

    insert_role("Acteur")
    insert_role("Realisateur")

    insert_link("1", "1", "2")
    insert_link("1", "2", "2")
    insert_link("1", "3", "1")
    insert_link("2", "4", "1")
    insert_link("3", "5", "2")

if __name__ == "__main__":
    populate()
