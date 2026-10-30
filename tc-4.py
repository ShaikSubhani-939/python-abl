#RETAIL BILLING WITH DISCOUNT
subtotal = 0

for item in range(1, 4):
    price = float(input("Enter price of item " + str(item) + ": "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity < 0:
        print("Invalid price or quantity")
        break

    subtotal += price * quantity

else:
    if subtotal >= 2000:
        discount = subtotal * 0.05
    else:
        discount = 0

    print("Subtotal: Rs.", round(subtotal, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Final amount: Rs.", round(subtotal - discount, 2))
