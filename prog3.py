import os
import pymongo
import pandas as pd

# connect to our mongo cluster
myclient = pymongo.MongoClient("mongodb+srv://JackRothberg:Minot2tru!@cluster0.59eck.mongodb.net/covidSportingGoods")

# use specific database
mydb = myclient["covidSportingGoods"]

menu = "Query menu:\n    1 - Retail Percentage from 2019 of March 2020 vs June 2020\n    2 - International average sports equipment market size\n    3 - Sporting goods retail sales stats Aprils of 2017-2020\n    4 - Sporting goods retail sales stats Junes of 2017-2020\n    5 - Outdoor sporting goods sales stats 2017-2019 and Outdoor sporting goods sales growth 2019-2020\nTo exit the program, type “exit”"

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
    print("Retail sale percentage 2020 from 2019 in March")
    # use salesBySector collection
    mycol = mydb["salesBySector"]
    lst = mycol.find( {"RetailPercentFrom2019": {"$lt": 0}, "Month": "March" }, {"Sector":1, "RetailPercentFrom2019":1, "_id":0} )
    df1 = pd.DataFrame(lst)
    print(df1)

    print("\n")

    print("Retail sale percentage 2020 from 2019 in June")
    # use salesBySector collection
    mycol = mydb["salesBySector"]
    lst = mycol.find( {"RetailPercentFrom2019": {"$gt": 0}, "Month": "June" }, {"Sector":1, "RetailPercentFrom2019":1, "_id":0} )
    df2 = pd.DataFrame(lst)
    print(df2)

    print("\n")

    print("Intersection")
    # https://www.geeksforgeeks.org/intersection-of-two-dataframe-in-pandas-python/
    int_df = pd.merge(df1, df2, how ='inner', on =['Sector'])
    print(int_df)

def query2():
    # use sportsEquipmentMarketSize collection
    mycol = mydb["sportsEquipmentMarketSize"]
    
    print("Market Size 2017 - 2020")
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

def query3():
    # use sportingGoodsRetail collection
    mycol = mydb["sportingGoodsRetail"]

    print("Retail sales in April 2017 - 2020")
    # display retail sales in April 2017 - 2020
    lst = mycol.find( { "Month": "April" }, {"Year":1, "RetailSales":1, "_id":0} )
    df = pd.DataFrame(lst)
    df.sort_values(by=['Year'], inplace=True)
    print(df)

    print("\n")

    print("Avg retail sales in April 2017 - 2020")
    # display avg retail sales in April 2017 - 2020
    lst = mycol.aggregate([ { "$match": { "Month": "April", "Year": {"$lt": 2020} } }, {"$group":{"_id": "$Month", "avgRetail": { "$avg": "$RetailSales" }}}])
    df = pd.DataFrame(lst)
    del df['_id']
    print(df)

    print("\n")

    print("Min retail sales from 2017 - 2020")
    # display min retail sales from 2017 - 2020
    lst = mycol.aggregate([ {"$group":{"_id": "null", "MinRetail": { "$min": "$RetailSales" }}}])
    df = pd.DataFrame(lst)
    del df['_id']
    print(df)

def query4():
    # use sportingGoodsRetail collection
    mycol = mydb["sportingGoodsRetail"]

    print("Sporting goods retail sales Junes of 2017-2020")
    # display Sporting goods retail sales Junes of 2017-2020
    lst = mycol.find( { "Month": "June" }, {"Year":1, "RetailSales":1, "_id":0} )
    df = pd.DataFrame(lst)
    df.sort_values(by=['Year'], inplace=True)
    print(df)

    print("\n")

    print("Avg retail sales in June 2017 - 2019")
    # display avg retail sales in June 2017 - 2019
    lst = mycol.aggregate([ { "$match": { "Month": "June", "Year": {"$lt": 2020} } }, {"$group":{"_id": "$Month", "avgRetail": { "$avg": "$RetailSales" }}}])
    df = pd.DataFrame(lst)
    del df['_id']
    print(df)

    print("\n")

    print("Max retail sales from 2017 - 2020")
    # display max retail sales from 2017 - 2020
    lst = mycol.aggregate([ {"$group":{"_id": "null", "MaxRetail": { "$max": "$RetailSales" }}}])
    df = pd.DataFrame(lst)
    del df['_id']
    print(df)

def query5():
    # use outdoorSportsEquipmentRetail collection
    mycol = mydb["outdoorSportsEquipmentRetail"]

    print("Outdoor sporting goods sales stats 2017-2019")
    # display Outdoor sporting goods sales stats 2017-2019
    lst = mycol.find( { "Year": { "$in": [2017, 2018, 2019] } }, {"_id":0, "Year":1, "Revenue":1} )
    df = pd.DataFrame(lst)
    df.sort_values(by=['Year'], inplace=True)
    print(df)

    # YEARLY GROWTH: ( (14726 - 11272) + (18408 - 14726) ) / 2 = 3568
    print("\nYEARLY GROWTH: ( (14726 - 11272) + (18408 - 14726) ) / 2 = 3568")

    print("\n")

    print("Outdoor sporting goods sales stats 2019 and 2020")
    # display Outdoor sporting goods sales stats 2019 and 2020
    lst = mycol.find( { "Year": { "$in": [2019, 2020] } }, {"_id":0, "Year":1, "Revenue":1} )
    df = pd.DataFrame(lst)
    df.sort_values(by=['Year'], inplace=True)
    print(df)

    # 2019 - 2020 GROWTH: 23192 - 18408 = 4784
    print("\n2019 - 2020 GROWTH: 23192 - 18408 = 4784")
    

def main():
    clearScreen()

    options = { #dictionary of query functions
        1: query1,
        2: query2,
        3: query3,
        4: query4,
        5: query5
    
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
            print("Invalid selection. Value must be a number.")
            continue
        if selection not in options.keys():
                print("Invalid selection. Value must be between 1 and 5 (inclusive).")
                continue
        clearScreen()
        options[selection]() # run selected query
        proceed()
        print(menu)
        continue 
    
main()