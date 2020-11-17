import os
menu = "Query menu:\n    1 - Lower sales in March 2020 than March 2019\n    2 - Higher sales in June 2020 than June 2019\n    3 - International average sports equipment market size\n    4 - Sporting goods retail sales Aprils of 2017-2020\n    5 - Average sporting goods sales in April before 2020\n    6 - Lowest grossing month for sporting goods sales between 2017-2020\n    7 - Sporting goods retail sales Junes of 2017-2020\n    8 - Average sporting goods sales in June before 2020\n    9 - Highest grossing month for sporting goods sales between 2017-2020\n    10 - Outdoor sporting goods sales stats 2017-2020\n    11 - Outdoor sporting goods sales growth 2019-2020\n    To exit the program, type “exit”"

def clearScreen():
    """
    runs operating system's command to clear the terminal window. Works for both windows and UNIX based environments
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def proceed():
    """
    Declares the end of the output, prompts the user to return to the main menu when he is ready,
    and clears the screen

    """
    print("\n-----------------------\n")
    print("     END OF OUTPUT")
    print("\n-----------------------\n")
    input("Press any key to go back to main menu...")
    clearScreen()

def query1():
    print("Query 1 executed")

def query2():
    print("Query 2 executed")

def query3():
    print("Query 3 executed")

def query4():
    print("Query 4 executed")

def query5():
    print("Query 5 executed")

def query6():
    print("Query 6 executed")

def query7():
    print("Query 7 executed")

def query8():
    print("Query 8 executed")

def query9():
    print("Query 9 executed")

def query10():
    print("Query 10 executed")

def query11():
    print("Query 11 executed")

def main():
    options = { #dictionary of query functions
        1: query1,
        2: query2,
        3: query3,
        4: query4,
        5: query5,
        6: query6,
        7: query7,
        8: query8,
        9: query9,
        10: query10,
        11: query11 
    
    }
    print(menu)
    while True:
        option  = input("Please select an option: ")
        if option == "exit":
            exit()
        #selection = int(input("Please select an option... ")) # ask user for input
        
        try:
            selection  = int(option)
        except(ValueError):
            print("Invalid slection. Value must be a number.")
            continue
        if selection not in options.keys():
                print("Invalid selection. Value must be between 1 and 11 (inclusive).")
                continue
        clearScreen()
        options[selection]() # run selected query
        proceed()
        print(menu)
        continue 
    
main()