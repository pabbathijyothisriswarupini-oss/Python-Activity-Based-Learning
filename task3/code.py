
name = input("Patient name: ")
age = int(input("Age: "))
c = float(input("Consultation charge: "))
d = float(input("Diagnostic charge: "))
t = float(input("Treatment charge: "))
p = float(input("Payment amount: "))

if min(age, c, d, t, p) < 0:
    print("Invalid input")
else:
    total = c + d + t
    discount = total * 0.10 if age >= 60 else 0
    bill = total - discount

    if p > bill:
        print("Invalid payment: exceeds bill")
    else:
        status = "Paid" if p == bill else "Partially Paid" if p > 0 else "Unpaid"
        print("Total bill: ₹", total)
        print("Concession: ₹", discount)
        print("Final bill: ₹", bill)
        print("Balance: ₹", bill - p)
        print("Status:", status)

