# Import data analysis library
import pandas as pd
# Import graphing library
import matplotlib.pyplot as plot

# Class that is used to analzye the game data
class Analysis:
    def __init__(self):
        # Make the games.csv file into a dataframe
        self.df = pd.read_csv("data\games.csv")
        # Sets the minimum number of user reviews a game needs to be evaluated
        self.review_min = 1000
        # Sets how many games will be shown when considering the most popular games
        self.result_num = 20

    # Determines the most popular game of each genre
    def most_popular(self, title, genre):
        # Filter out any games with less than 1000 user ratings
        rated_df = self.df[self.df["NumUserRatings"] > self.review_min]
        
        # Filteers out any game that isn't of the correct genres
        genre_df = rated_df[rated_df[genre]==1]
        
        # Include only "BGGId", "Name", "AvgRating", and "NumUserRatings" columns. Sort by AvgRating, and include only the top-rated.
        filtered_df = genre_df[["BGGId", "Name", "AvgRating", "NumUserRatings"]].sort_values(by="AvgRating").tail(1)

        # Add the genre of each game
        filtered_df["Genre"] = title

        # Return the top-rated game of the genre.
        return filtered_df

    # Creates a favorites list that will eventually be put in a dataframe
    def favorites(self):
        # Creates an empty list that will have specified games added to it
        df_list = []
        # Loops, adding new games to the dataframe until the user indicates they are done.
        while(True):
            # Requests the BGGId for the specific game
            user_input = input("Please provide the BGGId of the game you would like to add to your favorites. Press 'q' to quit: ").upper()
            
            # Quits if the user types "Q"
            if user_input == "Q":
                # Returns the favorits_df if it exists
                try:
                    return favorites_df

                # Otherwise, quits to the main menu
                except:
                    break

            # Otherwise, checks if the user's input is an integer
            else:
                try:
                    # Converts the BBGId from a string to an integer
                    integer_input = int(user_input)

                    # Creates a filtered dataframe with the sepcified game and only the desired columns
                    added_df = self.df[self.df["BGGId"]==integer_input]
                    filtered_added_df = added_df[["BGGId", "Name", "AvgRating", "NumUserRatings"]].sort_values(by="AvgRating")

                    # Adds the favorites_df and the new dataframe entry into a list
                    df_list.append(filtered_added_df)

                    # Concatenates the list of dataframes into one dataframe
                    favorites_df = pd.concat(df_list)

                    # Prints the combined dataframe
                    print(favorites_df)
                # Prints error if the user enters a non-Integer
                except:
                    print("Invalid response. Please enter a valid BGGId.")

    # Determines the 20 most popular game of each genre
    def popular_genre(self, genre):
        # Filter out any games with less than 1000 user ratings
        rated_df = self.df[self.df["NumUserRatings"] > self.review_min]
        
        # Filters out any game that isn't of the correct genres
        genre_df = rated_df[rated_df[genre]==1]
        
        # Include only "BGGId", "Name", "AvgRating", and "NumUserRatings" columns. Sort by AvgRating, and include only the 20 top-rated.
        filtered_df = genre_df[["BGGId", "Name", "AvgRating", "NumUserRatings"]].sort_values(by="AvgRating").tail(self.result_num).iloc[::-1]

        # Prints the 20 top-rated game of the genre.
        print("\nThe most popular game of each genre")
        print(filtered_df)
        print("\n")
        # Graphs the 20 top-rated games of the genre
        self.graph_popular(filtered_df.tail(self.result_num), genre)
        
    # Adds the most popular game for each genre in the data set into a combined dataframe
    def genre_elite(self):
        # Empty list that will be filled with dataframes
        df_list = []

        # Dictionary of game column names and the genre they belong to
        genres = {"Cat:Thematic" : "Thematic", "Cat:Strategy" : "Strategy", "Cat:War" : "War", "Cat:Family" : "Family", 
        "Cat:CGS" : "CGS", "Cat:Abstract" : "Abstract", "Cat:Party" : "Party", "Cat:Childrens" : "Childrens"}

        # Iterate through the dictionary, taking the most popular game of each genre and adding it to a combined dataframe.
        for key, val in genres.items():
            # Gets the most popular game of each genre as a dataframe
            genre_df = self.most_popular(val, key)

            # Adds each genre's dataframe entry to a list
            df_list.append(genre_df)

            # Concatenates the list of dataframes into one dataframe
            genres = pd.concat(df_list)
        # Prints the combined dataframe
        print("\nThe most popular game of each genre")
        print(genres)
        print("\n")

        # Returns the genres dataframe
        return genres

    # Creates a graph of the the top 20 rated games and their score
    def graph_popular(self, popular_df, graph_title):
        # Resizes the graph
        plot.rcParams['figure.figsize'] = [18, 10]

        # Prints the bar graph
        popular_df.plot.bar(x="Name", y="AvgRating", rot=70, title=graph_title)
        plot.show(block=True)

    # Determines the 20 most popular games in the dataframe
    def top_twenty(self):
        # Filters out any games with less than 1000 ratings
        filtered_df = self.df[self.df["NumUserRatings"] > self.review_min]

        # Include only "BGGId", "Name", "AvgRating", and "NumUserRatings" columns. Sort by AvgRating, and include only the top 20 rated.
        selection_df = filtered_df[["BGGId", "Name", "AvgRating", "NumUserRatings"]].sort_values(by="AvgRating").tail(20).iloc[::-1]

        # Print the results to console
        print("The 20 most poplar games")
        print(selection_df.tail(self.result_num))
        print("\n")

        # Calls the graph_popular function to 
        self.graph_popular(selection_df.tail(self.result_num), "The 20 Most Popular Games")
