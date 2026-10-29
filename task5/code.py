
data = float(input("Required data (GB): "))
calls = int(input("Required call minutes: "))
days = int(input("Required validity (days): "))
budget = float(input("Budget: ₹"))
n = int(input("Number of plans: "))
plans = []

for i in range(n):
    print(f"\nPlan {i+1}")
    name = input("Plan name: ")
    price = float(input("Base price: ₹"))
    gb = float(input("Included data (GB): "))
    mins = int(input("Included call minutes: "))
    valid = int(input("Validity (days): "))
    cost = price + max(0, data-gb)*10 + max(0, calls-mins)
    ok = valid >= days and cost <= budget
    print(f"Total cost: ₹{cost:.2f}", "Eligible" if ok else "Not eligible")
    if ok:
        plans.append((cost, name))

if plans:
    cost, name = min(plans)
    print(f"\nBest plan: {name}, Cost: ₹{cost:.2f}")
else:
    print("\nNo eligible plan found.")

