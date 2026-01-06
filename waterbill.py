# Gathering user values

continuation = False
customer_code = str(input("Enter customer code (R, C, or I) "))
if (customer_code == "R") or (customer_code == "C") or (customer_code == "I"):
    beginning_meter = int(input("Enter beginning reading (between 0 and 999999999) "))
    ending_meter = int(input("Enter ending reading (between 0 and 999999999) "))
    if (beginning_meter < 0) or (beginning_meter > 999999999) or (ending_meter < 0) or (ending_meter > 999999999):
        print("Invalid input (beginning or ending reading value is out of the range)")
    else:
        continuation = True
else:
    print("Invalid input:", customer_code)
    
if continuation == True:
    