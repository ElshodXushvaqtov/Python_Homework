# Import necessary libraries
import pandas as pd
import numpy as np

# --- Homework 1 ---
print("--- Homework 1: DataFrame Operations ---")

# Create the initial DataFrame
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Rename column names using a function
df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})
print("\nDataFrame after renaming columns:")
print(df)

# Print the first 3 rows of the DataFrame
print("\nFirst 3 rows of the DataFrame:")
print(df.head(3))

# Find the mean age of the individuals
mean_age = df['age'].mean()
print(f"\nMean age: {mean_age:.2f}")

# Select and print only the 'first_name' and 'City' columns
name_city = df[['first_name', 'City']]
print("\nSelected 'first_name' and 'City' columns:")
print(name_city)

# Add a new column 'Salary' with random salary values (e.g., between 50000 and 100000)
df['Salary'] = np.random.randint(50000, 100000, size=len(df))
print("\nDataFrame with new 'Salary' column:")
print(df)

# Display summary statistics of the DataFrame
print("\nSummary statistics of the DataFrame:")
print(df.describe())
print("-" * 50)


# --- Homework 2: Sales and Expenses Analysis ---
print("\n--- Homework 2: Sales and Expenses Analysis ---")

# Create the sales_and_expenses DataFrame
sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})
print("\nSales and Expenses DataFrame:")
print(sales_and_expenses)

# Calculate and display the maximum sales and expenses
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
print(f"\nMaximum Sales: {max_sales}")
print(f"Maximum Expenses: {max_expenses}")

# Calculate and display the minimum sales and expenses
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
print(f"\nMinimum Sales: {min_sales}")
print(f"Minimum Expenses: {min_expenses}")

# Calculate and display the average sales and expenses
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()
print(f"\nAverage Sales: {avg_sales}")
print(f"Average Expenses: {avg_expenses}")
print("-" * 50)


# --- Homework 3: Monthly Expense Analysis ---
print("\n--- Homework 3: Monthly Expense Analysis ---")

# Create the expenses DataFrame
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})
print("\nOriginal Expenses DataFrame:")
print(expenses)

# Set 'Category' column as the index
expenses_indexed = expenses.set_index('Category')
print("\nExpenses DataFrame with 'Category' as index:")
print(expenses_indexed)

# Calculate and display the maximum expense for each category
max_expense_per_category = expenses_indexed.max(axis=1)
print("\nMaximum expense per category:")
print(max_expense_per_category)

# Calculate and display the minimum expense for each category
min_expense_per_category = expenses_indexed.min(axis=1)
print("\nMinimum expense per category:")
print(min_expense_per_category)

# Calculate and display the average expense for each category
avg_expense_per_category = expenses_indexed.mean(axis=1)
print("\nAverage expense per category:")
print(avg_expense_per_category)
print("-" * 50)
