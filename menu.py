# Import the program classes
from database import *

# Class that manages the menu. Through user options, functionality from other classes are called.
class Menu():
    def __init__(self):
        pass

    # Function that lets users view the highest reviewed games of a specified genre.
    def menu_database_options(self, analyze):
        # Creates an instance of the database class
        database = Database()
        # Repeats the menu loop until the user breaks it
        while True:
            print("\n************DATABASE OPTIONS**************")
            print("""
            1: Import a database
            2: View your database
            3: Add games to your database
            4: Remove games from your database
            5: Export your database as a .csv file
            \n""")
            # Requests menu option from the user.
            display_input = input("Please enter your selection. Press 'q' to quit: ").upper()
            # Calls the display_name function, allowing the user to search the database by a person's
            # name.
            """SET UP CSV IMPORT"""
            # Imports a database from a csv
            if display_input == "1":
                database.import_csv()
            # Displays the database table
            if display_input == "2":
                database.display_table()
            # Allows the user to create a table of favorites from the game
            elif display_input == "3":
                favorites_df = analyze.favorites()
                database.update_table(favorites_df)
            # Deletes a game from the table of favorites
            elif display_input == "4":
                database.delete_row()
            # Exports the table of favorites to a csv file
            elif display_input == "5":
                database.export_table()            
            # Quits to the main menu
            elif display_input == "Q":
                database.cur.close()
                print("\nReturning to main menu...")
                break  

    # Function that lets users view the highest reviewed games of a specified genre.
    def menu_genre_search(self, analyze):
        # Repeats the menu loop until the user breaks it
        while True:
            print("\n************MAIN MENU**************")
            print("""
            1: Thematic games
            2: Strategy games
            3: War games
            4: Family games
            5: CGS games
            6: Abstract games
            7: Party games
            8: Childrens' games
            Q: Quit/Log Out
            \n""")
            # Requests menu option from the user.
            display_input = input("Please enter your selection: ").upper()
            # Calls the display_name function, allowing the user to search the database by a person's
            # name.
            if display_input == "1":
                analyze.popular_genre("Cat:Thematic")
                break
            # Calls the popular_genre method for the specified genre, displaying the most popular games 
            # of that genre.
            elif display_input == "2":
                analyze.popular_genre("Cat:Strategy")
                break
            elif display_input == "3":
                analyze.popular_genre("Cat:War")
                break
            elif display_input == "4":
                analyze.popular_genre("Cat:Family")
                break
            elif display_input == "5":
                analyze.popular_genre("Cat:CGS")
                break
            elif display_input == "6":
                analyze.popular_genre("Cat:Abstract")
                break                
            elif display_input == "7":
                analyze.popular_genre("Cat:Party")
                break  
            elif display_input == "8":
                analyze.popular_genre("Cat:Childrens")
                break  
            # Quits to the main menu
            elif display_input == "Q":
                print("\nReturning to main menu...")
                break  

    # Main menu option. Allows users to see data regarding data set, as well as call on other menus for particular queries.
    def display_menu(self, analyze):
        # Repeats the menu loop until the user breaks it
        while True:
            print("************MAIN MENU**************")
            print("""
            A: View the top twenty highest-rated games
            B: View the highest-rated game of each genre
            C: View the top twenty highest-rated games of a specific genre
            D: Manage your Favorite Games database
            Q: Quit/Log Out
            """)
            # Asks the user to choose an option. Converts input to uppercase if not already.
            user_input = input("Please enter your selection: ").upper()
            # If user enters "A", allows them to add a new entry to the table.
            if user_input == "A":
                analyze.top_twenty()
            # Calls the dispaly_table function to show the current table.
            elif user_input == "B":
                analyze.genre_elite()
            # Allows the user to search the table for entries, either by name or by birth month.
            elif user_input == "C":
                self.menu_genre_search(analyze)
            # Calls the menu_database_options method
            elif user_input == "D":
                self.menu_database_options(analyze)
            # Quits the program
            elif user_input == "Q":
                print("\nExiting the program. Goodbye.")
                quit()