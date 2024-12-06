# Name: Hunter Shelton
#   Prog Purpose: This program uses lists to find the personal property tax for Charlotesville vehicles
#   and produces a report.
#
# Personal Property tax in Charlottesville:
#   -- 4.20% per year
#   -- Paid every six months
# Personal Property Tax Relief (PPTR):
#   -- Eligibility: vehicles used for personal use only
#   -- Tax relief rate is 33%

import datetime

# define tax rates
PPT_RATE = 0.042   # 4.20%
RELIEF_RATE = 0.33 # 33%

# list data
vehicle = ["2019 Volvo ",
           "2018 Toyota",
           "2022 Kia   ",
           "2020 Ford  ",
           "2023 Honda ",
           "2019 Lexus ",]
vehicle_value = [13000, 10200, 17000, 21000, 28000, 16700]
pptr_eligible = ["Y", "Y", "N", "Y", "N", "Y",]
owner_name = ["Brand, Debra      ",
              "Smith, Carter     ",
              "Johnson, Bradley  ",
              "Garcia, Jennifer  ",
              "Henderson, Leticia",
              "White, Danielle   ",]
ppt_owed = []

# global variables

num_vehicles = len(vehicle)
tax_due = 0
total = 0

# note: having done C in the past I really want to make a struct for better organization
# in C/CPP I would have made something like:
# struct taxcars {
#   char* carname;
#   int value;
#   bool pptrEligible;
#   char* owner_name;
#   }
# I think the python equivalent would be a dictionary?

##############  define program functions  ##############
def main():
    perform_calculations()
    display_results()

def perform_calculations():
    global total, tax_due

    for i in range(num_vehicles):
        tax_due = (vehicle_value[i]*PPT_RATE /2)
        if pptr_eligible[i].upper() == "Y":
            tax_due = tax_due * (1-RELIEF_RATE)
        ppt_owed.append(tax_due)
        total = total + tax_due

def display_results():
    currency = '8,.2f'
    line = '-------------------------------------------------------------------------'
    taxbill = '******* PERSONAL PROPERTY TAX BILL *******'
    tab = "\t"
    full_date = str(datetime.datetime.now())
    short_date = full_date[0:16]

    print(line)
    print(tab + taxbill)
    print("\t\tCharlottesville, Virginia")
    print("\n\t\tRUN DATE/TIME: " + short_date)
    print("\nNAME" + tab + tab + tab + "VEHICLE" + tab + tab + "VALUE" + tab + tab + "RELIEF" + tab + "TAX_DUE")
    print(line)
    for i in range(num_vehicles):
        print(owner_name[i] + tab + vehicle[i] + tab + format(vehicle_value[i], currency) + tab + pptr_eligible[i] + tab + format(ppt_owed[i], currency))
    print(line)
    print("******************************* TOTAL TAX DUE: " + tab + format(total, currency))

########## call on main program to execute ##########
main()
