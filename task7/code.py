
n = int(input("Number of products: "))
items = []
subtotal = tax = 0

rates = {"electronics": 0.18, "clothing": 0.05, "other": 0.12}

for i in range(n):
    name = input("Product name: ")
    category = input("Category (electronics/clothing/other): ").lower()
    price = float(input("Unit price: ₹"))
    qty = int(input("Quantity: "))

    if category not in rates or price < 0 or qty <= 0:
        print("Invalid details!")
        continue

    amount = price * qty
    itemtax = amount * rates[category]
    items.append((name, qty, amount, itemtax))
    subtotal += amount
    tax += itemtax

discount = min(subtotal * 0.10, 1000) if subtotal > 5000 else 0

print("\n--- ITEMIZED INVOICE ---")
for name, qty, amount, itemtax in items:
    print(f"{name} x{qty}: ₹{amount:.2f}, Tax: ₹{itemtax:.2f}")

print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Total tax: ₹{tax:.2f}")
print(f"Final bill: ₹{subtotal - discount + tax:.2f}")

