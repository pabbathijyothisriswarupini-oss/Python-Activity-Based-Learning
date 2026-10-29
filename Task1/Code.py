
n = int(input("Number of applicants: "))
eligible = []

for i in range(n):
    name = input("\nStudent name: ")
    marks = tuple(map(int, input("Enter 3 subject marks: ").split()))
    attendance = float(input("Attendance (%): "))
    income = int(input("Annual family income: ₹"))
    aggregate = sum(marks) / len(marks)

    if aggregate >= 75 and min(marks) >= 60 and attendance >= 75 and income <= 250000:
        eligible.append((name, aggregate, attendance, income))

eligible.sort(key=lambda x: (-x[1], -x[2], x[3]))

if eligible:
    print("\nScholarship Ranking")
    for rank, (name, marks, att, inc) in enumerate(eligible, 1):
        print(rank, name, "Aggregate:", marks,
              "Attendance:", att, "Income:", inc)
else:
    print("No eligible applicants found.")

