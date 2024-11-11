# Print Following pattern  
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5, 0, -1):  # Loop to control the number of rows
    for j in range(i):  # Loop to print stars in each row
        print('*', end=' ')  # Print stars in the same line with a space in between
    print()  # Move to the next line after each row