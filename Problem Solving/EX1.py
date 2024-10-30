num = 1
tot = 0.0
while True:
    x = input('Enter a number: ')
    if x == 'done' :
        break
    try:
        x1 = float(x)
    except:
        print('Invalide Number')
        continue

    num = num + num
    tot = tot + x1
print(tot,"\n",  num, "\n", tot/num)