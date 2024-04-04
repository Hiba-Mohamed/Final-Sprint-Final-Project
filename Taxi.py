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

def PrintCompanyCarsReport():
    while True:
        try:
            NewCar = input("Would ypu like to add a new car before printing comapny-owned cars listing? (Y/N) \"END\" when finished: ").upper()
            if NewCar != "Y" and NewCar != "N":
                print("Data Entry Error: Please type \"Y\" or \"N\"")
        except:
            print("Error occured")
        if NewCar == "Y":
            # Read the last car ID from the file
            with open('CompanyCars.dat', 'r') as file:
                lines = file.readlines()
                # this is the last line and the first entry with index 0 (the carID)
                last_car_id = lines[-1].split()[0]
    
            # add 1 to the latest carID to make it the new car id then turn it to a string
            new_car_id = str(int(last_car_id) + 1)

            CarMake = input("Enter the car's make (e.g. Ford): ").capitalize()
            CarModel = input("Enter the car's model (e.g. Corolla): ").capitalize()
            CarYear = int(input("Enter the car's year (e.g. 2016): "))
            CarLicensePlateNumber = input("Enter car's license plate number (e.g. ABC123 ): ").upper()
            CarType = input("Indicate if the car is business-owned or an employees own car (Type \"BO\" or \"EO\"): ").upper()

            # Write the new car details including the new Car ID to the file
            with open('CompanyCars.dat', 'a') as file:
                file.write(f"{new_car_id} {CarMake} {CarModel} {CarYear} {CarLicensePlateNumber} {CarType}\n")

            print("")
            print("   Car ID    Car Make   Car Model   Car Year   Plate Number   Owned By")
            print("-------------------------------------------------------------------------")
            with open('CompanyCars.dat', 'r') as file:
                for car in file:
                # Split the car details by spaces
                    car_details = car.strip().split()
                    if car_details[-1] == "BO":
                        car_details[-1] = "Business"
                    else:
                        car_details[-1] = "Employee"
                # Print the formatted car details
                    print("{:<12} {:<12} {:<12} {:<12} {:<10} {:<8}".format(*car_details))
                    print("")

        else:
            print("")
            print("   Car ID    Car Make   Car Model   Car Year   Plate Number   Owned By")
            print("-------------------------------------------------------------------------")
            with open('CompanyCars.dat', 'r') as file:
                for car in file:
                # Split the car details by spaces
                    car_details = car.strip().split()
                    if car_details[-1] == "BO":
                        car_details[-1] = "Business"
                    else:
                        car_details[-1] = "Employee"
                # Print the formatted car details
                    print("{:<12} {:<12} {:<12} {:<12} {:<10} {:<8}".format(*car_details))
                    print("")
        if NewCar == "END":
            break


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
    print("8. Print Cars Information report")
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
        PrintCompanyCarsReport()

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