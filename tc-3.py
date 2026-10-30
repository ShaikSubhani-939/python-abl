#EMPLOYEE PAYROLL AND DEDUCTION ANALYSIS
basic = float(input("Basic pay: "))
allowance = float(input("Allowance: "))
overtime = float(input("Overtime pay: "))

if basic < 0 or allowance < 0 or overtime < 0:
    print("Invalid salary details")
else:
    gross = basic + allowance + overtime
    deduction = gross * 0.08
    net = gross - deduction

    print("Gross salary: Rs.", round(gross, 2))
    print("Deduction (8%): Rs.", round(deduction, 2))
    print("Net salary: Rs.", round(net, 2))
