#Function for storing the laptop date
def LaptopData():    
    file = open("Laptop_info.txt","r")
    laptop_data = {}
    laptop_SN = 1
    for data in file:
        data = data.replace("\n","")
        laptop_data.update({laptop_SN:data.split(",")})#indside a dictionary the ID also has its data list
        laptop_SN= laptop_SN + 1
    file.close()
    return laptop_data



def LaptopData_Table():
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("SN \t\t Laptop Name             Brand                  Price\t       Quantity        Processor           Graphic Card")
    print("-----------------------------------------------------------------------------------------------------------------------------------")

    #Displaying the laptop data 
    file = open("Laptop_info.txt","r")
    Laptop_SN= 1
    for data in file:
        print(Laptop_SN, "\t\t"+data.replace(",","\t\t"))
        Laptop_SN = Laptop_SN + 1
        print("---------------------------------------------------------------------------------------------------------------------------------")    
    file.close()
    print("\n")




