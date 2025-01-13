"""def great(name):
     print(f"Hello, {name}!")
great("simon")  
def greet_user(name):
    greeting_message = f"Hello, {name}! Welcome!"
    print(greeting_message)
greet_user("Alice")
def calculate_area(length, width):
    area = length * width
    return area
area = calculate_area(5, 10) 
print(f"Area of the rectangle: {area}")  
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
check_even_odd(7)
check_even_odd(4)
# Create a list of favorite fruits
favorite_fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Access the second element (index 1) and print it
second_fruit = favorite_fruits[1]
print(f"The second favorite fruit is: {second_fruit}")
# Define a dictionary for favorite book information
favorite_book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction"
}

# Retrieve the genre using the key and print it
genre = favorite_book["genre"]
print(f"The genre of the favorite book is: {genre}")
import random

# Generate a random set of numbers between 1 and 10
random_numbers = [random.randint(1, 10) for _ in range(20)]  # Generate 20 random numbers
unique_numbers = set(random_numbers)  # Use set to remove duplicates

# Display the unique numbers
print(f"Unique random numbers: {unique_numbers}")"""

# calculator.py

# main.py

import example.calculator as calculator

# Perform arithmetic operations
num1 = 5
num2 = 3

print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
