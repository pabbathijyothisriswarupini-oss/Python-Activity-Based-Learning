# Campus Event Financial Planning in Python

## 1. Problem Statement
Campus Event Financial Planning: Calculate venue, equipment, catering, transport, and certificate costs; determine participant contributions, sponsorship shortfalls, and the minimum registration count needed to break even. 


## 2. Algorithm

1. Start.
2. Input venue, equipment, catering, transport, and certificate costs.
3. Input sponsorship amount, expected participants, and contribution per participant.
4. Calculate total event expenses.
5. Calculate the remaining cost after sponsorship.
6. Calculate the required contribution per participant.
7. Calculate the minimum registrations needed to cover the remaining cost.
8. Display expenses, sponsorship shortfall, participant contribution, and break-even registrations.
9. Stop.

## 3. Flowchart 
```Mermaid

flowchart TD
    A([Start]) --> B[/Enter event costs and sponsorship/]
    B --> C[Calculate total expenses and shortfall]
    C --> D[Calculate participant contribution]
    D --> E[Find minimum registrations]
    E --> F[/Display financial report/]
    F --> G([Stop])
```



## 5. Sample Input


Venue cost: ₹20000
Equipment cost: ₹8000
Catering cost: ₹15000
Transport cost: ₹5000
Certificate cost: ₹2000
Sponsorship amount: ₹20000
Expected participants: 100
Contribution per participant: ₹250


## 6. Sample Output


--- EVENT BUDGET REPORT ---
Total cost: ₹50000.00
Sponsorship shortfall: ₹30000.00
Required contribution per participant: ₹300.00
Minimum registrations to break even: 120



