from person_crud import insert_person, search_person, update_person
from person_crud import delete_person
from datetime import date

insert_person("firstname", "lastname", date(2018, 12, 13), "M")
search_person("firstname", "lastname", date(2018, 12, 13), "M")
#update_person(1, "firstname", "lastname", date(2018, 12, 15), "M")
#delete_person(4)
