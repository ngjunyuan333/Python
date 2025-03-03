Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
## Jun yuan
from datetime import date, timedelta

def register():
    Staff_ID = input("Enter a Staff ID:")
    Staff_Name = input("Enter a Staff name:")
    Role_list = ['Manager', 'Customer Service Staff I', 'Customer Service Staff II', 'Car Service Staff']
    Staff_Role = input("Choose role as Manager=1, Customer Service Staff I=2, Customer Service Staff II=3, Car Service Staff=4:")
    Staff_Role = int(Staff_Role) - 1
    if int(Staff_Role)>3:
          print("Invalid Staff role, please try again.")
          register()
    elif int(Staff_Role)<0:
          print("Invalid Staff role, please try again.")
          register()
    else:
      Staff_Role = Role_list[Staff_Role] 
    Password = input("Create password:")
    Date_of_register = date.today()

    staff_record = {
        "Staff ID": Staff_ID,
        "Staff Name": Staff_Name,
        "Staff Role": Staff_Role,
        "Password": Password,
        "Register Date": Date_of_register.strftime("%Y-%m-%d")
    }
    
    with open("Staff_record.txt", "a") as db:
        db.write(str(staff_record) + "\n")
    print("Staff created successfully! Please login to proceed.")


##Hui an
def _init_(self, starting_id='10001'):
        self.last_id = int(starting_id)

def generate_customer_id(self):
        new_id = 'C' + str(self.last_id).zfill(5)
        self.last_id += 1
        return new_id
    
def init():
        Customer_ID = new_id
        Customer_Name = input("Please Enter Your Name:")
        Customer_NRIC = input(int("Please Enter Your NRIC(Malaysian), example: xxxxxx-xx-xxxx. :"))
        Customer_PassportNo = input(int("Please Enter Your Passport Number(Foreigner Only), example: PA1234567890X. :"))
        Customer_LicenseNo = input(int("Please Enter Your Car Dring License Number, example: D12345678. :"))
        Customer_Address = input("Please Enter Your Address:")
        Customer_PhoneNo = input(int("Please Enter A Valid Phone Number, example: 011-41237894. :"))
        Others_info = input("Do let us know if there is other information:")
        Customer_Password = input("Please Create A Password:")
        Registration_Date = date.today()

        Customer_Record = {
            "Custmomer ID": Customer_ID,
            "Custmomer Name": Customer_Name,
            "Custmomer NRIC": Customer_NRIC,
            "Custmomer Passport Number": Customer_PassportNo,
            "Custmomer Car Driving License Number": Customer_LicenseNo,
            "Custmomer Contact Address": Customer_Address,
            "Custmomer Phone Number": Customer_PhoneNo,
            "Custmomer Additional Information": Others_info,
            "Custmomer Password": Customer_Password,
            "Custmomer Registration_Date": Registration_Date.stfrtime("%Y-%m-%d")
        }

        with open("customer_record.txt", "a") as db:
            db.write(str(customer_record) + "\n")
        print("Customer register successful! Thank you.")

def login_I():
    Username = input("Please Enter Your Username: ")
    Password = input("Please Enter Your Password: ")
    attempts = 1

    with open("customer_record.txt","r") as db:
        for line in db:
            Username= input("Please Enter Your Username: ")
            Password= input("Please Enter Your Password: ")
             
            if username == correct_username and correct_password:
                print("Login Succesful, Welcome!")
                break
            else:
                print("Incorrect Username or Password. Please try again.")
                attempts += 1 
            if attempts == 3:
                print("Maximum Login Attempts Reached. Please Try Again.")

def cus_main():
    while True: 
            print("Welcome!")
            print("1. Custoner login")
            print("2. Register new customer")
            print("3. Exit")
            choice = input("Please Enter Your Choice.")

            if choice == "1":
                login_I() 
            elif choice == "2":
                init()
            elif choice == "3":
                print("Goodbye!")
            break
    else:
        print("Invalid choice. Please try again.")

