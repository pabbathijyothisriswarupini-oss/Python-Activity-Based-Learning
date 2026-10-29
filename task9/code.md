# Multi-Currency Travel Budget Analysis in Python

## 1. Problem Statement
 Multi-Currency Travel Budget Analysis: Convert travel expenses using supplied exchange rates, incorporate conversion fees, compare planned spending against a budget, and identify the largest expense category. 

## 2. Algorithm

1. Start.
2. Input the travel budget and conversion fee percentage.
3. Enter expense categories, amounts, currencies, and exchange rates.
4. Convert each expense into INR.
5. Calculate the conversion fee and total expense.
6. Add all expenses to calculate total spending.
7. Identify the largest expense category.
8. Compare spending with the budget.
9. Display the expense report and budget status.
10. Stop.

## 3. Flowchart 
```m*ermaid

flowchart TD
    A([Start]) --> B[/Enter budget and expenses/]
    B --> C[Convert expenses to INR]
    C --> D[Add conversion fees]
    D --> E{More expenses?}
    E -- Yes --> C
    E -- No --> F[Find total and largest category]
    F --> G{Within budget?}
    G --> H[/Display expense report/]
    H --> I([Stop])
```




## 5. Sample Input


Travel budget in INR: ₹30000
Conversion fee (%): 2
Number of expenses: 3

Expense category: Hotel
Amount in foreign currency: 200
Exchange rate to INR: 83

Expense category: Food
Amount in foreign currency: 100
Exchange rate to INR: 90

Expense category: Transport
Amount in foreign currency: 50
Exchange rate to INR: 105


## 6. Sample Output


Hotel: ₹16932.00
Food: ₹9180.00
Transport: ₹5355.00

Total spending: ₹31467.00
Largest category: Hotel
Budget exceeded!
Balance: ₹-1467.00


