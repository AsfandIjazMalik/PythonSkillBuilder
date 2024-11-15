# Print odd number form 1 to 20
# Expected Output : 1 3 5 7 9 11 13 15 17 19

odd_num = 1
while odd_num <= 20:
    if odd_num % 2 != 0:
        print(odd_num, end=' ')
    odd_num += 1