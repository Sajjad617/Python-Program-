try:
    hours = int(input("Enter Your Hours: "))
    rate  = int(input("Enter a Rate: "))
    Total = hours * rate
    print(Total)
except:
    print("Error, please enter numeric input")