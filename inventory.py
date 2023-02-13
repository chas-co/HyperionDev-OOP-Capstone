


#========The beginning of the class==========
class Shoe:
    #define the clas constructor to initialise attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    #returns the cost of the shoe
    def get_cost(self):
        return self.cost
    #returns quantity of shoe
    def get_quantity(self):
        return self.quantity
    #returns string representation of shoe object
    def __str__(self):
        shoe_string = f"""
    ======product:{self.product}=======
        Country:    {self.country}
        Code:       {self.code}
        cost:       {self.cost}
        quantity:   {self.quantity}
        """
        return shoe_string

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
inventory = []
#==========Functions outside the class==============
def read_shoes_data():
    try:
        #open and read the content of the file
        with open("inventory.txt","r") as inv_file:
            inventory = inv_file.readlines()
            #remove the first line from out list
            inventory.pop(0)
        for item in inventory:
            #split the content of each line an create a shoe object for each line
            shoe = item.split(",")
            shoe_list.append(Shoe(shoe[0],shoe[1],shoe[2],float(shoe[3]),int(shoe[4])))
    except FileExistsError:
        print("The file you are trying to open does not exist")
    
    print("************Shoe Inventory Successfully Loaded************\n")
#captures new shoe object and updates the inventory
def capture_shoes():
    while True:
        try:
            country = input("Please Enter the country of the shoe\n")
            code = input("Please enter the shoe code\n")
            product = input("Please enter the product name\n")
            cost = int(input("Please enter the cost of the shoe\n"))
            quantity = int(input("Please enter the number of shoes in inventory\n"))
            break
        except ValueError:
            print("You have entered a wrong value please try again\n")
            continue
    #create new shoe object and add it to shoe list 
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    #update the inventory file as well.
    with open("inventory.txt","w") as inv_file:
        inv_file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            inv_file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.get_cost()},{shoe.get_quantity()}\n")

#displays all shoes in inventory
def view_all():
    if len(shoe_list) < 1:
        print("Your inventory has not been loaded.\nPlease Select option 1 on the menu to load inventory\n")
        return
    for shoe in shoe_list:
        print(shoe.__str__())
 

def re_stock():
    if len(shoe_list) < 1:
        print("Your inventory has not been loaded.\nPlease Select option 1 on the menu to load inventory\n")
        return
    #create a list and store shoe quantities in correspoding index
    quantity_list = []
    for shoe in shoe_list:
        quantity_list.append(shoe.get_quantity())

    #find the index with the minimum quantity
    low_stock = quantity_list.index(min(quantity_list))

    print (f"""
    This is the product with the lowest stock quantity
    {shoe_list[low_stock].__str__()}""")

    #ask for quantity of shoes to add to the current stock 
    while True:
        try:
            new_quantity = int(input("Enter the number of shoes you want to restock with\n"))
            break
        except ValueError:
            print("You must enter numbers only in this field")
            continue

    #update the quantity
    shoe_list[low_stock].quantity += new_quantity

    #update the inventory file
    with open("inventory.txt","w") as inv_file:
        inv_file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            inv_file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.get_cost()},{shoe.get_quantity()}\n")
    
  
def search_shoe():
    
    if len(shoe_list) < 1:
        print("Your inventory has not been loaded.\nPlease Select option 1 on the menu to load inventory\n")
        return
    while True:
        try:
            #request for product code for shoe search
            prod_code = input("Please enter the code of the product you want to search for:\n")
            code_list = []
            for shoe in shoe_list:
                code_list.append(shoe.code)
            #find index of the supplied product code return the shoe object
            shoe_index = code_list.index(prod_code)
            break
        except ValueError:
            print("please enter a valid product code\n")
            continue

    found_shoe = shoe_list[shoe_index]
    return found_shoe
   

def value_per_item():

    if len(shoe_list) < 1:
        print("Your inventory has not been loaded.\nPlease Select option 1 on the menu to load inventory\n")
        return
    value_list = []
    #calculate value of each shoe using the class methods in corresponding index
    for shoe in shoe_list:
        value_list.append(shoe.get_quantity() * shoe.get_cost())
    #print the index
    for i,value in enumerate(value_list):
        print(f"{shoe_list[i].__str__()}\n****TotalValue: £{value}****\n")

def highest_qty():
    if len(shoe_list) < 1:
        print("Your inventory has not been loaded.\nPlease Select option 1 on the menu to load inventory\n")
        return
    quantity_list = []
    #collect all shoe quantities in order into a new list
    for shoe in shoe_list:
        quantity_list.append(shoe.get_quantity())
    #find the index of highest quantity
    high_stock = quantity_list.index(max(quantity_list))
    sale_shoe = shoe_list[high_stock]

    #print the product and inform user that it is on sale
    print(f"""
    ======product:{sale_shoe.product}=======
        Country:    {sale_shoe.country}
        Code:       {sale_shoe.code}
        quanity:    {sale_shoe.get_quantity()}
        
    $$$$$$$This product is up for sale$$$$$$$\n""")



 

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

while True:
    while True:
        try:
            menu = int(input('''Select one of the following Options below:
            1. Read shoe data from file
            2. Capture new shoes
            3. View all shoes
            4. Restock shoe
            5. Search for a shoe
            6. Check value per item in stock
            7. Check product with highest quantity
            8. Exit\n'''))
            break
        except ValueError:
            print("Please try again select a number from the option\n")
            continue

    if menu == 1:
        read_shoes_data()
    elif menu == 2 :
        capture_shoes()
    elif menu == 3:
        view_all()
    elif menu == 4:
        re_stock()
    elif menu == 5:
       found_shoe = search_shoe()
       print(found_shoe.__str__())
    elif menu == 6:
        value_per_item()
    elif menu == 7:
        highest_qty()
    elif menu == 8:
        print("Goodbye!")
        break
    else:
        print("Please try again select a number from the option")
   