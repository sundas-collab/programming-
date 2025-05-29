# Given list of numbers
numbers = [5, 12, 7, 18, 9, 24, 3, 16, 11]

# Counters for each category
divisible_by_3 = 0
even_not_3 = 0
odd_not_3 = 0

# Loop through each number
for num in numbers:
    if num % 3 == 0:
        print(f"{num} is divisible by 3")
        divisible_by_3 += 1
    elif num % 2 == 0:
        print(f"{num} is even but not divisible by 3")
        even_not_3 += 1
    else:
        print(f"{num} is odd and not divisible by 3")
        odd_not_3 += 1

# Final counts
print("\nSummary:")
print("Numbers divisible by 3:", divisible_by_3)
print("Even numbers (not divisible by 3):", even_not_3)
print("Odd numbers (not divisible by 3):", odd_not_3)

def classify_numbers(numbers):
    # Initialize counters
    counts = {
        "positive": 0,
        "zero": 0,
        "negative": 0
    }

    # Loop through each number in the list
    for num in numbers:
        if num > 0:
            print(f"{num} is positive")
            counts["positive"] += 1
        elif num == 0:
            print(f"{num} is zero")
            counts["zero"] += 1
        else:
            print(f"{num} is negative")
            counts["negative"] += 1

    # Return the dictionary with counts
    return counts

# Example usage
number_list = [5, -2, 0, 8, -7, 0, 3]
result = classify_numbers(number_list)

# Print the result
print("\nClassification Summary:")
print(result)