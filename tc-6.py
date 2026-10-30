#EXAMINATION RESULT AND GRACE-MARK VALIDATION 
marks = [int(input("Enter marks for subject " + str(i) + ": "))
         for i in range(1, 4)]

if any(mark < 0 or mark > 100 for mark in marks):
    print("Invalid marks")
else:
    low = [i for i in range(3) if marks[i] < 35]

    if len(low) == 1 and marks[low[0]] == 34:
        other_marks = [marks[i] for i in range(3) if i != low[0]]

        if all(mark >= 35 for mark in other_marks):
            marks[low[0]] = min(100, marks[low[0]] + 1)
            print("One grace mark applied")

    total = sum(marks)

    print("Final marks:", marks)
    print("Total:", total, "/ 300")

    if all(mark >= 35 for mark in marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")
