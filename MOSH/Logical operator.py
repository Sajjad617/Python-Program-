# (AND) All condition is True then program is true otherwise false
# (OR) All condition is False then program is False otherwise True
# AND: both
# OR: at least one
# NOT: Fales is True / True is False
has_high_income = True
good_credit = False

if has_high_income and not good_credit:
    print("Eligible for loan\n")
else:
    print("Loan not Eligible\n")


if has_high_income or good_credit:
    print("Eligible for loan\n")
else:
    print("Loan not Eligible\n")