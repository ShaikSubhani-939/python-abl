#MANUFACTURING COST AND PROFITABILITY
material = float(input("Material cost: "))
labour = float(input("Labour cost: "))
machine = float(input("Machine cost: "))
quantity = int(input("Quantity produced: "))
selling_price = float(input("Selling price per unit: "))

if min(material, labour, machine, quantity, selling_price) < 0:
    print("Invalid input")
else:
    total_cost = material + labour + machine
    revenue = quantity * selling_price
    profit = revenue - total_cost

    print("Total production cost: Rs.", round(total_cost, 2))
    print("Sales revenue: Rs.", round(revenue, 2))
    print("Profit: Rs.", round(profit, 2))

    if profit >= 2000:
        print("Target profit achieved")
    else:
        print("Target profit not achieved")
