'''
num = [5, 2, 5, 2, 2]
for x in num:
    print('*' * x)
print("End")
'''

num = [5, 2, 5, 2, 2]
for x_count in num:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

    print(x_count)



'''
for item in ['Mosh', 'John', 'Sarah',  'smith']:
    print (item)

for item in [1, 100, 1000, 10000]:
        print(item)
'''
# for item in range(1, 50, 5):
  #  print(item)
'''
prices = [10, 20, 30]
total = 0
for item in prices:
    total += item
print(f"item : {total}")
print(f"Total: {total}")
'''
