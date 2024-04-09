# Description : Final Sprint project. Menu based program for Taxi company.
# Author      : Robot Group 5 (Summaya Siddiqui, Campbell Kramer, Adam Sparkes, Abdul Reeves, Michael O'Brien, and Hiba Mohamed)
# Date(s)     : April 1- , 2024



# Define required libraries.
import datetime
import FormatValues as FV
import time
import sys


#constants# Define program constants.

TODAY = datetime.datetime.now()
# Open the defaults file and read the values into variables
def ReadDefaults():

    f = open('Defaults.dat', 'r')

    NEXT_TRANSACTION_NUMBER = int(f.readline())   #143
    NEXT_DRIVER_NUMBER = int(f.readline())        #1922 
    MONTHLY_STAND_FEE = float(f.readline())       #175.00 
    DAILY_RENTAL_FEE = float(f.readline())       #60.00
    WEEKLY_RENTAL_FEE = float(f.readline())      #300.00
    HST_RATE = float(f.readline())

    return NEXT_TRANSACTION_NUMBER, NEXT_DRIVER_NUMBER, MONTHLY_STAND_FEE, DAILY_RENTAL_FEE, WEEKLY_RENTAL_FEE, HST_RATE

def WriteDefaults(NEXT_TRANSACTION_NUMBER, NEXT_DRIVER_NUMBER, MONTHLY_STAND_FEE, DAILY_RENTAL_FEE, WEEKLY_RENTAL_FEE, HST_RATE):

    f = open('Defaults.dat', 'w')
    
    f.write("{}\n".format(str(NEXT_TRANSACTION_NUMBER)))
    f.write("{}\n".format(str(NEXT_DRIVER_NUMBER)))
    f.write("{}\n".format(str(MONTHLY_STAND_FEE)))
    f.write("{}\n".format(str(DAILY_RENTAL_FEE)))
    f.write("{}\n".format(str(WEEKLY_RENTAL_FEE)))
    f.write("{}\n".format(str(HST_RATE)))

