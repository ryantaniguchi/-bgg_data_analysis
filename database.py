# Import the sqlite3 database library
import sqlite3
# Import data analysis library
import pandas as pd
# Import csv-management library
import csv

# Class that manages database operations
class Database():
    def __init__(self):
        # Create sqlite database and cursor
        self.conn = sqlite3.connect('games.db')
        self.cur = self.conn.cursor()

    # Imports data from a csv file
    def import_csv(self):
        # Requests the user provide the name of a .csv file.
        csv_name = input("Please enter the name of the file you are importing from, not including the extension: ")
        
        # Opens and reads the .csv file information
        with open(csv_name + ".csv", "r") as fin:
            dr = csv.DictReader(fin)
            csv_info = [(i['BGGId'], i['Name'], i['AvgRating'], i['NumUserRatings']) for i in dr]

        # Create the Favorite_games table if it doesn't already exist
        self.cur.execute('create table if not exists Favorite_games(BGGId int, Name varchar2(255), AvgRating float, NumUserRatings int);')

        # Insert data into table
        self.cur.executemany(
            "insert into Favorite_games (BGGId, Name, AvgRating, NumUserRatings) VALUES (?, ?, ?, ?);", csv_info)

        # Show the table that has been created
        self.display_table()

    # Exports table to csv file.
    def export_table(self):
        # Requests the user provide the name of a .csv file.
        csv_name = input("Please choose a .csv filename, not including the extension: ")
        # Converts the table to a Pandas dataframe
        db_df = pd.read_sql_query("SELECT * FROM Favorite_games", self.conn)
        # Converts the dataframe to a .csv file
        db_df.to_csv(csv_name + '.csv', index=False)

    # Function to display the table.
    def display_table(self):
        try:
            # Count how many rows are in the table
            self.cur.execute('select count(*) from Favorite_games;')
            number_of_rows = self.cur.fetchone()[0]

            # Select all the data from the table so it can be printed in order of month
            self.cur.execute('select * from Favorite_games order by BGGId;')

            # Print the table
            for i in self.cur.fetchall():
                print(i)

            # Return the total number of ratings that have been given for the games in the table.
            self.cur.execute('select SUM(NumUserRatings) from Favorite_games;')
            number_of_ratings = self.cur.fetchone()[0]

            # Commit work
            self.conn.commit()

            # Print the number of rows in the table.
            print("There are", number_of_rows, "games in this table.")
            # Prints the total number of ratings in the table
            print("There are", number_of_ratings, "individual ratings for these games.")

        # Returns an error if the table has not been created.
        except Exception as error:
            print("\nUnable to locate table. Please add an entry to create the table.")

    # Function to delete the specified row.
    def delete_row(self):
        try:
            # Query to delete any rows that match te BGGID
            BGGId = input("Please enter the BGGId of the game being deleted: ")
            sql_update_query  = """DELETE from Favorite_games where BGGId=?"""
            self.cur.execute(sql_update_query, (BGGId,))
            print("Specified game has been deleted.")

            # Display the table row by row
            self.display_table()
        # Returns an error if the table has not been created.
        except Exception as error:
            print("\nUnable to locate table. Please add an entry to create the table.")

    # Checksi f the Favorite_games table exists, creating it if it doesn't
    def table_creation(self, df):

        # Create table "Favorite_games" in the database, or appends to it if it already exists
        df.to_sql("Favorite_games", con=self.conn, if_exists='append')

        # Commits the changes
        self.conn.commit()

    # Creates or updates table with games that the user has selected.
    def update_table(self, df):
        # Create the table and the database, filling it with the games in the dataframe
        self.table_creation(df)

        # Selects the contents of the table
        self.cur.execute("SELECT * FROM Favorite_games")

        # Print the contents of the database table
        print("\nThe Favorite_games table")
        for row in self.cur.fetchall():
            print(row)
