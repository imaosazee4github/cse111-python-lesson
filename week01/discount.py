from datetime import datetime 
DISCOUNTS_RATE = .1
TAX_RATE = .06
today = datetime.now()
day_of_week = today.weekday()
subTotal = 0
quantity = 1
while quantity != 0:
    quantity = int(input("Enter the quantity: "))
    if quantity != 0:
        Price = float(input("Enter price of goods: "))
        subTotal += quantity * Price

print(f"Total order {subTotal}")
discount=0
if day_of_week ==2 or day_of_week == 3 or day_of_week == 4:
    if subTotal > 50:
        discount = round(subTotal * DISCOUNTS_RATE, 2)
        print(f"Discount {discount} ")
    else:
        short = 50 - subTotal
        print(f"You can get a discount by ordering {short} amount more.")
subTotal -= discount
tax = round(subTotal * TAX_RATE, 2)
total = subTotal + tax


print(f"Tax {tax} ")
print(f"Total {total} ")