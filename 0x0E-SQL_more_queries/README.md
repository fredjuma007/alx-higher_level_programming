0x0E. SQL - More queries

Tasks
0. My privileges!
mandatory

Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
1. Root user
mandatory

Write a script that creates the MySQL server user user_0d_1.
2. Read user
mandatory

Write a script that creates the database hbtn_0d_2 and the user user_0d_2.

    user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
    The user_0d_2 password should be set to user_0d_2_pwd
    If the database hbtn_0d_2 already exists, your script should not fail
    If the user user_0d_2 already exists, your script should not fail

3. Always a name
mandatory

Write a script that creates the table force_name on your MySQL server.
4. ID can't be null
mandatory

Write a script that creates the table id_not_null on your MySQL server.

5. Unique ID
mandatory

Write a script that creates the table unique_id on your MySQL server.
6. States table
mandatory

Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
7. Cities table
mandatory

Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
8. Cities of California
mandatory

Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
9. Cities by States
mandatory

Write a script that lists all cities contained in the database hbtn_0d_usa.

10. Genre ID by show
mandatory

Import the database dump from hbtn_0d_tvshows to your MySQL server: download

Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
11. Genre ID for all shows
mandatory

Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)

Write a script that lists all shows contained in the database hbtn_0d_tvshows.
12. No genre
mandatory

Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql)

Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
13. Number of shows by genre
mandatory

Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)

Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
14. My genres
mandatory

Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 13-count_shows_by_genre.sql)

Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
15. Only Comedy

Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 14-my_genres.sql)

Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
16. List shows and genres

Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql)

Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
