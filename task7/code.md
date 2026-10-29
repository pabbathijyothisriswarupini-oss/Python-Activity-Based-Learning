# Retail Billing with Multiple Discount Rules in Python

## 1. Problem Statement
Retail Billing with Multiple Discount Rules: Process multiple products, quantities, categoryspecific taxes, threshold discounts, and maximum concession limits to generate an itemized invoice. 


## 2. Algorithm

1. Start.
2. Input the number of products.
3. For each product, input name, category, price, and quantity.
4. Calculate each item's subtotal.
5. Apply the discount if the total subtotal exceeds ₹5,000.
6. Limit the discount to ₹1,000.
7. Calculate tax according to each product category.
8. Calculate the final bill.
9. Display the itemized invoice and total amount.
10. Stop.

## 3. Flowchart 
```Mermaid

flowchart TD
    A([Start]) --> B[/Enter product details/]
    B --> C[Calculate subtotal and category tax]
    C --> D{Subtotal above ₹5000?}
    D -- Yes --> E[Apply discount up to ₹1000]
    D -- No --> F[No discount]
    E --> G[Calculate final bill]
    F --> G
    G --> H[/Display itemized invoice/]
    H --> I([Stop])






## 5. Sample Input


Number of products: 2
Product name: Phone
Category (electronics/clothing/other): electronics
Unit price: ₹5000
Quantity: 1
Product name: Shirt
Category (electronics/clothing/other): clothing
Unit price: ₹1000
Quantity: 1


## 6. Sample Output


--- ITEMIZED INVOICE ---
Phone x1: ₹5000.00, Tax: ₹900.00
Shirt x1: ₹1000.00, Tax: ₹50.00
Subtotal: ₹6000.00
Discount: ₹600.00
Total tax: ₹950.00
Final bill: ₹6350.00



