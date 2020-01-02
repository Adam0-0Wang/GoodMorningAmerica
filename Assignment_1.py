"""
Sonya Cao
COMPSCI 1026
BAUER
10/02/19
Good Morning America!: program prompts user to input breakfast order and will then return the pre-tax total, tax and final total charged for the breakfast
"""


EGG_COST = 0.99
BACON_COST = 0.49
SAUSAGE_COST = 1.49
HASH_COST = 1.19
TOAST_COST = 0.79
COFFEE_COST = 1.09
TEA_COST = 0.89
SMALL_COST = EGG_COST + HASH_COST + 2*TOAST_COST + 2*BACON_COST + SAUSAGE_COST
REGULAR_COST = 2*EGG_COST + HASH_COST + 2*TOAST_COST + 4*BACON_COST + 2*SAUSAGE_COST
BIG_COST = 3*EGG_COST + 2*HASH_COST + 4*TOAST_COST + 6*BACON_COST + 3*SAUSAGE_COST


total_cost = 0 #initializing total cost variable to 0


def format_input(text_line):  #allows the program to accept both uppercase, lowercase and leading and trailing characters for inputted menu items
    text_line = text_line.lower().strip()
    word_list = text_line.split()
    text_line = " ".join(word_list)
    return text_line


while True:
    # resets item variable so that it goes through the loop that checks if it is a valid menu item
    item = ""
    item = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea:")
    item = format_input(item)#converts the ordered item to a understandable format

    # will loop only if the menu item entered is invalid
    while item != "small breakfast" and item != "regular breakfast" and item != "big breakfast" and item != "egg" and item != "bacon" and item != "sausage" and item != "hash brown" and item != "toast" and item != "coffee" and item != "tea" and item != 'q':
        print("Error, invalid menu item. Please try again.") #if item is invalid, error message will appear and the user will be prompted to enter item again
        item = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea:")
        item = format_input(item) #converts the ordered item to a understandable format

    if item == 'q':#if instead of a menu item, 'q' is entered program will break out of while loop
        break

    quantity = input("Enter quantity") #prompting user for quantity of menu item inputted

    #if the quantity is not numeric, will print error message and prompt user to enter a quantity again
    while not quantity.isnumeric():
        print("invalid quantity")
        quantity = input("Enter quantity")

    quantity = int(quantity) #if quantity is numeric will convert that value to an int

    #will add every new item ordered to the cumulative total cost variable
    if item == "small breakfast":
        total_cost += SMALL_COST * quantity
    elif item == "regular breakfast":
        total_cost += REGULAR_COST * quantity
    elif item == "big breakfast":
        total_cost += BIG_COST * quantity
    elif item == "egg":
        total_cost += EGG_COST * quantity
    elif item == "bacon":
        total_cost += BACON_COST * quantity
    elif item == "sausage":
        total_cost += SAUSAGE_COST * quantity
    elif item == "hash brown":
        total_cost += HASH_COST * quantity
    elif item == "toast":
        total_cost += TOAST_COST * quantity
    elif item == "coffee":
        total_cost += COFFEE_COST * quantity
    elif item == "tea":
        total_cost += TEA_COST * quantity

#calculating the tax and final cost for the order and then printing out a receipt for the user
tax = round(total_cost * 0.13, 2)
final_cost = round(total_cost + tax, 2)
total_cost = round(total_cost, 2)
print("Pre-tax total: $" + str(total_cost) + "\nTax: $" + str(tax) + "\nTotal: $" + str(final_cost))
