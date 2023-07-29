import datetime
from Read import*
from Functions import*
from Write import*


#Calling display function
Loop = True
while Loop == True:
    display()
    LaptopData_Table()
    options()
    #asking the user input
    a=True 
    while a== True:
        try:
            User_Input = int(input("Enter the operation to continue:"))
            a = False
        except ValueError:
            print("Invalid Input.Please enter an integer")
        
        print("\n\n")

    if User_Input== 1:
        print("----------------------------------------")
        print("To generate a bill, provide the details:")
        print("----------------------------------------")
        
        #Calling the users inputs fucntions 
        Name, phone_number, Email, Address = Inputs()


        Laptop_Sold = []# kine ko saman yetta bascah 
        More_Needed = True

        while More_Needed == True:
            LaptopData_Table()
            print ("\n")
            
#           #Validate ID
            hi = LaptopData()
            Laptop_ID1 = validate_id(hi)
          
            
            # to check if the stock is zerro or not
            if  int(hi[Laptop_ID1][3]) ==0:
                print("The product you are trying  to reach is out of stock !! ")
                display()
                LaptopData_Table()
                options()
                User_Input = int(input("Enter the operation to continue:"))
                continue
                
            else:
                Get_Quantity_of_selected_Laptop = LaptopData()[Laptop_ID1][3]
                quan = User_quantity(Get_Quantity_of_selected_Laptop)
#                #Validate Quantity
               
            
                    
                #Update stock  
                hi = LaptopData()
                hi[Laptop_ID1][3] = int(hi[Laptop_ID1][3]) - int(quan)
                update_stock(hi)
                
                #Getting users purchased items
                Product_Name= hi[Laptop_ID1][0]
                Quantity_Selected_By_User= quan
                Pric_of_item_selected = hi[Laptop_ID1][2].replace("$",'')
                Unit_Price = hi[Laptop_ID1][2]
                Brand_Name= hi[Laptop_ID1][1]
                total_Pric= int(Pric_of_item_selected)*int(Quantity_Selected_By_User)
                Laptop_Sold.append([Product_Name,Brand_Name,Quantity_Selected_By_User,Unit_Price,total_Pric])
                

                User_req = input("Do you wan to  continue (Y/N)").upper()
                if User_req=="Y":
                    More_Needed= True
                else:
                    #bill
                    #calling the Invoice printing function  
                    Selling_Bill(Name,phone_number,Email, Address, Laptop_Sold)
                    #calling the Invoic printing function in text file 
                    fun(Name, phone_number, Email, Address, Laptop_Sold)
                   

                    #date and time
                    #Bill number
                    More_Needed = False
                    display()
                    LaptopData_Table()
                    options()
                    User_Input = int(input("Enter the operation to continue:"))
                    Loop= True
                
                
                

    
    elif User_Input== 2:
        
        print("----------------------------------------")
        print("To generate a bill, provide the details:")
        print("----------------------------------------")

        Name = input("Enter the Manufacture details:")
        print("\n")

        phone_number = input("Enter your phone number:")
        print("\n")

        Email = input("Enter your email:")
        print ("\n")

        Address = input("Enter your address:")
        print ("\n")
        
        Laptop_Purchase = []
        More_Needed = True

        while More_Needed == True:
            LaptopData_Table()
            print ("\n")
            

           #Validate ID
            hi = LaptopData()
            Laptop_ID2 = Manu_Vlidate_ID(hi)
            
            #Validate quantity
            UserQuantity= Man_validate_quantity()
                   
            

            #Update stock
            hi= LaptopData()
            hi[Laptop_ID2][3] = int(hi[Laptop_ID2][3]) + int(UserQuantity)
            update_stock_manu(hi)
            

            #Getting users purchased items
            Product_Name= hi[Laptop_ID2][0]
            Quantity_Selected_By_User= UserQuantity
            Pric_of_item_selected = hi[Laptop_ID2][2].replace("$",'')
            Unit_Price = hi[Laptop_ID2][2]
            Brand_Name= hi[Laptop_ID2][1]
            total_Pric= int(Pric_of_item_selected)*int(Quantity_Selected_By_User)
            Laptop_Purchase.append([Product_Name,Brand_Name,Quantity_Selected_By_User,Unit_Price,total_Pric])

            #Asing user if he/she wants to further continue or not 
            User_req = input("Do you wan to  continue (Y) or press any key to print ").upper()
            if User_req=="Y":
                More_Needed= True
            else:
                #calling the Invoice printing function  
                Bill_Print(Name, phone_number, Email, Address, Laptop_Purchase)
                #calling the Invoic printing function in text file 
                Manu_f(Name, phone_number, Email, Address, Laptop_Purchase)
                
                
                More_Needed = False
                display()
                LaptopData_Table()
                options()
                User_Input = int(input("Enter the operation to continue:"))
                Loop= True
                
           
    elif User_Input== 3:
        Loop= False
        print("Thank you, Please visit Again !!")
        print("\n")
        
    else:
        print("Please enter the valid input")
        Loop = True
        
        



    
    
        
        

    
        
        
    
        


                            
            
           

        
                
            
            

        
            
            
            

        
        
        
        

        
        
        
    

