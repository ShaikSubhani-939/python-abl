held = int(input("Total classes held: "))
attended = int(input("Classes attended: "))

if held <= 0 or attended < 0 or attended > held:
    print("Invalid attendance details")
else:
    percentage = attended / held * 100
    future = 0

    while (attended + future) / (held + future) < 0.75:
        future += 1

    print("Current attendance:", round(percentage, 2), "%")
    print("Additional classes to attend:", future)