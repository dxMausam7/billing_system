import datetime

#first display message
def display():
    """
    This fucntion is used to display the first title of the Laptop shop
    """
    print("\n\n")
    print("\t\t\t\t\t\t\t\t****THE DX_Daonzen Electronics ****")
    print("\t\t\t\t\t\t\t\t------------------------------------")
    print("\n\n")
    

def options():
    """
    Displaying options to the User to select
    """ 
    print("\n\n")
    print("Enter 1 to sell to customer")
    print("Enter 2 to Purchase from manufacturer")
    print("Enter 3 to Exit")
    print("\n\n")
    
def Inputs():
    """
    This functions take the user customers details such as Name,phone number 

    Returns:
        _type_: Name, phone_number, Email, Address
    """
    Name = input("Enter the Name:")
    phone_number = input("Enter your phone number:")
    Email = input("Enter your email:")
    Address = input("Enter your address:")
    return Name,phone_number,Email,Address



def Selling_Bill(Name, phone_number, Email, Address,Laptop_Sold):
    """
    Grenerates an invoice for the laptop sales and prints the output into the terminal

    Args:
        Name (String): Name of the customer 
        phone_number (String): Phone number of the customer 
        Email (String): Email address of the customer 
        Address (String): Address of the customer 
        Laptop_Sold (A list of List): contains the details of the laptop data sold.
                                        Each sublist contains:
                                        -Item Name
                                        -Brand 
                                        -Total Quantity
                                        -Unit price 
                                        -Total 
    """             
    total = 0
    shipping_cost = 500
    for i in Laptop_Sold:
        total += int(i[4])
    Grand_total = total + shipping_cost
    today_date_and_time = datetime.datetime.now()
    print(today_date_and_time)
    print("\n")
    print("\t\t\t\t SHOP INVOICE")
    print("\n\n")
    print("\t\t Radhe Radhe , Bhaktapur | Phone No: 9842942875")
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("                   Details Of Laptops:")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("  Name of the Customer:"+str(Name ))
    print("  Phone Number:"+str(phone_number))
    print("  Address:"+str(Address))
    print("  Email:"+str(Email))
    print("  Date and time of purchase" + str(today_date_and_time)+"\n")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("                   Purchase Details are:")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("Item Name\t\t Brand \t\t Total Quantity \t\t Unit Price \t\t\t Total ")
    print("-----------------------------------------------------------------------------------------------------------------------")
    for i in Laptop_Sold:
        print(i[0], "\t\t",i[1],"\t\t",i[2],"\t\t\t",i[3],"\t\t\t","$",i[4])
    print("-----------------------------------------------------------------------------------------------------------------------")
    print(" Your shipping cost is:", shipping_cost)
    print(" Grand Total:"+str(Grand_total))
    

def Bill_Print(Name, phone_number, Email, Address, Laptop_Purchase):
    """
    This program generates a shop invoice for laptop purchase.
    Uses: 
    The program calculates the total price of the purchase and add a Vat amount of 13% to it 
    The program genetrates an inovice fo the purchase including a list of purchase items and their details.
    The invoice also includes the VAT amount and the grand total including VAT and prints it. 
    Args:
        Name (String ): Name of manufacturer 
        phone_number (String): Phone of manufacturer 
        Email (String): Email of the manufacturer 
        Address (Satring): Address of the manufacturer
        Laptop_Purchase (List): A list containing details of purcahse laptops such as name, brand, total quantyity, unit price, and total
        No return type
    """
    total = 0
    today_date_and_time = datetime.datetime.now()
    VAT = 0.13
    for i in Laptop_Purchase:
        total += int(i[4])
    Vat_AMT = VAT*total
    Grand_total = total + Vat_AMT
    today_date_and_time = datetime.datetime.now()
    print(today_date_and_time)
    print("\n")
    print("\t\t\t\t SHOP INVOICE")
    print("\n\n")
    print("\t\t Radhe Radhe , Bahaktapur  | Phone No: 9842942875")
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("                         Details Of Laptops:")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print(" Name of the Manufacture:"+str(Name))
    print(" Contact Number:"+str(phone_number))
    print(" Eamil:"+str(Email))
    print(" Address:"+str(Address))
    print(" Date and time of purchase" +str(today_date_and_time)+"\n")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("     Purchase Details are:")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("Item Name\t\t Brand \t\t Total Quantity \t\t Unit Price \t\t\t Total ")
    print("-----------------------------------------------------------------------------------------------------------------------")
    for i in Laptop_Purchase:
        print(i[0], "\t\t",i[1],"\t\t",i[2],"\t\t\t",i[3],"\t\t\t","$",i[4])
    print("-----------------------------------------------------------------------------------------------------------------------")
    print(" Your Vat amount   is:", Vat_AMT)
    print(" Grand Total:"+str(Grand_total))




    
    
#validating the ID 
def validate_id(hi):
    """
    This function Validates the user-provided laptop ID.
    Args:
        hi (List): A list of laptop details

    Returns:
        int: The validateted Laptop ID 
    """
    b=True
    while b==True:
        try:
            Laptop_ID = int(input("Please provide id:"))
            b=False
        except:
            print("Invalid Input.Please enter an integer")
    while Laptop_ID <=0 or Laptop_ID >len(hi):
        print("Please provide the valid laptop id !!!")
        print("\n")
        Laptop_ID= int(input("Please provide valid :"))
    return Laptop_ID 

#Validating the quantity 
def User_quantity(Get_Quantity_of_selected_Laptop):
    """
    Ask the user to provide the quantity if the laptop they want to buy and validate the input.
    Returns:
        int: The validate quantity of the laptop the user wants to Sell
    """
    c=True
    while c==True:
        try:
            User_Quantity = int(input("please provid the number if the quantity of the Laptop you want to Sell:"))
            c=False
        except:
            print("Invalid Input.Please enter an integer")
    while User_Quantity <=0 or User_Quantity > int(Get_Quantity_of_selected_Laptop):
        print("Invaldi Quantity Selection, Plaease provide the valid quantity !!")
        print("\n")
        User_Quantity = int(input("please provid the number if the quantity of the Laptop you want to Sell:"))
        print("\n")
    return User_Quantity


#Validate id 
def Manu_Vlidate_ID(hi):
    """
    The validate_id function takes a list of laptops 'hi' and prompts the users to input the ID of the laptop they want to buy.
    It then validates the input to ensyre that the ID entered is withine the range of valid IDs in the lsit 'hi'. if the input is invalid,
    the function prompts the user to provide a valid input.
    Args:
        hi (List): A list of Laptops

    Returns:
        int: _description_
    """
    d=True
    while d== True:
        try:
            Laptop_ID = int(input("Please provide ID of the laptop you want to buy:"))
            d=False
        except:
            print("Invalid Input.Please enter an integer")
    while Laptop_ID <=0 or Laptop_ID >len(hi):
        print("Please provide the valid laptop id !!!")
        print("\n")
        Laptop_ID= int(input("Please provide valid:"))
    return Laptop_ID



def Man_validate_quantity():
    """_summary_

    Returns:
        _type_: _description_
    """
    e=True
    while e==True:
        try:
            User_Quantity = int(input("please provid the number if the quantity of the Laptop you want to buy:"))
            e=False
        except:
            print("Invalid Input.Please enter an integer")
    while User_Quantity <=0:
        print ("Invaldi Quantity Selection, Plaease provide the valid quantity !! ")
        print("\n")
        User_Quantity = int(input("please provid the number if the quantity of the Laptop you want to buy:"))
        print("\n")
    return User_Quantity




        

    

    

