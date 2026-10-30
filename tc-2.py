#HOSPITAL BILLING AND PATIENT CLASSIFICATION
consultation = float(input("Consultation charge: "))
diagnostics = float(input("Diagnostic charge: "))
treatment = float(input("Treatment charge: "))

if consultation < 0 or diagnostics < 0 or treatment < 0:
    print("Invalid charge")
else:
    subtotal = consultation + diagnostics + treatment

    if subtotal >= 5000:
        concession = subtotal * 0.10
        category = "High Billing"
    else:
        concession = 0
        category = "General"

    final_bill = subtotal - concession

    print("Subtotal: Rs.", round(subtotal, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Final bill: Rs.", round(final_bill, 2))
    print("Patient category:", category)
