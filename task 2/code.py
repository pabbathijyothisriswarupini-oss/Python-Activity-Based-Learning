
n = int(input("Enter number of months: "))
previous = 0

for month in range(1, n + 1):
    units = int(input(f"Month {month} units: "))

    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 200 + (units - 100) * 3
    else:
        energy = 500 + (units - 200) * 5

    bill = energy + 50 + energy * 0.05
    if units < 100:
        bill -= energy * 0.10

    print(f"Month {month} bill: ₹{bill:.2f}")
    if previous > 0 and bill > previous * 1.30:
        print("Unusual increase detected!")
    previous = bill

print("Billing completed.")

