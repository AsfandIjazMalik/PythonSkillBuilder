# Calculate Factorial of 5 
# # Expected Output is : 120

num_factorial = int(input('Enter the number for which you want to calculate the factorial: '))
factorial = 1
for i in range(num_factorial, 1 , -1):
    factorial *= i
print(f'Factorial of {num_factorial} is {factorial}')