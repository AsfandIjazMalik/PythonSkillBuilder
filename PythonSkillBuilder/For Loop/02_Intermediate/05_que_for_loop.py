# Revers this word 'kilaM zajI dnafsA'
# Expected output is : Asfand Ijaz Mlaik

# Reverse Indexing
word = 'kilaM zajI dnafsA'
# len(word) - 1 is used to get last character of the word
for char in range(len(word) - 1, -1, -1): 
    print(word[char], end='') 