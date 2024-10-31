# Name: Hunter Shelton
# Prog Purpose: This program finds the cost of movie tickets
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime

############## define global variables ##############
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99

# define global varables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

############## define program functions ##############
def main():
    
    more_tickets = True
    
    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()
        
        yesno = input("\nWould you like to order again (Y or N)? ")
        while(yesno != "Y" and yesno != "y" and yesno != "N" and yesno != "n"): # loop to actually require Y/y to order again. otherwise, loop was default
            yesno = input("Please press Y if you wish to order again, or N to end the program.\n")
        if yesno == "N" or yesno == "n":
            more_tickets = False
            print("Thank you for your order. Enjoy your movie!")
            

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: ")) # script will throw an error if input is not valid int

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():  
    print('------------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print('------------------------------')
    print('Tickets      $ ' + format(subtotal,'8,.2f'))
    print('Sales Tax    $ ' + format(sales_tax,'8,.2f'))
    print('Total        $ ' + format(total,'8,.2f'))
    print('------------------------------')
    print(str(datetime.datetime.now()))

########## call on main program to execute ##########
main()
