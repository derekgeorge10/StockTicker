import random 


#print("hello world")

_oil = "oil"
_grain = "grain"
_gold = "gold"
_silver = "silver"
_industrail = "industrail"
_bonds = "bonds"

starting_value = 5000

inital_oil_cost = 1000

stock_library = []
money_library = []

num_players = int(input("Welcome to Stock Ticker. How many players will be playing today? \n"))
_OpeningStatement = """You have $5,000 to start. Please Choose the stocks that you would like to invest in.\n
Choices include: Oil, Grain, Gold, Silver, Industrial and Bonds.\n""" 
#print(_OpeningStatement)

while num_players > 0:  #game is played in this while loop.. Or is it? Players do get eliminated 
    if num_players == 2:
        player_one = input("What is the name of player 1? \n")
        
        player_two = input("What is the name of player 2? \n")
        
        inital_stock_choice1 = input(player_one  + ' ' + _OpeningStatement)
        
        if inital_stock_choice1 == _oil:
            inital_investment = str(input("How much would you like to invest in? \n"))
            
            if int(inital_investment) <= int(starting_value):
                print("You have invested " + inital_investment + " in the stock of " + inital_stock_choice1)
                
                updated_value = int(inital_investment) - int(starting_value)
                print(player_one + ' ' +"now has " + str(updated_value) + " left in their wallet \n\n")
                
            stock_library.append(inital_stock_choice1)
            print(stock_library)
            
        if inital_stock_choice1 == _grain:
            inital_investment = str(input("How much would you like to invest in? \n"))
            
            if int(inital_investment) <= int(starting_value):
                print("You have invested " + inital_investment + " in the stock of " + inital_stock_choice1)
                
                updated_value = int(inital_investment) - int(starting_value)
                
                print(player_one + ' ' +"now has " + str(updated_value) + " left in their wallet \n\n")
                print(player_one + ' ' +"now has " + str(updated_value) + " left in their wallet \n\n")
                
            stock_library.append(inital_stock_choice1)
            print(stock_library)
            
            
                
                
                
                
        #inital_stock_choice2 = input(player_two  + ' ' + _OpeningStatement)
        #if  inital_stock_choice2 == _oil:
         #   inital_investment = str(input("How much would you like to invest in? \n"))
          #  
           # if int(inital_investment) <= int(starting_value):
            #    print("You have invested " + inital_investment + " in the stock of " + inital_stock_choice2)
            #    updated_value = int(inital_investment) - int(starting_value)
             #   print(player_two + ' ' +"now has " + str(updated_value) + " left in their wallet")
                
            #stock_library.append(inital_stock_choice2)
            #print(stock_library)
            
      #  if  inital_stock_choice2 == _grain:
       #     inital_investment = str(input("How much would you like to invest in? \n"))
                
                
                
                
            

            
        
        
        
            
        
        
        





