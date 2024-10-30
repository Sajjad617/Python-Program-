weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    convert = weight * .45
    print(f"You are {convert} kilos")
else:
    convert = weight / .45
    print(f"You are {convert} pounds")