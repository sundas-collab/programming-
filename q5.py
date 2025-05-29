# Define the function
def check_even_odd(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

# Call the function with a number
num = int(input("Enter a number: "))
check_even_odd(num)