## NG WEI JIAN
# View rental transactions
def view_transactions_by_date(rentals, view_date):
    transactions = [rental for rental in rentals if rental["rental_date"].date() == view_date.date()]
    if transactions:
        for i, transaction in enumerate(transactions, 1):
            print(f"Transaction {i}:")
            print("Car Registration Number:", transaction["car"]["reg_number"])
            print("Customer ID:", transaction["customer_id"])
            print("Rental Date:", transaction["rental_date"].strftime("%d %B %Y"))
            print("Return Date:", transaction["return_date"].strftime("%d %B %Y"))
            print("Rental Periods (Days):", transaction["rental_period"])
            print("Total Rental: ${:.2f}".format(transaction["total_rental"]))
            print()
    else:
        print("No transactions found for the given date.")

# Cancel rental transaction
def cancel_transaction(rentals, transaction_number):
    if 1 <= transaction_number <= len(rentals):
        canceled_transaction = rentals.pop(transaction_number - 1)
        canceled_transaction["car"]["rental_status"] = "Available"  # Update car status to available
        print("Transaction canceled successfully.")
        return True
    else:
        print("Transaction not found.")
        return False

# Load from file
def load_rental_data(filename):
    rentals = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if lines[i].strip() == "Rentals:":
                    i += 1
                    while i < len(lines):
                        if lines[i].strip() == "":
                            i += 1
                            continue
                        rental = {
                            "car": {"reg_number": lines[i].strip().split(": ")[1]},
                            "customer_id": lines[i+1].strip().split(": ")[1],
                            "rental_date": datetime.strptime(lines[i+2].strip().split(": ")[1], "%d %B %Y"),
                            "return_date": datetime.strptime(lines[i+3].strip().split(": ")[1], "%d %B %Y"),
                            "rental_period": int(lines[i+4].strip().split(": ")[1]),
                            "total_rental": float(lines[i+5].strip().split(": $")[1])
                        }
                        rentals.append(rental)
                        i += 6
                else:
                    i += 1
    except FileNotFoundError:
        print("No rental data file found. Starting with empty rental list.")
    return rentals

# Save to file
def save_to_file(rentals, filename):
    with open(filename, 'w') as file:
        file.write("Rentals:\n")
        for rental in rentals:
            file.write("Car Registration Number: {}\n".format(rental["car"]["reg_number"]))
            file.write("Customer ID: {}\n".format(rental["customer_id"]))
            file.write("Rental Date: {}\n".format(rental["rental_date"].strftime("%d %B %Y")))
            file.write("Return Date: {}\n".format(rental["return_date"].strftime("%d %B %Y")))
            file.write("Rental Periods (Days): {}\n".format(rental["rental_period"]))
            file.write("Total Rental: ${:.2f}\n".format(rental["total_rental"]))
            file.write("\n")

def rent_car_process(cars, rentals):
    # Get customer input for rental dates
    rental_date_str = input("Enter rental date (YYYY-MM-DD): ")
    return_date_str = input("Enter return date (YYYY-MM-DD): ")

    rental_date = datetime.strptime(rental_date_str, "%Y-%m-%d")
    return_date = datetime.strptime(return_date_str, "%Y-%m-%d")

    print("Available Cars for Rent:")
    for i, car in enumerate(cars, 1):
        status = "Reserved" if car["rental_status"] == "Reserved" else "Available"
        print(f"{i}. {car['make']} {car['model']} - ${car['daily_rate']} per day (Status: {status})")

    # Car selection
    while True:
        try:
            car_choice = int(input("Enter the number of the car you want to rent: "))
            if 1 <= car_choice <= len(cars):
                selected_car_index = car_choice - 1
                if cars[selected_car_index]["rental_status"] == "Reserved":
                    print("Selected car is reserved and cannot be rented at the moment.")
                else:
                    break
            else:
                print("Invalid car choice. Please enter a number between 1 and {}.".format(len(cars)))
        except ValueError:
            print("Invalid input. Please enter a number.")

    customer_id = input("Enter customer id")
    rental_transaction = rent_car(cars, rentals, selected_car_index, rental_date, return_date, customer_id)

    if rental_transaction:
        print("Rental Transaction Details:")
        print("Car Registration Number:", rental_transaction["car"]["reg_number"])
        print("Customer ID:", customer_id)
        print("Rental Date:", rental_transaction["rental_date"].strftime("%d %B %Y"))
        print("Return Date:", rental_transaction["return_date"].strftime("%d %B %Y"))
        print("Rental Periods (Days):", rental_transaction["rental_period"])
        print("Total Rental: ${:.2f}".format(rental_transaction["total_rental"]))

        save_to_file(rentals, "CustomerService2.txt")

