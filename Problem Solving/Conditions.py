name = input('What is your name: ')

if len(name) < 3:
    print('Name must be ar least  3 characters')
elif len(name) >10:
    print('Name must be a maximum of 10 Character')
else:
    print("Name looks good!")