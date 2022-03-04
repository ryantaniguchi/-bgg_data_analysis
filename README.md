# Overview

This program analyzes a database from Kaggle, [Board game Database from BoardGameGeek](https://www.kaggle.com/threnjen/board-games-database-from-boardgamegeek), which contains user data taken from the board gaming website, BoardGameGeek. It analyzes the data in order to determine the highest-reviewed games hosted on that website, both in general and for specific genres. The program allows a user to create a database table of their favorite games from that website and to export that data as a .csv file.

This program was developed largely out of an interest in data analysis and the pandas library. Data analysis is something that is of great interest to me, and I wanted to learn more about the pandas library and how it was used to anlayze data sets such as Board game Database from BoardGameGeek. In addition, I have a great interest in board and card games, and hoped to perhaps find new games that would be of interest to me.

[Software Demo Video](https://youtu.be/aJ6JzZyQp9g)

# Data Analysis Results

1. Based on average rating, what are the top twenty highest-rated games when accounting for number of reviews?
    1. Mage Knight: Ultimate Edition
    2. Trickerion: Collector's Edition
    3. Middara: Unintentional Malum – Act 1
    4. Gloomhaven
    5. Too Many Bones: Undertow
    6. Gloomhaven: Jaws of the Lion
    7. Clank!: Legacy – Acquisitions Incorporated
    8. Twilight Imperium: Fourth Edition
    9. Aeon's End: The New Age
    10. Eclipse: Second Dawn for the Galaxy
    11. War of the Ring Collector's Edition
    12. Brass: Birmingham
    13. Pandemic Legacy: Season 0
    14. Kanban EV
    15. Kingdom Death: Monster
    16. Pandemic Legacy: Season 1
    17. Sleeping Gods
    18. War of the Ring: Second Edition
    19. The Castles of Burgundy
    20. Gaia Project
<br/><br/>
2. What is the highest rated game per subgenre?
    * Thematic - Middara: Unintentional Malum – Act 1
    * Strategy - Gloomhaven
    * War - War of the Ring: Second Edition
    * Family - The Crew: Mission Deep Sea
    * CGS - Star Wars: X-Wing (Second Edition)
    * Abstract - Cascadia
    * Party - Human Punishment: Social Deduction 2.0
    * Childrens - Zombie Kidz Evolution

# Development Environment

This program was developed using Visual Studio Code 1.64.2 and GitHub.

This program was written in Python 3.9.10 using the following libraries:
* matplotlib 3.5.1
* sqlite3
* csv
* pandas 1.4.1

# Useful Websites

* [Pandas - Overview of Pandas](https://pandas.pydata.org/docs/getting_started/overview.html)
* [Kaggle](https://www.kaggle.com/)
* [Towards Data Science - Getting started with Data Analysis with Python Pandas](https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77)

# Future Work

* Allow creation of multiple database tables to hold data
* Allow users to query for different columns in datasets
* Allow only unique entries in tables