# View transactions
def view_transactions_process(rentals):
    view_date_str = input("Enter date to view rental transactions (YYYY-MM-DD): ")
    view_date = datetime.strptime(view_date_str, "%Y-%m-%d")
    print("Rental Transactions on {}: ".format(view_date.strftime("%d %B %Y")))
    view_transactions_by_date(rentals, view_date)

# Cancel transaction
def cancel_transaction_process(rentals):
    view_transactions_process(rentals)
    cancel_index = int(input("Enter the number of the transaction you want to cancel: "))
    if cancel_transaction(rentals, cancel_index):
        print("\nUpdated Rental Transactions:")
        view_transactions_by_date(rentals, datetime.now())  # Display updated list of transactions
        save_to_file(rentals, "CustomerService2.txt")

# Add new car to system

def add_car(cars, make, model, daily_rate, reg_number):
    car = {
        "make": make,
        "model": model,
        "daily_rate": daily_rate,
        "reg_number": reg_number,
        "rental_status": "Available"
    }
    cars.append(car)

# Rent car
def rent_car(cars, rentals, car_index, rental_date, return_date, Customer_ID):
    car = cars[car_index]
    if car["rental_status"] == "Reserved":
        print("Car is reserved and cannot be rented at the moment.")
        return None
    elif car["rental_status"] == "Available":
        car["rental_status"] = "Reserved"  # Update car status to reserved
        rental_period = (return_date - rental_date).days
        total_rental = car["daily_rate"] * rental_period
        rental = {
            "car": car,
            "customer_id": Customer_ID,
            "rental_date": rental_date,
            "return_date": return_date,
            "rental_period": rental_period,
            "total_rental": total_rental
        }
        rentals.append(rental)
        return rental
    else:
        print("Car is not available for rental.")
        return None

# Return rented car
def return_car(cars, rentals, car_index):
    car = cars[car_index]
    for rental in rentals:
        if rental["car"] == car:
            car["rental_status"] = "Available"
            rentals.remove(rental)
            return rental
    print("Car was not rented out.")
    return None


def car_main():
    cars = []
    rentals = load_rental_data("CustomerService2.txt")

    # Car details
    add_car(cars, "Toyota", "Camry", 50, "KV1234E")
    add_car(cars, "Honda", "Accord", 60, "AB5678F")
    add_car(cars, "Ford", "Explorer", 70, "CD91011G")
    add_car(cars, "Chevrolet", "Malibu", 55, "EF121314H")
    add_car(cars, "Tesla", "Model S", 100, "GH151617I")

    while True:
        print("\n1. Rent a Car")
        print("2. View Rental Transactions by Date")
        print("3. Cancel a Rental Transaction")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            rent_car_process(cars, rentals)
        elif choice == "2":
            view_transactions_process(rentals)
        elif choice == "3":
            cancel_transaction_process(rentals)
        elif choice == "4":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


##Eric
##Eric
import re

# Create an empty text file for car_database
car_db_file = "car_database.txt"
with open(car_db_file, "w") as file:
    pass  # Nothing to write, just creating the file

car_database = {} 

# Function to validate date format (mm/dd/yyyy)
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%m/%d/%Y')
        return True
    except ValueError:
        return False

# Specify the file path where you want to write the JSON data
file_path = "Car_Database.txt"

import re

