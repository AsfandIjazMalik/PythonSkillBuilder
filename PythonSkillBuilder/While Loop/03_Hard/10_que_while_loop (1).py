# Write a program that counts how many digits are in a given positive integer using a while loop.
# For example, if the user enters 98765, the program should output 5 because the number 123 has 3 digits.

number = int(input("Enter a positive integer to count its digits: "))
digit_count = 0

while number > 0:
    digit_count += 1  # Increment the digit count
    number //= 10  # Remove the last digit

print(f"The number of digits is: {digit_count}")
