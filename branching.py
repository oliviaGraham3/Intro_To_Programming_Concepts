hrsBeforeUpCharge = 1000
hours = int(input("Enter the KW hours used: "))
price = 0

if hours <= hrsBeforeUpCharge:
    price = hours * 7.633
elif hours > hrsBeforeUpCharge:
    hrsAfterUpCharge = hours - hrsBeforeUpCharge
    price = hrsBeforeUpCharge * 7.633 + hrsAfterUpCharge * 9.259
price = round(price / 100, 2)
print(price)