# Function to check if a given plate is a valid Malaysian plate
def is_valid_malaysian_plate(plate: str) -> bool:
    return re.fullmatch(r'[A-Z]{1,3}\d{1,4}[A-Z]{0,1}', plate) is not None

from datetime import datetime

# Function to check if a date string is in a valid format
def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%m/%d/%Y")
        return True
    except ValueError:
        return False

# Function for registering a car
def register_car():
    print("\nRegister Car")
    car_plate_no = input("Enter Car Plate Number: ")
    if not is_valid_malaysian_plate(car_plate_no):
        print("Invalid Malaysian car plate format. Please enter a valid plate number.")
        return
    if car_plate_no in car_database:
        print("Car Plate Number already exists. Please choose another one.")
        return
    manufacturer = input("Enter Car Manufacturer: ")
    
    # Validate Year of Manufacture
    while True:
        year_of_manufacture = input("Enter Year of Manufacture (YYYY): ")
        if not year_of_manufacture.isdigit() or len(year_of_manufacture) != 4:
            print("Invalid input. Please enter a valid year (YYYY).")
        else:
            break

    # Validate Seating Capacity
    while True:
        seating_capacity = input("Enter Seating Capacity: ")
        if not seating_capacity.isdigit():
            print("Invalid input. Seating capacity must be a number.")
        else:
            break

    # Validate Last Service Date
    while True:
        last_service_date = input("Enter Last Service Date (mm/dd/yyyy): ")
        if not is_valid_date(last_service_date):
            print("Invalid input. Please enter a valid date in mm/dd/yyyy format.")
        else:
            last_service_datetime = datetime.strptime(last_service_date, "%m/%d/%Y")
            manufacture_year_datetime = datetime.strptime(year_of_manufacture, "%Y")
            if last_service_datetime.year < manufacture_year_datetime.year:
                print("Last Service Date cannot be before the Year of Manufacture.")
            else:
                break

    # Validate Insurance Expiry Date
    while True:
        insurance_expiry_date = input("Enter Insurance Expiry Date (mm/dd/yyyy): ")
        if not is_valid_date(insurance_expiry_date):
            print("Invalid input. Please enter a valid date in mm/dd/yyyy format.")
        else:
            insurance_expiry_datetime = datetime.strptime(insurance_expiry_date, "%m/%d/%Y")
            if insurance_expiry_datetime.year < manufacture_year_datetime.year:
                print("Insurance Expiry Date cannot be before the Year of Manufacture.")
            else:
                break

    # Validate Road Tax Expiry Date
    while True:
        road_tax_expiry = input("Enter Road Tax Expiry Date (mm/dd/yyyy): ")
        if not is_valid_date(road_tax_expiry):
            print("Invalid input. Please enter a valid date in mm/dd/yyyy format.")
        else:
            road_tax_expiry_datetime = datetime.strptime(road_tax_expiry, "%m/%d/%Y")
            if road_tax_expiry_datetime.year < manufacture_year_datetime.year:
                print("Road Tax Expiry Date cannot be before the Year of Manufacture.")
            else:
                break
            
    # Add Policy Number
    policy_number = input("Enter Policy Number: ")

    car_database[car_plate_no] = {
        "Manufacturer": manufacturer,
        "Year of Manufacture": year_of_manufacture,
        "Seating Capacity": seating_capacity,
        "Last Service Date": last_service_date,
        "Insurance Expiry Date": insurance_expiry_date,
        "Road Tax Expiry": road_tax_expiry,
        "Policy Number": policy_number
    }

    # Write the car data to the "Car_Database.txt" file
    with open("Car_Database.txt", "a") as car_file:
        car_file.write(f"{car_plate_no},{manufacturer},{year_of_manufacture},{seating_capacity},{last_service_date},{insurance_expiry_date},{road_tax_expiry},{policy_number}\n")
    
    print("Car registration successful!")

