# Name: Hunter Shelton
# Prog Purpose: This program finds the cost of a meal at Palermo Pizza

import datetime

##############  define global variables  ##############

PRICE_SMALL = 9.99
PRICE_MED = 12.99
PRICE_LARGE = 17.99
PRICE_XL = 21.99
PRICE_DRINK = 3.99
PRICE_BREADSTICKS = 6.99
SALES_TAX_RATE = .055


# define global variables

pizza_size = ""

# item counts
num_pizzas = 0
num_drinks = 0
num_breadsticks = 0

# cost tallies
cost_pizzas = 0
cost_drinks = 0
cost_breadsticks = 0

# totals
subtotal = 0
sales_tax = 0
total = 0

##############  define program functions  ##############
def main():

    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        while(yesno.upper() != "Y" and yesno.upper() != "N"): # loop to actually require Y/y to order again. otherwise, loop was default
            yesno = input("Please press Y if you wish to order again, or N to end the program.\n")
        if yesno.upper() == "N":
            more = False
            print("Thank you for your order. Enjoy your pizza!")

def get_user_data():
    global pizza_size, num_pizzas, num_drinks, num_breadsticks
    
    print('****** Palermo Pizza ******')
    print ('S Small Pizza       $ '+str(PRICE_SMALL))
    print ('M Medium Pizza      $ '+str(PRICE_MED))
    print ('L Large Pizza       $ '+str(PRICE_LARGE))
    print ('X Extra Large Pizza $ '+str(PRICE_XL))

    pizza_size = input("\nWhat size pizza would you like to order? (S, M, L, X): ")
    pizza_size = pizza_size.upper()
    while(pizza_size != "S" and pizza_size != "M" and pizza_size != "L" and pizza_size != "X"):
        pizza_size = input("\nPlease input a valid pizza size. (S, M, L, X): ")
        pizza_size = pizza_size.upper()

    num_pizzas = int(input("Number of pizzas: "))
    num_drinks = int(input("Number of drinks: "))
    num_breadsticks = int(input("Number of breadstick orders: "))

def perform_calculations():
    global cost_pizzas, cost_drinks, cost_breadsticks, subtotal, total, sales_tax

    if pizza_size == "S":
        cost_pizzas = num_pizzas * PRICE_SMALL
    elif pizza_size == "M":
        cost_pizzas = num_pizzas * PRICE_MED
    elif pizza_size == "L":
        cost_pizzas = num_pizzas * PRICE_LARGE
    elif pizza_size == "X":
        cost_pizzas = num_pizzas * PRICE_XL
    
    cost_drinks = num_drinks * PRICE_DRINK
    cost_breadsticks = num_breadsticks * PRICE_BREADSTICKS

    subtotal = cost_pizzas + cost_drinks + cost_breadsticks
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    currency = '8,.2f'
    line = '----------------------------------'
    full_date = str(datetime.datetime.now())
    short_date = full_date[0:16]

    print(line)
    print('****** Palermo Pizza ******')
    print(short_date)
    print(line)
    print('Number of pizzas ordered:      '+ str(num_pizzas))
    #print('Number of drinks ordered:      '+ str(num_drinks))
    #print('Number of breadsticks ordered: '+ str(num_breadsticks))
    print(line)
    print('Pizzas       $ ' + format(cost_pizzas,currency))
    print('Drinks       $ ' + format(cost_drinks,currency))
    print('Breadsticks  $ ' + format(cost_breadsticks,currency))
    print(line)
    print('Subtotal     $ ' + format(subtotal,currency))
    print('Sales Tax    $ ' + format(sales_tax,currency))
    print('Total        $ ' + format(total,currency))
    print(line)
    print(full_date)

########## call on main program to execute ##########
main()