def EnterNewEmployee():
    NEXT_TRANSACTION_NUMBER, NEXT_DRIVER_NUMBER, MONTHLY_STAND_FEE, DAILY_RENTAL_FEE, WEEKLY_RENTAL_FEE, HST_RATE = ReadDefaults()
    while True:
    # Gather user inputs
    
    # Employee Name
        while True:
            FirstName = input("Enter employee first name: ").title()
            if FirstName == "":
                print("Data Entry Error - Employee first name cannot be blank.")
            else:
                break
        while True:
            LastName = input("Enter employee last name: ").title()
            if LastName == "":
                print("Data Entry Error - Employee first name cannot be blank.")
            else:
                break
        EmployeeName = FirstName + " " + LastName

        # Employee Address
        StAddress = input("Enter employee street address: ").title()
        City = input("Enter employee city: ").title()
        Prov = input("Enter employee province (XX): ").upper()
        
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        allowed_num = set("0123456789")
        while True:
            PostalCode = input("Enter driver's postal code (X0X0X0): ").upper()
            if PostalCode == "":
                print("Error - Postal code cannot be blank.")
            elif len(PostalCode) != 6:
                print("Error - Postal code can be of 6 characrters only.")
            elif set(PostalCode[0]).issubset(allowed_char) == False and set(PostalCode[2]).issubset(allowed_char) == False and set(PostalCode[4]).issubset(allowed_char) == False:
                print("Error - The 1st, 3rd and 5th character in a postal code can be an alphabet only.")
            elif set(PostalCode[1]).issubset(allowed_num) == False and set(PostalCode[3]).issubset(allowed_num) == False and set(PostalCode[5]).issubset(allowed_num) == False:
                print("Error - The 1st, 3rd and 5th character in a postal code can be an alphabet only.")
            else:
                break
        PostCode = PostalCode[0] + PostalCode[1] + PostalCode[2] + PostalCode[3] + PostalCode[4] + PostalCode[5]
        
        EmployeeAdd = StAddress + "," + " " + City + "," + " " + Prov + "," + " " + PostCode

        # Employee Phone Number
        while True:
            PhoneNum = input("Enter employee phone number (9999999999): ")
            if PhoneNum == "":
                print("Data Entry Error - Phone number cannot be blank.")
            elif PhoneNum.isdigit() == False:
                print("Data Entry Error - Phone number contains digits only.")
            elif len(PhoneNum) != 10:
                print("Data Entry Error - Phone number contains 10 digits only.")
            else:
                break
        EmployeePhone = "(" + PhoneNum[0:3] + ")" + " " + PhoneNum[3:6] + "-" + PhoneNum[6:11]

        # Employee's License and Insurance Detail
        LicenseNum = input("Enter driver's license number: ").capitalize()
        
        while True:
            try:
                LicenseExpiryDate = input("Enter driver's license expiry date (YYYY-MM-DD): ")
                LicenseExpiryDate = datetime.datetime.strptime(LicenseExpiryDate, "%Y-%m-%d")
            except:
                print("Data Entry Error - Expiry date is not in a valid format.")
            else:
                break
        
        InsuranceCompany = input("Enter insurance policy company: ").title()
        PolicyNumber = input("Enter insurance policy number: ")

        CarLst = ["O" , "R"]
        while True:
            CarType = input("Enter if the driver has his own car or a rented car (O / R): ").upper()
            if CarType == "":
                print("Data Entry Error - Car type can not be blank.")
            elif CarType not in CarLst:
                print("Data Entry Error - invalid entry.") 
            elif CarType == "R":
                NumDays = input("Enter the number of days car is rented for: ")
                NumDays = int(NumDays)
                break
            else:
                break
    
        BalDue = input("Enter the amount of balance due: ")
        BalDue = float(BalDue)

        # Perform required calculations.
        if CarType == "O":
            TotalRentalFee = 0
            NumDays = 0
            MonthlyFee = MONTHLY_STAND_FEE

        if CarType == "R":
            MonthlyFee = 0
            if NumDays == 7:
                TotalRentalFee = WEEKLY_RENTAL_FEE
            elif NumDays >= 1 and NumDays < 7:
                TotalRentalFee = DAILY_RENTAL_FEE * NumDays
            

        HST = (MonthlyFee + TotalRentalFee) * HST_RATE

        TotalFee = MonthlyFee + TotalRentalFee + HST

        NEXT_DRIVER_NUMBER += 1

        # Display results
        print()
        print(f"            HAB TAXI SERVICES - EMPLOYEE DETAIL")
        print(f"---------------------------------------------------------")
        print()
        print(f" Driver ID:                 {NEXT_DRIVER_NUMBER - 1}")
        print(f" Employee Name:             {EmployeeName}")
        print(f" Employee Address:          {StAddress}")
        print(f"                            {City + "," + " " + Prov + "," + " " + PostCode}")
        print(f" Phone:                     {EmployeePhone}")
        print()
        print(f" License Number:            {LicenseNum:<10s}")
        print(f" License Expiry Date:       {FV.FDateM(LicenseExpiryDate):<10s}")
        print(f" Insurance Policy Number:   {PolicyNumber}")
        print()
        print(f"-----------------------------------------------------------")
        print()
        if CarType == "O":
            TypeOfCar = "Own"
        else:
            TypeOfCar = "Rented"
        print(f" Car Type: {TypeOfCar:<6s}           Monthly Stand Fee: {FV.FDollar2(MonthlyFee):>10s}")
        print(f" Number of Rental Days: {NumDays}   Total Rental Fee:  {FV.FDollar2(TotalRentalFee):>10s}")
        print(f"                            HST:               {FV.FDollar2(HST):>10s}")
        print(f"----------------------------------------------------------")
        print(f"                            Total Fee:         {FV.FDollar2(TotalFee):>10s}")
        print(f"----------------------------------------------------------")
        

        # Write the employee details to a file called Employee.dat
        for _ in range(5):  # Change to control no. of 'blinks'
            print('Saving employee data ...', end='\r')
            time.sleep(.3)  # To create the blinking effect
            sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
            time.sleep(.3)
        
        f = open('Employee.dat', 'a')

        f.write("{}, ".format(str(NEXT_DRIVER_NUMBER -1)))
        f.write("{}, ".format(str(EmployeeName)))
        f.write("{}, ".format(str(EmployeeAdd)))
        f.write("{}, ".format(str(EmployeePhone)))
        f.write("{}, ".format(str(LicenseNum)))
        f.write("{}, ".format(FV.FDateM(LicenseExpiryDate)))
        f.write("{}, ".format(str(InsuranceCompany)))
        f.write("{}, ".format(str(PolicyNumber)))
        f.write("{}, ".format(str(CarType)))
        f.write("{}, ".format(str(MonthlyFee)))
        f.write("{}, ".format(str(TotalRentalFee)))
        f.write("{}\n".format(str(BalDue)))
    
        f.close()

        print()
        print("Employee data successfully saved ...", end='\r')
        time.sleep(1)  # To create the blinking effect
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns

        Continue = input("Do you want to proceed with another policy (Y/N): ").capitalize()
        if Continue == "Y":
            print("You are all set to enter new driver's details.")
            print()
        else:
            break

    # Write updated values back to Defaults.dat
    WriteDefaults(NEXT_TRANSACTION_NUMBER, NEXT_DRIVER_NUMBER, MONTHLY_STAND_FEE, DAILY_RENTAL_FEE, WEEKLY_RENTAL_FEE, HST_RATE)
        

