# Initial shopping list
shopping_list = ["milk", "bread", "eggs", "butter", "juice", 
                 "sugar", "salt", "biscuits", "tea", "coffee"]

# 1. Display all items using a loop
print("Current Shopping List:")
for item in shopping_list:
    print("-", item)

# 2. Ask the user if they want to add a new item
add_choice = input("\nDo you want to add a new item? (yes/no): ").lower()
if add_choice == "yes":
    new_item = input("Enter the item to add: ").strip()
    shopping_list.append(new_item)
    print(f"'{new_item}' added to the shopping list.")

# 3. Ask the user if they want to remove any item
remove_choice = input("\nDo you want to remove an item? (yes/no): ").lower()
if remove_choice == "yes":
    item_to_remove = input("Enter the item to remove: ").strip()
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
        print(f"'{item_to_remove}' removed from the shopping list.")
    else:
        print("Item not found.")

# 4. Display the updated list
print("\nUpdated Shopping List:")
for item in shopping_list:
    print("-", item)