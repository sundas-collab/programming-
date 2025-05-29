# Define a tuple
my_tuple = ("apple", "banana", "cherry")

# Access items
print("First item:", my_tuple[0])
print("Last item:", my_tuple[-1])

# Loop through tuple
print("All items:")
for item in my_tuple:
    print(item)

# Join tuples
tuple1 = ("red", "green")
tuple2 = ("blue", "yellow")
combined = tuple1 + tuple2
print("Joined tuple:", combined)

# "Update" a tuple (indirectly)
temp_list = list(my_tuple)
temp_list[1] = "mango"
my_tuple = tuple(temp_list)
print("Updated tuple:", my_tuple)

# Unpacking
person = ("Alice", 30, "UK")
name, age, country = person
print(f"Name: {name}, Age: {age}, Country: {country}")

# Tuple methods
sample = ("x", "y", "x", "z")
print("Count of 'x':", sample.count("x"))
print("Index of 'y':", sample.index("y"))

import array

arr = array.array('i', [1, 2, 3])  # Only integers
arr.append(4)
print("Array:", arr.tolist())     # Convert to list for display

my_list = [1, "apple", 3.5]
my_list.append("banana")
print("List:", my_list)

my_tuple = (1, "apple", 3.5)
print("Tuple:", my_tuple)

my_set = {1, 2, 2, 3}
my_set.add(4)
print("Set:", my_set)  # Duplicates removed