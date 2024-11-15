# write a program which calculate the the power of a number to 4
# like 3 x 3 x 3 x 3 = 81

number_cal = int(input('Enter the number for which you want to calculate to the power of 4'))
power = 4
iteration = 0
while iteration <= 4:
    reuslt = number_cal ** power
    iteration += 1

print(reuslt)