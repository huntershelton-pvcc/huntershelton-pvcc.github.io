# Name: Hunter Shelton
# Prog Purpose: This program finds the cost of movie tickets, popcorn, & drinks
#   The output is sent to an .html file

import datetime

##############  define global variables ############
RATE_TUITION_IN = 164.40
RATE_TUITION_OUT = 353
RATE_CAPITAL_FEE = 26
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90


# define global variables

inout = 1 # 1 is in-state, 2 is out of state
numcredits = 0
scholarship_amt = 0

tuition = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0
# create output file
outfile = 'pvccweb.html'


##############  define program functions ################
def main():
    
    open_outfile()
    more = True
    
    while more:
        get_user_data()
        perform_calculations()
        create_output_file()

        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        while(yesno.upper() != "Y" and yesno.upper() != "N"): # loop to actually require Y/y to order again. otherwise, loop was default
            yesno = input("Please press Y if you wish to calculate tuition & fees for another student, or N to end the program.\n")
        if yesno.upper() == "N":
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> PVCC Tuition </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(wp-pvcc.jpg); color: #bfb6a6;">\n')
    
def get_user_data():
    global inout, numcredits, scholarship_amt
    
    print('**** PIEDMONT VIRGINIA COMM COLLEGE Tuition & Fees ****')
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarship_amt = int(input("Scholarship amount received: "))

def perform_calculations():
    global tuition, inst_fee, cap_fee, act_fee, total, balance

    if inout == 1:
        tuition = numcredits * RATE_TUITION_IN
        cap_fee = 0
    else:
        tuition = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE
    
    inst_fee = RATE_INSTITUTION_FEE * numcredits
    act_fee  = RATE_ACTIVITY_FEE * numcredits

    total = tuition + cap_fee + inst_fee + act_fee
    balance = total - scholarship_amt

def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "

    f.write('\n<table border="3" style ="background-color: #491108; font-family: georgia; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2>**** PIEDMONT VIRGINIA COMM COLLEGE ****</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('     Tuition and Fees Report\n')
    
    f.write(tr + 'Tuition' + endtd + '$'+ format(tuition, currency) + endtr)
    f.write(tr + 'Capital Fee' + endtd + '$'+ format(cap_fee, currency) + endtr)
    f.write(tr + 'Institution Fee' + endtd + '$'+ format(inst_fee, currency) + endtr)
    f.write(tr + 'Activity Fee' + endtd + '$'+ format(act_fee, currency) + endtr)

    f.write(tr + 'Total' +  endtd + '$'+ format(total, currency)  + endtr)     
    f.write(tr + 'Scholarship Amount' + endtd + '$'+ format(scholarship_amt, currency) + endtr)
    f.write(tr + 'Balance Due'+ endtd + '$'+ format(balance, currency) + endtr)
    
    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')


##########  call on main program to execute ############
main()              


