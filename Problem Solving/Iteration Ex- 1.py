num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    #print(fval)
    num = num + 1 nm
    tot = tot + fval

#print('All Done')
print(int(tot), num, tot/num)
