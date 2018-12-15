from person_crud import insert_person, search_person
from datetime import date

insert_person("firstname", "lastname", date(2018, 12, 13), "M")
search_person("firstname", "lastname", date(2018, 12, 13), "M")
