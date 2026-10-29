
budget = float(input("Travel budget in INR: ₹"))
fee_rate = float(input("Conversion fee (%): "))
n = int(input("Number of expenses: "))
expenses = {}

for i in range(n):
    category = input("Expense category: ")
    amount = float(input("Amount in foreign currency: "))
    rate = float(input("Exchange rate to INR: "))

    if amount < 0 or rate <= 0:
        print("Invalid expense!")
        continue

    converted = amount * rate
    fee = converted * fee_rate / 100
    total = converted + fee
    expenses[category] = expenses.get(category, 0) + total
    print(f"{category}: ₹{total:.2f}")

spent = sum(expenses.values())

print(f"\nTotal spending: ₹{spent:.2f}")
if expenses:
    print("Largest category:", max(expenses, key=expenses.get))
print("Budget exceeded!" if spent > budget else "Within budget.")
print(f"Balance: ₹{budget - spent:.2f}")

