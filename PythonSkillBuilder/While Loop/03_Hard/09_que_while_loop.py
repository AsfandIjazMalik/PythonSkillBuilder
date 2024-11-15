# Sum of Digits: Write a program that takes a positive integer input from the user and calculates the sum of its digits using a while loop.
# For example, if the user enters 12345, the program should output 1 + 2 + 3 + 4 + 5 = 15.

number = int(input("Enter a positive integer to calculate the sum of its digits: "))
sum_of_digits = 0

while number > 0:
    sum_of_digits += number % 10  # Adds the last digit of the number
    number //= 10  # Removes the last digit

print(f"The sum of digits is: {sum_of_digits}")
