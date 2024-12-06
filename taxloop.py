# Name: Hunter Shelton
#   Prog Purpose: This program uses loops to find the personal property tax for Charlotesville vehicles
#   and produces a report.
#
# Personal Property tax in Charlottesville:
#   -- 4.40% per year
#   -- Paid every six months
# Personal Property Tax Relief (PPTR):
#   -- Eligibility: vehicles used for personal use only
#   -- Tax relief rate is 30%

import datetime

# define tax rates
PPT_RATE = 0.044   # 4.40%
RELIEF_RATE = 0.30 # 30%

# global variables
line = '----------------------------------'
taxbill = '**** PERSONAL PROPERTY TAX BILL ****'
vehicle_value = 0
eligible = 1 # 1 is yes, 2 is no for tax relief eligibility
relief_amount = 0
total = 0
tax_due = 0


##############  define program functions  ##############
def main():

    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate personal property tax for another vehicle? (Y/N): ")
        while(yesno.upper() != "Y" and yesno.upper() != "N"): # loop to actually require Y/y to order again. otherwise, loop was default
            yesno = input("Please press Y if you wish to calculate personal property tax for another vehicle, or N to end the program.\n")
        if yesno.upper() == "N":
            more = False
            print("Thank you for using the personal property tax calculator.")

def get_user_data():
    global vehicle_value, eligible
    print(taxbill)
    vehicle_value = int(input("Assessed value of the vehicle: $ "))
    eligible = int(input("Is your vehicle eligible for tax relief? Enter 1 for YES, 2 for NO: "))

def perform_calculations():
    global relief_amount, tax_due, total

    if eligible == 1:
        tax_due = (vehicle_value*PPT_RATE)
        relief_amount = tax_due * RELIEF_RATE
    else:
        tax_due = (vehicle_value*PPT_RATE)
        relief_amount = 0

    total = (tax_due - relief_amount)/2

def display_results():
    currency = '8,.2f'
    full_date = str(datetime.datetime.now())

    print(line)
    print(taxbill)
    print('     Please Pay in a Timely Manner')
    print(full_date)
    print(line)
    print('Assessed Value       $ ' + format(vehicle_value,currency))
    print('Relief Amount        $ ' + format(relief_amount,currency))
    print('Full Annual Amount   $ ' + format(total*2, currency))
    print(line)
    print('Total Due            $ ' + format(total, currency))

########## call on main program to execute ##########
main()
