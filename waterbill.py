import math 
 
import random 
 
# Initializes global variables 
 
exit = False 
 
account_number = random.randint(1000, 9000) 
 
print("Welcome to the water bill calculation program. Exit whenever you want.") 
 
while not (exit == "N" or exit == "n"):  # Keeps user in the program until they exit 
    account_number = account_number + 1 
 
    # Initializes variables for every cycle 
 
    exit = False 
 
    usage_cost = 0 
 
    water_usage = 0 
 
    customer_code = "init" 
 
    beginning_meter = -1 
 
    ending_meter = -1 
 
    # Gathers user data 
 
    while ((customer_code == "R") or (customer_code == "C") or (customer_code == "I")) == False: 
 
        customer_code = str(input("Enter customer code (R, C, or I): ")) 
 
        if ((customer_code == "R") or (customer_code == "C") or (customer_code == "I")) == False: 
            print("Error, please enter a valid character such as R, C, or I.") 
 
    while (beginning_meter < 0) or (beginning_meter > 999999999) or (ending_meter < 0) or (ending_meter > 999999999): 
 
        beginning_meter = int(input("Enter beginning reading (between 0 and 999999999): ")) 
 
        ending_meter = int(input("Enter ending reading (between 0 and 999999999): ")) 
 
        if (beginning_meter < 0) or (beginning_meter > 999999999) or (ending_meter < 0) or (ending_meter > 999999999): 
            print("Error, please enter a valid number between 0 and 999999999.") 
 
    customer_name = str(input("What is the customer's name? ")) 
 
    customer_phone = input("What is the customer's phone number? ") 
 
    customer_address = str(input("What is the customer's address? ")) 
 
    # Water usage calculations 
 
    if (ending_meter - beginning_meter) < 0: 
 
        water_usage = math.abs(ending_meter - beginning_meter)  # Calculates water usage from overflowing 
 
    else: 
 
        water_usage = (ending_meter - beginning_meter) * 0.1  # Calculates water usage regularly 
 
    if customer_code == "R": 
 
        usage_cost = (water_usage * 0.0005) + 5 
 
    elif customer_code == "C": 
 
        if water_usage <= 4.0E6: 
            usage_cost = 1000 
 
    elif water_usage > 4.0E6: 
 
        usage_cost = 1000 + ((water_usage - 4.0E6) * 0.00025) 
 
    elif customer_code == "I": 
 
        if water_usage <= 4.0E6: 
            usage_cost = 1000 
 
    elif water_usage > 4.0E6 and water_usage <= 10.0E6: 
 
        usage_cost = 2000 
 
    elif water_usage > 10.0E6: 
 
        usage_cost = 2000 + ((water_usage - 10.0E6) * 0.00025) 
 
        # Section for bill 
 
    print(f"\nWater Works Services" 
           
         f"\nName: {customer_name}" 
 
          f"\nPhone: {customer_phone}" 
 
          f"\nAddress: {customer_address}" 
 
          f"\nAccount number: {account_number}" 
 
          f"\nCustomer code: {customer_code}" 
 
          f"\nBeginning meter reading: {beginning_meter:09}" 
 
          f"\nEnding meter reading: {ending_meter:09}" 
 
          f"\nGallons of water used: {water_usage:0.1f}" 
 
          f"\nAmount billed: ${usage_cost:0.2f}") 
 
    # Exit process 
 
    while not (exit == "Y" or exit == "y" or exit == "N" or exit == "N"): 
 
        exit = str(input("\nDo you want to perform a new calculation? ")) 
 
        if not (exit == "Y" or exit == "y" or exit == "N"): 
            print("Error, please enter capital or lowercase Y or N.") 
 
print("Done.") 
