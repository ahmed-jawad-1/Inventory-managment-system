from colorama import Fore, Style
import os
import json


def load():
    if os.path.exists("test4.json"):
        with open("test4.json", "r") as file:
            return json.load(file)
    return []

def load_employ():
    if os.path.exists("testemploy.json"):
        with open("testemploy.json", "r") as file:
            return json.load(file)
    return []

# Function to save inventory to a file
def save_inventory(inventory):
    with open("test4.json", "w") as file:
        json.dump(inventory, file, indent=4)

def save_employ(employ):
    with open("testemploy.json", "w") as file:
        json.dump(employ, file, indent=4)


def billing():
    print(Style.RESET_ALL)
    print(Fore.BLUE+"Billing")
    print(Style.RESET_ALL)
    print()
    name = input("Enter customer name: ")
    Date = input("Enter the date (dd/mm/yyyy): ")
    list2 = []
    list3 = []
    list4 = []
    total_price = 0
    while True:
        barcode = input("Enter the barcode (enter 0 to stop) : ")
        if barcode == '0':
            break
        if barcode in inventory.keys():
            list1 = inventory[barcode]
            quan = int(input("Enter quantity: "))
            if quan <= list1[1]:
                price = list1[2]
                t_price = price*quan
                total_price += t_price
                list2.append(list1[0])
                list3.append(quan)
                list4.append(list1[2])
                list1[1] = list1[1] - quan
                inventory[barcode] = list1
            else:
                print(Fore.RED+"Not enough stock")
                print(Style.RESET_ALL)
        else:
            print(Fore.RED+"Barcode not found")
            print(Style.RESET_ALL)
    print()
    print(Fore.BLUE+" || ",end="")
    print(Fore.LIGHTYELLOW_EX+" Name ",end="")
    print(Fore.BLUE+" || ",end="")
    print(Style.RESET_ALL,end="")
    print(f"{name.capitalize()}",end="")
    print(Style.RESET_ALL,end="")
    print(Fore.BLUE+" || ",end="")
    print(Fore.LIGHTYELLOW_EX+" Date ",end="")
    print(Fore.BLUE+" || ",end="")
    print(Style.RESET_ALL,end="")
    print(f"{Date}",end="")
    print(Fore.BLUE+" || ")
    print(Style.RESET_ALL)
    print(Fore.BLUE+" || ",end="")
    print(Style.RESET_ALL,end="")
    print(Fore.YELLOW+"Item",end="")
    print(Fore.BLUE+" || ",end="")
    print(Style.RESET_ALL,end="")
    print(Fore.BLUE+" || ",end="")
    print(Style.RESET_ALL,end="")
    print(Fore.YELLOW+"Quantity",end="")
    print(Fore.BLUE+" || ",end="")
    print(Style.RESET_ALL,end="")
    print(Fore.BLUE+" || ",end="")
    print(Style.RESET_ALL,end="")
    print(Fore.YELLOW+"Price",end="")
    print(Fore.BLUE+" || ",end="")
    print(Style.RESET_ALL)

    for i in range(len(list2)):
        print(Fore.BLUE+" || ",end="")
        print(Style.RESET_ALL,end="")
        print(f"{list2[i]}",end="")
        print(Fore.BLUE+" || ",end="")
        print(Style.RESET_ALL,end="")
        print(Fore.BLUE+" || ",end="")
        print(Style.RESET_ALL,end="")
        print(f"{list3[i]}",end="")
        print(Fore.BLUE+" || ",end="")
        print(Style.RESET_ALL,end="")
        print(Fore.BLUE+" || ",end="")
        print(Style.RESET_ALL,end="")
        print(f"{list4[i]}$",end="")
        print(Fore.BLUE+" || ",end="")
        print(Style.RESET_ALL)
    print(Fore.BLUE+" || ",end="")
    print(Style.RESET_ALL,end="")
    print(Fore.YELLOW+"Total Price",end="")
    print(Fore.BLUE+" || ",end="")
    print(Fore.GREEN+f"{total_price}$",end="")
    print(Style.RESET_ALL)
    print()
    save_inventory(inventory)

def adding_items():
        print()
        print(Fore.BLUE+"Adding Data")
        print(Style.RESET_ALL)
        while (True):
            bar = input("Enter barcode (press 0 to stop) : ")
            if bar == '0':
                break
            if bar in inventory:
                print(Fore.RED+"Item Already in Stock")
                print(Style.RESET_ALL)
                continue
            item=input("Enter the item name: ")
            for i in inventory.keys():
                if item.upper() in inventory[i][0].upper():
                    print(Fore.RED+"Item already in stock")
                    print(Style.RESET_ALL)
            quantity=int(input("Enter the quantity: "))
            price=float(input("Enter the price: "))
            inventory[bar] = [item,quantity,price]
        print(Fore.GREEN+"Item added successfully")
        print(Style.RESET_ALL)
        save_inventory(inventory)
def login():
    global username
    print(Fore.BLUE+"-- Login --")
    print(Style.RESET_ALL)
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in employ:
        if password==employ[username]:
            print(Fore.GREEN+"Login successfully")
            print(Style.RESET_ALL)
            return True
        else:
            print(Fore.RED+"Invalid username")
            print(Style.RESET_ALL)
            return False

