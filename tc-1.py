units = int(input("Enter units consumed: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = 100 * 2 + (units - 100) * 3
    else:
        energy_charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    total_bill = energy_charge + 50

    print("Energy charge: Rs.", energy_charge)
    print("Fixed charge: Rs. 50")
    print("Total bill: Rs.", total_bill)