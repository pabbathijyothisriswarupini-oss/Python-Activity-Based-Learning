
n = int(input("Number of passengers: "))
distance = int(input("Travel distance (km): "))
booking_total = penalty_total = 0

for i in range(n):
    print(f"\nPassenger {i+1}")
    name = input("Name: ")
    age = int(input("Age: "))
    cls = input("Class (Sleeper/AC): ").lower()
    action = input("Action (Book/Cancel): ").lower()

    if distance <= 100:
        fare = distance * 2
    elif distance <= 300:
        fare = 200 + (distance - 100) * 3
    else:
        fare = 800 + (distance - 300) * 4

    if cls == "ac":
        fare *= 2
    elif cls != "sleeper":
        print("Invalid class!")
        continue

    if age < 5:
        fare = 0
    elif age >= 60:
        fare *= 0.80

    if action == "book":
        total = fare + 40
        booking_total += total
        print(f"{name}: Booking fare = ₹{total:.2f}")
    elif action == "cancel":
        total = fare * 0.25
        penalty_total += total
        print(f"{name}: Cancellation penalty = ₹{total:.2f}")
    else:
        print("Invalid action!")

print(f"\nTotal booking amount: ₹{booking_total:.2f}")
print(f"Total cancellation penalties: ₹{penalty_total:.2f}")

