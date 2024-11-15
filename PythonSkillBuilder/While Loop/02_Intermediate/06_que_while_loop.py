# Check consonant in Word learning
# Expected output: 5

word = input('Enter Word to count consonant in a word: ').lower()
count = 0
vowel = 'aeiou'
index = 0

while index < len(word):
    if word[index] not in vowel:
        count += 1
    index += 1
print(count)