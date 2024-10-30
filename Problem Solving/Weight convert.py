weight = int(input("weight: "))
unit = input("(L )bs or (k)g: ")
if unit.upper() == "L":
   con =  weight * 0.45
   print(f"You are {con} Kilos")
elif unit.upper() == "K":
    converted = weight/0.45
    print(f"You are {converted} pounds")
else:
    print("Doesn't match ")