from movie_crud import insert_movie, search_movie, update_movie, delete_movie
from datetime import date

insert_movie('Test1', 120, date(2018, 12, 13))
search_movie('Test1', 120, date(2018, 12, 13))
update_movie(1, 'Test1_updated', 120, date(2018, 12, 15))
delete_movie(3)
