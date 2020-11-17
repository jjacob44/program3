import os
import pymongo
import pandas as pd

# connect to our mongo cluster
myclient = pymongo.MongoClient("mongodb+srv://JackRothberg:Minot2tru!@cluster0.59eck.mongodb.net/covidSportingGoods")

# use specific database
mydb = myclient["covidSportingGoods"]

menu = "Query menu:\n    1 - Lower sales in March 2020 than March 2019\n    2 - Higher sales in June 2020 than June 2019\n    3 - International average sports equipment market size\n    4 - Sporting goods retail sales Aprils of 2017-2020\n    5 - Average sporting goods sales in April before 2020\n    6 - Lowest grossing month for sporting goods sales between 2017-2020\n    7 - Sporting goods retail sales Junes of 2017-2020\n    8 - Average sporting goods sales in June before 2020\n    9 - Highest grossing month for sporting goods sales between 2017-2020\n    10 - Outdoor sporting goods sales stats 2017-2019\n    11 - Outdoor sporting goods sales growth 2019-2020\n    To exit the program, type “exit”"

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
    # use salesBySector collection
    mycol = mydb["salesBySector"]
    lst = mycol.find( {"RetailPercentFrom2019": {"$lt": 0}, "Month": "March" }, {"Sector":1, "RetailPercentFrom2019":1, "_id":0} )
    df = pd.DataFrame(lst)
    print(df)

def query2():
    # use salesBySector collection
    mycol = mydb["salesBySector"]
    lst = mycol.find( {"RetailPercentFrom2019": {"$gt": 0}, "Month": "June" }, {"Sector":1, "RetailPercentFrom2019":1, "_id":0} )
    df = pd.DataFrame(lst)
    print(df)

def query3():
    # use sportsEquipmentMarketSize collection
    mycol = mydb["sportsEquipmentMarketSize"]
    
    print("--------Market Size 2017 - 2020----------")
    # display market size from 2017 - 2020
    lst = mycol.find({"Year": {"$in": [2017, 2018, 2019, 2020]}})
    df = pd.DataFrame(lst)
    df.sort_values(by=['Year'], inplace=True)
    del df['_id']
    print(df)

    print("--------Avg Market Size 2017 - 2019----------")

    # display average market size of 2017 - 2019
    lst = mycol.aggregate([ { "$match": { "Year": {"$in": [2017,2018,2019] } } }, {"$group":{"_id": "null", "avgMarketSize": { "$avg": "$MarketSize" }}}])
    df = pd.DataFrame(lst)
    del df['_id']
    print(df)

def query4():
    # use sportingGoodsRetail collection
    mycol = mydb["sportingGoodsRetail"]

    # display retail sales in April 2017 - 2020
    lst = mycol.find( { "Month": "April" }, {"Year":1, "RetailSales":1, "_id":0} )
    df = pd.DataFrame(lst)
    df.sort_values(by=['Year'], inplace=True)
    print(df)

def query5():

    query4()

    print("\n")

    # use sportingGoodsRetail collection
    mycol = mydb["sportingGoodsRetail"]

    # display avg retail sales in April 2017 - 2020
    lst = mycol.aggregate([ { "$match": { "Month": "April", "Year": {"$lt": 2020} } }, {"$group":{"_id": "$Month", "avgRetail": { "$avg": "$RetailSales" }}}])
    df = pd.DataFrame(lst)
    del df['_id']
    print(df)

def query6():
    # use sportingGoodsRetail collection
    mycol = mydb["sportingGoodsRetail"]

    # display min retail sales from 2017 - 2020
    lst = mycol.aggregate([ {"$group":{"_id": "null", "MinRetail": { "$min": "$RetailSales" }}}])
    df = pd.DataFrame(lst)
    del df['_id']
    print(df)

def query7():
    # use sportingGoodsRetail collection
    mycol = mydb["sportingGoodsRetail"]

    # display avg retail sales in June 2017 - 2020
    lst = mycol.find( { "Month": "June" }, {"Year":1, "RetailSales":1, "_id":0} )
    df = pd.DataFrame(lst)
    df.sort_values(by=['Year'], inplace=True)
    print(df)

def query8():
    # use sportingGoodsRetail collection
    mycol = mydb["sportingGoodsRetail"]

    # display avg retail sales in June 2017 - 2019
    lst = mycol.aggregate([ { "$match": { "Month": "June", "Year": {"$lt": 2020} } }, {"$group":{"_id": "$Month", "avgRetail": { "$avg": "$RetailSales" }}}])
    df = pd.DataFrame(lst)
    del df['_id']
    print(df)

def query9():
    # use sportingGoodsRetail collection
    mycol = mydb["sportingGoodsRetail"]

    # display max retail sales from 2017 - 2020
    lst = mycol.aggregate([ {"$group":{"_id": "null", "MaxRetail": { "$max": "$RetailSales" }}}])
    df = pd.DataFrame(lst)
    del df['_id']
    print(df)

def query10():
    # use outdoorSportsEquipmentRetail collection
    mycol = mydb["outdoorSportsEquipmentRetail"]

    print("Outdoor sporting goods sales stats 2017-2019")
    # display Outdoor sporting goods sales stats 2017-2019
    lst = mycol.find( { "Year": { "$in": [2017, 2018, 2019] } }, {"_id":0, "Year":1, "Revenue":1} )
    df = pd.DataFrame(lst)
    df.sort_values(by=['Year'], inplace=True)
    print(df)

    print("\n")

    print("Outdoor sporting goods sales stats 2019 and 2020")
    # display Outdoor sporting goods sales stats 2019 and 2020
    lst = mycol.find( { "Year": { "$in": [2019, 2020] } }, {"_id":0, "Year":1, "Revenue":1} )
    df = pd.DataFrame(lst)
    df.sort_values(by=['Year'], inplace=True)
    print(df)

def query11():
    # use outdoorSportsEquipmentRetail collection
    mycol = mydb["outdoorSportsEquipmentRetail"]

    # display Outdoor sporting goods sales stats 2017-2019
    lst = mycol.find( { "Year": { "$in": [2019, 2020] } }, {"_id":0, "Year":1, "Revenue":1} )
    df = pd.DataFrame(lst)
    df.sort_values(by=['Year'], inplace=True)
    print(df)

def main():
    clearScreen()

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