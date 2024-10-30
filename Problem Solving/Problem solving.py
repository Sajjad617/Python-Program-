"""
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.

9.
Modify the above question to allow student to sit if he/she has medical cause.
Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
"""
classes_held = int(input("Number of classes held: "))
classes_attend = int(input("Number of classes attended: "))

attendence_percentage = (classes_attend / classes_held) * 100


if attendence_percentage >= 75:
      print("You are allowed to sit in the exam")
else:
      medical_cause = input("Do you have any medical cause?\nIf Yes then enter 'Y' if not enter 'N' ")
      if medical_cause == "Y":
            print("You are allowed to sit in the exam")
      else:
            print("You are not allowed  sit in the exam ")