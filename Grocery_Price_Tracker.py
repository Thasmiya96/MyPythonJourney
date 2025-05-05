# Store items as tuples (item_name, price)
grocery_list = []

# Input loop for 6 items
for i in range(6):
    item = input(f"Enter item {i+1}: ")
    price = int(input(f"Enter price of {item}: "))
    grocery_list.append((item, price))

# Function to display menu
def get_response():
    print('''
Enter Number:
  > 1. View List
  > 2. Search an item
  > 3. Total Expenses
  > 4. Exit
''')

# Main loop
while True:
    get_response()
    response = int(input("Enter your choice: "))

    if response == 1:
        sorted_list = sorted(grocery_list, key=lambda x: x[0])  # Sort by item name
        print("\nGrocery Items:")
        for item, price in sorted_list:
            print(f"- {item}: ₹{price}")
    
    elif response == 2:
        search_item = input("Enter item to search: ")
        found = False
        for item, price in grocery_list:
            if item.lower() == search_item.lower():
                print(f"{item} is in the list, price: ₹{price}")
                found = True
                break
        if not found:
            print(f"{search_item} not found.")

    elif response == 3:
        total = sum(price for item, price in grocery_list)
        print(f"Total Expense: ₹{total}")
    
    elif response == 4:
        print("Exiting program. Thank you!")
        break
    
    else:
        print("Invalid choice. Try again.")
