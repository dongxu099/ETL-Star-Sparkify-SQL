The purpose of this relational database is to process the company's data being saved in some JSON files into SQL tables that can be further analyzed. 

1. The analytical goals

* Analyze the user's daily activities and
* Provide future song recommendations to users

2. Database schema design

I created a STAR schema, optimized for song play analysis. One fact table and four dimension tables are created as follows：

* Fact Table: songplays with attributes referencing to the dimension tables
* Dimension Tables: users, songs, artists and time table

3. The ETL pipeline:

I defined the following three functions to operationalize the entire ETL pipeline:

* a function to process a single file in the song_data and obtain the songs and artists tables
* a function to process a single file in the log_data and obtain the dimension tables of users and time, and the fact table of songplays
* a function to iterate through all files of the song_data and the log_data so that the first two functions can process information for the entire databases

Some special treatments and transformation to the data are detailed as follows:

* artist and songs tables are extracted from the song_data files.
* time, users are extracted from the log_data files.
* songplay table are extracted from both files, since it got the song ID and artist ID by querying the songs and artists tables to find matches based on song title, artist name, and song duration time.
* songplays table only consider records with NextSong action.
* users table will update the level value when it sees an new level value.
