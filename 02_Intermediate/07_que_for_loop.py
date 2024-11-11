# Fabonacci Sequence up to 10 
# What is Fabonacci Serious : Sum of last Two numbers and first two is fixed

a = 0 
b = 1
print(a,b , end=' ')

for _ in range(8):
    next_term = a + b
    print(next_term, end=' ')
    a,b = b, next_term