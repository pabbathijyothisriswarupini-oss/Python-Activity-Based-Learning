
venue = float(input("Venue cost: ₹"))
equipment = float(input("Equipment cost: ₹"))
catering = float(input("Catering cost: ₹"))
transport = float(input("Transport cost: ₹"))
certificates = float(input("Certificate cost: ₹"))
sponsor = float(input("Sponsorship amount: ₹"))
participants = int(input("Expected participants: "))
contribution = float(input("Contribution per participant: ₹"))

cost = venue + equipment + catering + transport + certificates
shortfall = max(0, cost - sponsor)

if min(venue, equipment, catering, transport, certificates, sponsor, contribution) < 0 or participants <= 0:
    print("Invalid input")
else:
    required = shortfall / participants
    registrations = 0 if shortfall == 0 else (
        -(-shortfall // contribution) if contribution > 0 else -1
    )

    print("\n--- EVENT BUDGET REPORT ---")
    print(f"Total cost: ₹{cost:.2f}")
    print(f"Sponsorship shortfall: ₹{shortfall:.2f}")
    print(f"Required contribution per participant: ₹{required:.2f}")
    if registrations >= 0:
        print(f"Minimum registrations to break even: {int(registrations)}")
    else:
        print("Break-even impossible with zero contribution")

