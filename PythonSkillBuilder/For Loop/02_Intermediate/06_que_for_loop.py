vowel = 'aeiou'
word = 'Education'
count = 0

for char in word.lower():
    if char in 'aeiou':
        count += 1
        
print(f'Vowel Characters in {word} is {count}')