# Check charcetr hwo many time accur in a word Asfand Ijaz Malik
# a : 4
# s : 1
# f : 1
# n : 1
# d : 1 
# i = 2
# j : 1
# z : 1
# m : 1
# l : 1
# k : 1

word = 'Asfand Ijaz Malik'
char_count = {}

for char in word.lower():
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    print(char + ':' ,count)