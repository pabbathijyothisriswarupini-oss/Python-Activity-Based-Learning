# Employee Payroll and Deduction Analysis in Python

## 1. Problem Statement

 Employee Payroll and Deduction Analysis: Calculate gross salary from basic pay, allowances, overtime, and incentives; apply progressive deductions and generate a formatted salary statement.

## 2. Algorithm

1. Start.
2. Input employee name, basic pay, allowances, overtime, and incentives.
3. Calculate gross salary.
4. Calculate progressive deductions using salary slabs.
5. Calculate net salary by subtracting deductions from gross salary.
6. Display the formatted salary statement.
7. Stop.

## 3. Flowchart 
```Mermaid

flowchart TD
    A([Start]) --> B[/Input salary details/]
    B --> C[Calculate gross salary]
    C --> D[Calculate progressive deductions]
    D --> E[Calculate net salary]
    E --> F[/Display salary statement/]
    F --> G([Stop])
```



## 5. Sample Input


Employee name: Ravi
Basic pay: ₹30000
Allowances: ₹5000
Overtime: ₹2000
Incentives: ₹3000


## 6. Sample Output
--- SALARY STATEMENT ---
Employee: Ravi
Gross Salary: ₹40000.00
Deduction: ₹3000.00
Net Salary: ₹37000.00