# Function for updating car information
def update_car():
    while True:
        print("\nUpdate Car Information")
        car_plate_no = input("Enter Car Plate Number to update: ")
        if car_plate_no in car_database:
            print("Select the field to update:")
            print("1. Insurance Policy Number")
            print("2. Insurance Expiry Date")
            print("3. Road Tax Expiry Date")
            print("4. Car Renting Rate per day")
            print("5. Rental Availability")
            print("6. Last Service Date")
            print("7. Requested Date (for Reserved)")
            print("8. Request Day Rented and Returning Date (for Rented)")
            print("9. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                insurance_policy_no = input("Enter New Insurance Policy Number: ")
                car_database[car_plate_no]["Insurance Policy Number"] = insurance_policy_no
                print("Insurance Policy Number updated successfully!")
            elif choice == '2':
                insurance_expiry_date = input("Enter New Insurance Expiry Date: ")
                car_database[car_plate_no]["Insurance Expiry Date"] = insurance_expiry_date
                print("Insurance Expiry Date updated successfully!")
            elif choice == '3':
                road_tax_expiry = input("Enter New Road Tax Expiry Date: ")
                car_database[car_plate_no]["Road Tax Expiry"] = road_tax_expiry
                print("Road Tax Expiry Date updated successfully!")
            elif choice == '4':
                renting_rate = input("Enter New Car Renting Rate per day: ")
                car_database[car_plate_no]["Renting Rate"] = renting_rate
                print("Car Renting Rate per day updated successfully!")
            elif choice == '5':
                print("Select the Rental Availability:")
                print("1. Available")
                print("2. Requested Date (for Reserved)")
                print("3. Request Day Rented and Returning Date (for Rented)")
                print("4. Under Service")
                print("5. Disposed")
                availability_choice = input("Enter your choice: ")
                if availability_choice == '1':
                    car_database[car_plate_no]["Rental Availability"] = "Available"
                    print("Rental Availability updated to Available successfully!")
                elif availability_choice == '2':
                    requested_date = input("Enter Requested Date (for Reserved): ")
                    car_database[car_plate_no]["Rental Availability"] = "Requested Date: {}".format(requested_date)
                    print("Requested Date updated successfully!")
                elif availability_choice == '3':
                    rent_date = input("Enter Rent Date: ")
                    return_date = input("Enter Returning Date: ")
                    car_database[car_plate_no]["Rental Availability"] = "Request Day Rented: {}, Returning Date: {}".format(rent_date, return_date)
                    print("Request Day Rented and Returning Date updated successfully!")
                elif availability_choice == '4':
                    last_service_date = input("Enter New Last Service Date: ")
                    car_database[car_plate_no]["Rental Availability"] = "Under Service: {}".format(last_service_date)
                    print("Last Service Date updated successfully!")
                elif availability_choice == '5':
                    car_database[car_plate_no]["Rental Availability"] = "Disposed"
                    print("Rental Availability updated to Disposed successfully!")
                else:
                    print("Invalid choice. Please enter a number from 1 to 5.")
            elif choice == '6':
                last_service_date = input("Enter New Last Service Date: ")
                car_database[car_plate_no]["Last Service Date"] = last_service_date
                print("Last Service Date updated successfully!")
            elif choice == '7':
                requested_date = input("Enter Requested Date (for Reserved): ")
                car_database[car_plate_no]["Rental Availability"] = "Requested Date: {}".format(requested_date)
                print("Requested Date updated successfully!")
            elif choice == '8':
                rent_date = input("Enter Rent Date: ")
                return_date = input("Enter Returning Date: ")
                car_database[car_plate_no]["Rental Availability"] = "Request Day Rented: {}, Returning Date: {}".format(rent_date, return_date)
                print("Request Day Rented and Returning Date updated successfully!")
            elif choice == '9':
                user_menu()
            else:
                print("Invalid choice. Please enter a number from 1 to 8.")

           # Update the Car_Database.txt file
with open("Car_Database.txt", "w") as car_file:
    for car_plate_no, car_info in car_database.items():
        car_file.write(f"{car_plate_no},{car_info['Manufacturer']},{car_info['Year of Manufacture']},{car_info['Seating Capacity']},{car_info['Last Service Date']},{car_info['Insurance Policy Number']},{car_info['Insurance Expiry Date']},{car_info['Road Tax Expiry']},{car_info.get('Renting Rate', '')},{car_info.get('Rental Availability', '')}\n")

# Function for viewing car information
def view_car():
    print("\nView Car Information")

    # Read data from the Car_Database.txt file
    try:
        with open("Car_Database.txt", "r") as car_file:
            for line in car_file:
                car_data = line.strip().split(',')
                car_plate_no = car_data[0]
                manufacturer = car_data[1]
                year_of_manufacture = car_data[2]
                seating_capacity = car_data[3]
                last_service_date = car_data[4]
                insurance_policy_no = car_data[5]
                insurance_expiry_date = car_data[6]
                road_tax_expiry = car_data[7]
                renting_rate = car_data[8] if len(car_data) > 8 else "Not Available"
                rental_availability = car_data[9] if len(car_data) > 9 else "Not Available"
                
                print("Car Plate Number:", car_plate_no)
                print("Manufacturer:", manufacturer)
                print("Year of Manufacture:", year_of_manufacture)
                print("Seating Capacity:", seating_capacity)
                print("Last Service Date:", last_service_date)
                print("Insurance Policy Number:", insurance_policy_no)
                print("Insurance Expiry Date:", insurance_expiry_date)
                print("Road Tax Expiry:", road_tax_expiry)
                print("Renting Rate per day:", renting_rate)
                print("Rental Availability:", rental_availability)
                print()
    except FileNotFoundError:
        print("Car database file not found.")

# Function for deleting a car
def delete_car():
    print("\nDelete Car")
    car_plate_no = input("Enter Car Plate Number to delete: ")
    if car_plate_no in car_database:
        if car_database[car_plate_no].get("Rental Availability") == "Disposed":
            del car_database[car_plate_no]
            print("Car '{}' deleted successfully!".format(car_plate_no))
        else:
            print("Car '{}' cannot be deleted because it is not in 'Disposed' status.".format(car_plate_no))

        # Update the Car_Database.txt file
        with open("Car_Database.txt", "w") as car_file:
            for car_plate, car_info in car_database.items():
                car_file.write(f"{car_plate},{car_info['Manufacturer']},{car_info['Year of Manufacture']},{car_info['Seating Capacity']},{car_info['Last Service Date']},{car_info['Insurance Policy Number']},{car_info['Insurance Expiry Date']},{car_info['Road Tax Expiry']},{car_info.get('Renting Rate', '')},{car_info.get('Rental Availability', '')}\n")
    else:
        print("Car Plate Number not found.")

        
# Main function for user menu
def user_menu():
    while True:
        print("\nUser Menu:")
        print("1. Register Car")
        print("2. Update Car")
        print("3. View Car")
        print("4. Delete Car")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_car()
        elif choice == '2':
            update_car()
        elif choice == '3':
            view_car()
        elif choice == '4':
            delete_car()
        elif choice == '5':
            print("Logging out. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
... 
... ##jun yuan
... def login():
...     Staffname = input("Enter your Staff Name: ")
...     Password = input("Enter your Password: ")
... 
...     with open("Staff_record.txt", "r") as db:
...         for line in db:
...             record = eval(line)  # Convert the string representation of dictionary to actual dictionary
...             if record["Staff Name"] == Staffname and record["Password"] == Password:
...                 if record["Staff Role"] == 'Manager' :
...                     print("ongoing")
...                 elif record["Staff Role"] =='Customer Service Staff I':
...                     cus_main()
...                 elif record["Staff Role"] == 'Customer Service Staff II':
...                     car_main()
...                 elif record["Staff Role"] == 'Car Service Staff':
...                     user_menu()
...         return
...           
... def main(): 
...     while True:
...         print("1. Login")
...         print("2. Register")
...         print("3. Exit")
...         choice = input("Enter your choice: ")
... 
...         if choice == "1":
...             login()
...         elif choice == "2":
...             register()
...         elif choice == "3":
...             print("Goodbye!")
...             break
...     else:
...         print("Invalid choice. Please try again.")
... main()
