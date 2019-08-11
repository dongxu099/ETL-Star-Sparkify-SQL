1. Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

The purpose of this database is to process the data within the JSON files into a form of tables that can be further analyzed by the company, Sparkify. The analytical goals of Sparkify are 1) analyze the user's daily activities and 2) provide future song recommendations to users.

2. State and justify your database schema design and ETL pipeline.

I created a STAR schema, optimized for song play analysis. One fact table and four dimension tables are created.
* Fact Table: songplays: attributes referencing to the dimension tables.
* Dimension Tables: users, songs, artists and time table.
For ETL pipeline, I defined the following functions
* a function to process a single file in the song_data and obtain the songs and artists tables
* a function to process a single file in the log_data and obtain the users and time dimension tables and the songplays fact table
* a function to iterate through all files of the song_data and the log_data so that the first two functions can process information for the entire databases.
