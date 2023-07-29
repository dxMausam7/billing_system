import datetime


def fun(Name, phone_number, Email, Address, Laptop_Sold):
    total = 0
    shipping_cost = 500
    for i in Laptop_Sold:
        total += int(i[4])
    Grand_total = total + shipping_cost
    today_date_and_time = datetime.datetime.now()
    file = open(str(Name)+str(phone_number)+".txt", "w")
    file.write("\n")
    file.write("\t\t\t\t Shop Invoice \n")
    file.write("\n")
    file.write("\t\t Radhe Radhe Bhaktapur | Phone:95959595 \n ")
    file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------------\n")
    file.write("Details Of Laptops:\n")
    file.write("-----------------------------------------------------------------------------------------------------\n")
    file.write("Name of the Customer:"+str(Name)+"\n")
    file.write("Contact Number:"+str(phone_number)+"\n")
    file.write("Email:"+str(Email)+"\n")
    file.write("Address:"+str(Address)+"\n")
    file.write("Date and time of purchase" +str(today_date_and_time)+"\n")
    file.write( "------------------------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Purchase Details are:\n")
    file.write( "--------------------------------------------------------------------------------------------------------\n")
    file.write("Item Name \t\t\t    Brand \t\t\t   Total Quantity \t\t   Unit Price \t\t\  Total\n")
    file.write("----------------------------------------------------------------------------------------------------------\n")
    for i in Laptop_Sold:
        file.write(str(i[0])+"\t\t\t"+str(i[1]) +"\t\t\t"+str(i[2])+"\t\t\t"+"$"+str(i[3])+"\t\t\t"+str(i[4])+"\n")
    file.write("--------------------------------------------------------------------------------------------------------\n")
    file.write("Your shipping cost is:" +str(shipping_cost)+"\n")
    file.write("Grand Total:"+str(Grand_total)+"\n")
    file.close()
    
def Manu_f(Name, phone_number, Email, Address, Laptop_Purchase):
    total = 0
    today_date_and_time = datetime.datetime.now()
    VAT = 0.13
    for i in Laptop_Purchase:
        total += int(i[4])
    Vat_AMT = VAT*total
    Grand_total = total + Vat_AMT
    today_date_and_time = datetime.datetime.now()
    file = open(str(Name)+str(phone_number)+".txt", "w")
    file.write("\n")
    file.write("\t\t\t\t Shop Invoice \n")
    file.write("\n")
    file.write("\t\t Radhe Radhe, Bahktapur | Phone:95959595 \n ")
    file.write("\n")
    file.write("-----------------------------------------------------------------------------------------------------\n")
    file.write("Details Of Laptops:\n")
    file.write("-----------------------------------------------------------------------------------------------------\n")
    file.write("Name of the Customer:"+str(Name)+"\n")
    file.write("Contact Number:"+str(phone_number)+"\n")
    file.write("Date and time of purchase" +str(today_date_and_time)+"\n")
    file.write("Email:"+str(Email)+"\n")
    file.write("Address:"+str(Address)+"\n")
        
    file.write("------------------------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Purchase Details are:\n")
    file.write("--------------------------------------------------------------------------------------------------------\n")
    file.write("Item Name \t\t Brand \t\t Total Quantity \t\t Unit Price \t\t\t Total\n")
    file.write("----------------------------------------------------------------------------------------------------------\n")
    for i in Laptop_Purchase:
         file.write(str(i[0])+"\t\t\t"+str(i[1]) +"\t\t\t"+str(i[2])+"\t\t\t"+"$"+str(i[3])+"\t\t\t"+str(i[4])+"\n")
    file.write("--------------------------------------------------------------------------------------------------------\n")
    file.write("Your Vat amt is:"+str(Vat_AMT)+"\n")
    file.write("Grand Total:"+str(Grand_total)+"\n")
    file.close()


# update stock for Customers
def update_stock(hi):
    file = open("Laptop_info.txt", "w")
    for values in hi.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()

#update stcok for manufacture
def update_stock_manu(hi):
    file = open("Laptop_info.txt", "w")
    for values in hi.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()
