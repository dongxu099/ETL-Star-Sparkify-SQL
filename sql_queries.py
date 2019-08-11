# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
# FACT
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
                                songplay_id SERIAL PRIMARY KEY,
                                start_time bigint,
                                user_id varchar,
                                level varchar,
                                artist_id varchar,
                                song_id varchar,
                                session_id int,
                                location text,
                                user_agent text)""")

# DIMENTION
user_table_create = ("""CREATE TABLE IF NOT EXISTS users(
                            user_id varchar PRIMARY KEY,
                            first_name varchar, 
                            last_name varchar, 
                            gender varchar,
                            level varchar)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(
                            song_id varchar PRIMARY KEY,
                            title varchar,
                            artist_id varchar,
                            year int,
                            duration float)""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(
                              artist_id varchar PRIMARY KEY, 
                              name varchar, 
                              location varchar, 
                              latitude float, 
                              longitude float)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
                            start_time timestamp PRIMARY KEY, 
                            hour int, 
                            day int, 
                            week int, 
                            month int, 
                            year int, 
                            weekday int)""")

# INSERT RECORDS
songplay_table_insert = ("""INSERT INTO songplays(
                                start_time,
                                user_id,
                                level,
                                artist_id,
                                song_id,
                                session_id,
                                location,
                                user_agent)
                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""")

user_table_insert = ("""INSERT INTO users(
                            user_id, 
                            first_name, 
                            last_name, 
                            gender, 
                            level)
                        VALUES(%s,%s,%s,%s,%s)
                        ON CONFLICT(user_id) DO UPDATE
                        SET first_name = excluded.first_name,
                            last_name = excluded.last_name,
                            gender = excluded.gender,
                            level = excluded.level""")

song_table_insert = ("""INSERT INTO songs(
                            song_id, 
                            title, 
                            artist_id, 
                            year, 
                            duration)
                        VALUES(%s,%s,%s,%s,%s)""")

artist_table_insert = ("""INSERT INTO artists(
                              artist_id,
                              name,
                              location,
                              latitude,
                              longitude)
                           VALUES(%s,%s,%s,%s,%s)
                           ON CONFLICT (artist_id)
                           DO NOTHING""")

time_table_insert = ("""INSERT INTO time(
                              start_time,
                              hour,
                              day,
                              week,
                              month,
                              year,
                              weekday)
                           VALUES(%s,%s,%s,%s,%s,%s,%s)
                           ON CONFLICT (start_time) 
                           DO NOTHING""")

# Query the song_id and the artist_id
# title, name and duration are input parameters
song_select = ("""SELECT s.song_id, a.artist_id 
                  FROM songs AS s
                  LEFT OUTER JOIN artists AS a
                  ON s.artist_id = a.artist_id
                  WHERE s.title = %s AND a.name = %s AND s.duration = %s""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
