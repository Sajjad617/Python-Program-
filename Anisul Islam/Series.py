# 1 + 2 + 3 + ... + n
n = int(input("Enter the last value: "))
sum = 1
for x in range(1, n+1, 1) :
    sum = sum * x
print(sum)