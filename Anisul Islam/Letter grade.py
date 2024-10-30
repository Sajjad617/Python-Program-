marks = int(input("Enter your marks: "))

if 80 <= marks <= 100:
    print("A+")
elif 70 <= marks <= 79:
    print("A")
elif 60 <= marks <= 69:
    print("A-")
elif 50 <= marks <= 59:
    print("B")
elif 40 <= marks <= 49:
    print("C")
elif 33 <= marks <= 39:
    print("D")
else:
    print("You failed the exam")

'''
if marks >= 80 and marks <= 100 :
    print("A+")
elif marks >= 70 and marks <= 79 :
    print("A")
elif marks >= 60 and marks <= 69 :
    print("A-")
elif marks >= 50 and marks <= 59 :
    print("B")
elif marks >= 40 and marks <= 49 :
    print("C")
elif marks >= 33 and marks <= 39 :
    print("D")
else:
    print("You failed the exam")
'''
'''
if marks <= 100 and marks > 80:
    print("A+")
elif marks <= 79 and marks >= 70:
    print("A")
elif marks <= 69 and marks >= 60:
    print("A-")
elif marks <= 59 and marks >= 50:
    print("B")
elif marks <= 49 and marks >= 40:
    print("C")
elif marks <= 39 and marks >= 33:
    print("D")
else:
    print("You fail the exam")
'''