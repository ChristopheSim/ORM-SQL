from movie_crud import insert_movie, search_movie
from datetime import date

insert_movie('Test1', 120, date(2018, 12, 13))
search_movie('Test1', 120, date(2018, 12, 13))
