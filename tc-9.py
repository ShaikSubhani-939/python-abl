#WAREHOUSE INVENTORY RECONCILIATION
for product in range(1, 4):
    print("Product", product)

    opening = int(input("Opening stock: "))
    received = int(input("Received quantity: "))
    dispatched = int(input("Dispatched quantity: "))
    recorded = int(input("Recorded closing stock: "))

    if min(opening, received, dispatched, recorded) < 0:
        print("Invalid quantity")

    elif dispatched > opening + received:
        print("Invalid movement: dispatch exceeds available stock")

    else:
        expected = opening + received - dispatched
        difference = recorded - expected

        print("Expected closing stock:", expected)

        if difference == 0:
            print("Stock matched")
        else:
            print("Discrepancy:", difference, "(recorded - expected)")
