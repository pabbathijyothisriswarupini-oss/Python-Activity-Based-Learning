# Progressive Electricity Billing System in Python

## 1. Problem Statement
 Progressive Electricity Billing: Calculate household bills using multiple consumption slabs, fixed charges, surcharges, and rebates, then compare bills across several months and identify unusual increases. 

## 2. Algorithm

1. Start the program.
2. Input the number of months.
3. For each month, enter electricity consumption in units.
4. Calculate energy charges using progressive slabs.
5. Add fixed charges and surcharge.
6. Apply the rebate if eligible.
7. Compare the current bill with the previous month's bill.
8. Identify increases greater than 30%.
9. Display monthly bills and unusual increases.
10. Stop.

## 3. Flowchart 

```mermaid
flowchart TD
    A([Start]) --> B[/Enter monthly units/]
    B --> C[Calculate slab charges, surcharge and rebate]
    C --> D[Calculate total bill]
    D --> E{More months?}
    E -- Yes --> B
    E -- No --> F[Compare monthly bills]
    F --> G[Identify increases above 30%]
    G --> H[/Display bills and alerts/]
    H --> I([Stop])
```
## 5. Sample Input

Enter number of months: 3
Month 1 units: 80
Month 2 units: 120
Month 3 units: 250


## 6. Sample Output


Month 1 bill: ₹201.60
Month 2 bill: ₹365.00
Unusual increase detected!
Month 3 bill: ₹1062.50
Unusual increase detected!
Billing completed.