def signup():
    global username
    global password
    print(Fore.BLUE+"-- Signup --")
    print(Style.RESET_ALL)
    username = input("\nEnter a new username: ")
    password = input("Enter a new password: ")
    employ[username] = password
    print(Fore.GREEN+"details saved succesfully\n")
    print(Style.RESET_ALL)
    save_employ(employ)


def edit_inventory():
    print()
    print(Fore.BLUE+"Editing Inventory")
    print(Style.RESET_ALL)
    for i in inventory:
        list1 = inventory[i]
        print(Fore.BLUE+"|||",end="")
        print(Fore.YELLOW+"  Barcode  ",end='')
        print(Fore.BLUE+"||",end="")
        print(Fore.GREEN+f"  {i}  ",end='')
        print(Fore.BLUE+"||",end="")
        print(Fore.YELLOW+"  Name  ",end='')
        print(Fore.BLUE+"||",end="")
        print(Fore.GREEN+f"  {list1[0]} ",end='')
        print(Fore.BLUE+"|||")
    print(Style.RESET_ALL)
    edit = input("Which item you want to edit? (BARCODE) :  ")
    if edit in inventory:
        list1 = inventory[edit]
        for i in list1:
            print()
            print(Fore.BLUE+"|||",end="")
            print(Fore.YELLOW+"  Name  ",end='')
            print(Fore.BLUE+"||",end="")
            print(Fore.GREEN+f"  {list1[0]}  ",end='')
            print(Fore.BLUE+"||",end="")
            print(Fore.YELLOW+" Quantity ",end='')
            print(Fore.BLUE+"||",end="")
            print(Fore.GREEN+f"  {list1[1]} ",end='')
            print(Fore.BLUE+"||",end="")
            print(Fore.GREEN+f"  Price ",end='')
            print(Fore.BLUE+"||",end="")
            print(Fore.GREEN+f"  {list1[2]} ",end='')
            print(Fore.BLUE+"|||")
            print(Style.RESET_ALL)
            sel = (input('''Q: Quantity\nP : Price\nB: Go back\n\nWhich feild you want to edit? '''))
            if sel.upper() == 'Q':
                q_update = int(input("Enter the updated quantity: "))
                list1[1] = q_update
                save_inventory(inventory)
                print(Fore.GREEN+"Updated!")
            elif sel.upper() == 'P':
                p_update = int(input("Enter the updated price: "))
                list1[2] = p_update
                save_inventory(inventory)
                print(Fore.GREEN+"Updated!")
            elif sel.upper() == 'B':
                break
            else:
                print(Fore.RED+"Inavlid")
        else:
            print(Fore.RED+"Invalid Barcode")
    save_inventory(inventory)

def display_all():
        from tqdm import tqdm
        import sys
        import time

        for i in tqdm(range(100)):
            # Assuming your terminal supports ANSI color codes
            sys.stdout.write("\033[32m")  # Set color to green
            sys.stdout.flush()
            time.sleep(0.01)
        print("Done !")
        for i in inventory:
            list1 = inventory[i]
            print()
            print(Fore.BLUE+"|||",end="")
            print(Fore.YELLOW+"  Barcode  ",end='')
            print(Fore.BLUE+"||",end="")
            print(Fore.GREEN+f"  {i}  ",end='')
            print(Fore.BLUE+"||",end="")
            print(Fore.YELLOW+"  Name  ",end='')
            print(Fore.BLUE+"||",end="")
            print(Fore.GREEN+f"  {list1[0]} ",end='')
            print(Fore.BLUE+"||",end="")
            print(Fore.YELLOW+"  Quantity  ",end='')
            print(Fore.BLUE+"||",end="")
            print(Fore.GREEN+f"  {list1[1]} ",end='')
            print(Fore.BLUE+"||",end="")
            print(Fore.YELLOW+"  Price  ",end='')
            print(Fore.BLUE+"||",end="")
            print(Fore.GREEN+f"  {list1[2]} ",end='')
            print(Fore.BLUE+"|||")
        print(Style.RESET_ALL)
        print()

print("*********************************************************************")
print('''
 **   :::   :::   ::.        --:                             .::             **
 **   :++. .+++:  =+.        =+-                             -+=             **
 **    =+- -+-+= :+- ==-=+=. =+- ==-==+=-==+=  :=--==: -+-==:-++==           **
 **    :+= == ==.=+.  ::-=+- =+- =+:  ++-  =+:  .::=+= -+=.  -+=             **
 **     =+-+: -+-+= :==:.-+= =+- =+:  =+:  =+:.=+-.:++ -+=   -+=             **
 **     :=+=  .=++. :+=:-=== =+- =+:  =+:  =+:.=+-:==+ -+=   :++-:           **
''')
print("*********************************************************************")
print()
employ = load_employ()
inventory = load()

while True:
    qas = input("Signup OR Login: (S/L) ")
    print()
    if qas.upper() == 'S':
        signup()
    if login() == True:
        while (True):
            choice=input('''A: Add data\nB: Calculate bill\nC: Edit inventory\nD: Display All\nE: Logout\nWhat Operation you want to perform:  ''')

            if choice.upper() == "A":
                adding_items()
            if choice.upper() == "B":
                billing()
            if choice.upper() == "C":
                edit_inventory()
            if choice.upper() == "D":
                display_all()
            if choice.upper() == "E":
                break