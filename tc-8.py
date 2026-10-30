balance = 1000.0
count = int(input("Number of transactions: "))

for i in range(count):
    kind = input("Transaction type (D/W): ").upper()
    amount = float(input("Amount: "))

    if amount <= 0:
        print("Rejected: amount must be positive")
    elif kind == "D":
        balance += amount
        print("Deposit successful")
    elif kind == "W" and amount <= balance:
        balance -= amount
        print("Withdrawal successful")
    elif kind == "W":
        print("Rejected: insufficient balance")
    else:
        print("Rejected: invalid transaction type")

    print("Current balance: Rs.", round(balance, 2))

print("Final balance: Rs.", round(balance, 2))