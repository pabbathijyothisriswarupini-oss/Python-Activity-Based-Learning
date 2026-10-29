
material = float(input("Material cost: ₹"))
labour = float(input("Labour charges: ₹"))
machine = float(input("Machine cost: ₹"))
waste = float(input("Wastage percentage: "))
qty = int(input("Quantity produced: "))
price = float(input("Selling price per unit: ₹"))
target = float(input("Target profit: ₹"))

if min(material, labour, machine, waste, qty, price, target) < 0 or waste > 100 or qty == 0:
    print("Invalid input")
else:
    wastage = material * waste / 100
    cost = material + labour + machine + wastage
    revenue = qty * price
    profit = revenue - cost

    print("\n--- PRODUCTION REPORT ---")
    print(f"Wastage cost: ₹{wastage:.2f}")
    print(f"Total cost: ₹{cost:.2f}")
    print(f"Sales revenue: ₹{revenue:.2f}")
    print(f"Profit: ₹{profit:.2f}")
    print("Target achieved" if profit >= target
          else "Target not achieved")

