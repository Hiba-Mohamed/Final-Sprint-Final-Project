# Description : Final Sprint project. Menu based program for Taxi company.
# Author      : Robot Group 5 (Summaya Siddiqui, Campbell Kramer, Adam Sparkes, Abdul Reeves, Michael O'Brien, and Hiba Mohamed)
# Date(s)     : April 1- , 2024



# Define required libraries.



#constants# Define program constants.
# Open the defaults file and read the values into variables
f = open('Defaults.dat', 'r')
NEXT_TRANSACTION_NUMBER = int(f.readline())    #143
NEXT_DRIVER_NUMBER      = int(f.readline())    #1922 
MONTHLY_STAND_FEE       = float(f.readline())  #175.00 
DAILY_RENTAL_FEE        = float(f.readline())  #60.00
WEEKLY_RENTAL_FEE       = float(f.readline())  #300.00
HST_RATE                = float(f.readline())  #0.15

def EnterNewEmployee():
    pass

def EnterCompanyRevenue():
    pass

def EnterCompanyExpense():
    pass

def TrackCarRentals():
    pass

def RecordEmployeePayment():
    pass

def PrintCompanyProfitListing():
    pass

def PrintDriverFinancialListing():
    pass

def PrintCompanyOwnedCarsReport():
    while True:
        try:
            NewCar = input("Would ypu like to add a new car before printing comapny-owned cars listing? (Y/N): ").upper()
            if NewCar != "Y" and NewCar != "N":
                print("Data Entry Error:Pleaee type \"Y\" or \"N\"")
        except:
            print("Error occured")




# Main program
while True:
    print()
    print("       HAB Taxi Services ")
    print("     Company Services System")
    print()
    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues. ")
    print("3. Enter Company Expenses. ")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing. ")
    print("7. Print Driver Financial Listing. ")
    print("8. Print Company-Owned Cars Info")
    print("9. Quit Program. ")
    print()

    while True:
        try:
            choice = input("Enter choice (1 - 9): ")
            choice = int(choice)
        except:
            print("Data Entry Error - must be a valid number between 1 and 9. ")
        else:
            if choice < 1 or choice > 9:
                print("Data Entry Error - must be a valid number between 1 and 9.")
            else:
                break

    if choice == 1:
        EnterNewEmployee()

    elif choice == 2:
        EnterCompanyRevenue()

    elif choice == 3:
        EnterCompanyExpense()

    elif choice == 4:
        TrackCarRentals()

    elif choice == 5:
        RecordEmployeePayment()

    elif choice == 6:
        PrintCompanyProfitListing()

    elif choice == 7:
        PrintDriverFinancialListing()

    elif choice == 8:
        PrintCompanyOwnedCarsReport()

    else:
        break

# Write the default values back to the Defaults.dat file
f = open('Defaults.dat', 'w')
f.write("{}\n".format(str(NEXT_TRANSACTION_NUMBER)))
f.write("{}\n".format(str(NEXT_DRIVER_NUMBER)))
f.write("{}\n".format(str(MONTHLY_STAND_FEE)))
f.write("{}\n".format(str(DAILY_RENTAL_FEE)))
f.write("{}\n".format(str(WEEKLY_RENTAL_FEE)))
f.write("{}\n".format(str(HST_RATE)))
f.close()