# Name: Hunter Shelton
# Prog Purpose: This program finds the cost of a meal at Branch Barbeque Buffet
#   Price for one adult meal: $19.95
#   Price for one child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime

############## define global variables ##############
# define tax rate and prices
SALES_TAX_RATE = .062
SERVICE_FEE_RATE = .10
ADULT_MEAL = 19.95
CHILD_MEAL = 11.95

# define global varables
num_adult = 0
num_child = 0
cost_adult = 0
cost_child = 0
subtotal = 0
sales_tax = 0
service_fee = 0
total = 0

############## define program functions ##############
def main():
    
    order_again = True
    
    while order_again:
        get_user_data()
        perform_calculations()
        display_results()
        
        yesno = input("\nWould you like to order again (Y or N)? ")
        while(yesno != "Y" and yesno != "y" and yesno != "N" and yesno != "n"): # loop to actually require Y/y to order again. otherwise, loop was default
            yesno = input("Please press Y if you wish to order again, or N to end the program.\n")
        if yesno == "N" or yesno == "n":
            order_again = False
            print("Thank you for your order. Enjoy your meal!")
            

def get_user_data():
    global num_adult
    global num_child
    num_adult = int(input("Number of adult meals: ")) # script will throw an error if input is not valid int
    num_child = int(input("Number of child meals: ")) # script will throw an error if input is not valid int

def perform_calculations():
    global subtotal, sales_tax, total, cost_child, cost_adult, service_fee
    cost_adult = num_adult * ADULT_MEAL
    cost_child = num_child * CHILD_MEAL
    subtotal = cost_adult + cost_child
    service_fee = subtotal * SERVICE_FEE_RATE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + service_fee + sales_tax

def display_results():  
    print('------------------------------')
    print('**** Branch Barbeque Buffet ****')
    print('------------------------------')
    print('Adult Meals  $ ' + format(cost_adult,'8,.2f'))
    print('Child Meals  $ ' + format(cost_child,'8,.2f'))
    print('Subtotal     $ ' + format(subtotal,'8,.2f'))
    print('Service Fee  $ ' + format(service_fee,'8,.2f'))
    print('Sales Tax    $ ' + format(sales_tax,'8,.2f'))
    print('Total        $ ' + format(total,'8,.2f'))
    print('------------------------------')
    print(str(datetime.datetime.now()))

########## call on main program to execute ##########
main()