def EnterCompanyRevenue():
    pass

def EnterCompanyExpense():
    pass

def TrackCarRentals():
    while True:
        RentalId = input("Please enter the rental Id: ")
        DriverNumber = input("Please enter the driver number: ")
        StartDate = input("Please enter the start date: ")

        break

def RecordEmployeePayment():
    while True:
        f = open('Payments.dat', 'a')
        # Read the last car ID from the file
        with open("Payments.dat", 'r') as file:
            lines = file.readlines()
            print(lines)
            # this is the last line and the first entry with index 0 (the carID)
            last_payment_Id = lines[-1].split()[0]
            # add 1 to the latest carID to make it the new car id then turn it to a string
            new_payment_Id = str(int(last_payment_Id) + 1)

        DriverNumber = input("Please enter the driver number: ")
        while True:
            try:
                PaymentDate = input("Enter payment date (YYYY-MM-DD): ")
                PaymentDate = datetime.datetime.strptime(PaymentDate, "%Y-%m-%d")
            except:
                print("Data Entry Error - Payment date is not in a valid format.")
            else:
                break
        PaymentAmount = float(input("Please enter the payment amount: "))
        paymentReason = input("Please enter the reason for payment: ")
        PaymentMethod = input("Please enter the payment method (Cash, Debit, or Visa): ")

        with open("Payments.dat", 'a') as file:
            file.write(f"{new_payment_Id} {DriverNumber} {PaymentDate} {PaymentAmount} {paymentReason} {PaymentMethod}\n")
        
        print()
        print("Payment record successfully saved ...", end='\r')
        time.sleep(1)  # To create the blinking effect
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
        f.close()

        Continue = input("Would you like to record another payment (Y/N): ").upper()
        if Continue == "Y":
            print("You are all set to enter new payment details.")
            print()
        else:
            break
        

def PrintCompanyProfitListing():
    print("-------------------------------------------------------------------------------------")
    print("               HAB Taxi Services Profit Listing Report          ")
    print("-------------------------------------------------------------------------------------")
    print(" Start Date: XX-XX-XXXX                                        End Date: XX-XX-XXXX  ")
    print("-------------------------------------------------------------------------------------")
    print()
    print("                                         Revenues")
    print(" Transaction    Transaction     Transaction     Transaction       HST        Total  ")
    print("     ID	          Date	         Amount	       Description  ")
    print("-------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------")
    print("Total Renenues:")
    print("-------------------------------------------------------------------------------------")
    print()
    print()
    print("                                         Revenues")
    print(" Invoice      Transaction     Transaction       Transaction       HST        Total  ")
    print("    ID	          Date	         Amount	       Description  ")
    print("-------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------")
    print("Total Expenses:")
    print("-------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------")
    print("Profit (Loss):")
    print("-------------------------------------------------------------------------------------")
    
def PrintDriverFinancialListing():
    pass

def PrintCompanyCarsReport():
    while True:
        f = open('CompanyCars.dat', 'a')
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
            f.close()  
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

