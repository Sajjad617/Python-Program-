"""index = 0
fruit = 'sajjad'
x = len(fruit) * (-1)
while index < len(fruit):
    index = index - 1
    letter = fruit[index]
    if index == x:
        break
    print(letter)

def letter_count(word):
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    return count

word = 'banana'
print(letter_count(word))
"""
word = 'cat'
if word < 'banana':
    print('Your word,' + word.capitalize() + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word.capitalize() + ', comes after banana.')
else:
    print('All right, bananas.')





