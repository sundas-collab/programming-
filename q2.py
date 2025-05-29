# Define a list
fruits = ["apple", "banana", "cherry"]

# Access items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Loop through the list
print("All fruits:")
for fruit in fruits:
    print(fruit)

# Add items
fruits.append("orange")
fruits.insert(1, "mango")
print("After adding items:", fruits)

# Remove items
fruits.remove("banana")
fruits.pop()
del fruits[0]
print("After removing items:", fruits)

# Sort a list
numbers = [4, 1, 3, 2]
numbers.sort()
print("Sorted list:", numbers)

# Copy a list
copied = numbers.copy()
print("Copied list:", copied)

# List comprehension
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers using list comprehension:", evens)

# Define a tuple
my_tuple = ("apple", "banana", "cherry")

# Access items
print("First item:", my_tuple[0])
print("Last item:", my_tuple[-1])

# Loop through tuple
print("All items:")
for item in my_tuple:
    print(item)