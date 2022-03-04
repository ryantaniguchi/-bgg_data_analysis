# Import the program classes
from analysis import *
from menu import *

def main():
    # Creates an instance of the Analysis(), Menu(), and classes
    analyze = Analysis()
    menu_options = Menu()
    
    # Calls the menu
    menu_options.display_menu(analyze)

if __name__ == '__main__':
    main()