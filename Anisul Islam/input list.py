num_of_word = 0
num_of_letters = 0
num_of_digit = 0
text = input("Enter a text number: ")

for x in text :
    x = x.lower()
    if x >= 'a' and x <= 'z' :
        num_of_letters = num_of_letters + 1

    elif x >= '0' and x <= '9' :
        num_of_digit = num_of_digit + 1

    elif x == ' ' :
        num_of_word = num_of_word + 1

print("Number of letters : ", num_of_letters)
print("Number of digits : ", num_of_digit)
print("Number of word : ", num_of_word+1)







'''
n = input("Enter a text of numbers: ")
list = n.split()
sum = 0
for num in list :
    sum = sum + int (num)

print(sum)
'''