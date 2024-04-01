# Description : Final Sprint project. Menu based program for Taxi company.
# Author      : Robot Group 5 (Summaya Siddiqui, Campbell Kramer, Adam Sparkes, Abdul Reeves, Michael O'Brien, and Hiba Mohamed)
# Date(s)     : April 1- , 2024





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

def NewReport():
    pass




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
    print("8. Your report – add description here.")
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
        NewReport()

    else:
        break

