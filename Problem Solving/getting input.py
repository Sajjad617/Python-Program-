price = 10000
has_good_creadit = False

if has_good_creadit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")