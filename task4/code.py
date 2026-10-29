
name = input("Employee name: ")
basic = float(input("Basic pay: ₹"))
allow = float(input("Allowances: ₹"))
overtime = float(input("Overtime: ₹"))
incentive = float(input("Incentives: ₹"))

if min(basic, allow, overtime, incentive) < 0:
    print("Invalid salary details")
else:
    gross = basic + allow + overtime + incentive

    if gross <= 20000:
        deduction = gross * 0.05
    elif gross <= 40000:
        deduction = 1000 + (gross - 20000) * 0.10
    else:
        deduction = 3000 + (gross - 40000) * 0.15

    net = gross - deduction
    print("\n--- SALARY STATEMENT ---")
    print("Employee:", name)
    print(f"Gross Salary: ₹{gross:.2f}")
    print(f"Deduction: ₹{deduction:.2f}")
    print(f"Net Salary: ₹{net:.2f}")

