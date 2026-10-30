marks = []

for student in range(1, 4):
    row = []
    print("Enter marks for Student", student)

    for subject in range(1, 4):
        mark = int(input("Subject " + str(subject) + ": "))
        row.append(mark)

    marks.append(row)

if any(mark < 0 or mark > 100 for row in marks for mark in row):
    print("Invalid marks: each mark must be from 0 to 100")

else:
    totals = []

    for i, row in enumerate(marks, start=1):
        total = sum(row)
        totals.append(total)

        print("Student", i, "total:", total,
              "average:", round(total / 3, 2))

    top_index = totals.index(max(totals))

    print("Highest scorer: Student", top_index + 1)