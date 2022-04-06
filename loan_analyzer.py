# coding: utf-8
from audioop import lin2lin
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""

loan_costs = [500, 600, 200, 1000, 450]

#Calculate number of loans
total_number_of_loans = len(loan_costs)

#Calculate sum of loans
sum_of_loans = sum(loan_costs)

#calculate average of loans
average_of_loans = sum_of_loans / total_number_of_loans

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
print(f"The total number of loans is {total_number_of_loans}.")

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
print(f"The total of all the loans (sum) is {sum_of_loans}.")

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
print(f"The average of all the loans is {average_of_loans}.")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.

#Extract the "future_value" of the "loan" dictionary
future_value = loan.get("future_value")

#Extract the "remaining_months" of the "loan" dictionary
remaining_months = loan.get("remaining_months")

#Print both values
print(f"The future value of the loan is {future_value}.")
print(f"There are {remaining_months} months remaining.")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

minimum_required_return = 0.20 #defines the Discount Rate, or in this case, the minimum required return threshold
present_value = future_value / (1 + minimum_required_return / 12) ** remaining_months
print(f"The present value of the loan is ${present_value}.")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
loan_price = loan.get("loan_price", 500)
print(F"The price of the loan is {loan_price}.")
if present_value >= loan_price:
    print(f"The loan (${present_value}) is worth at least the cost to buy it (${loan_price}) - therefore, buy the loan.")
else:
    print(f"The loan (${present_value}) is too expensive and not worth the price (${loan_price}) - therefore, pass.")

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.

# Defines a simple present value calculation function where the arguments are the variables in the formula, and then prints the results

def present_value_function_simp(future_value_fn,remaining_months_fn,annual_discount_rate_fn):
    present_value_fn = future_value_fn / (1 + annual_discount_rate_fn / 12) ** remaining_months_fn
    print(f"The present value as a result of the simple present value function is {present_value_fn}.")

# Defines a complex present value calculation whose arguments are the discount rate key and discount rate value, where the 
# function then adds the arguments to the "new_loan" dictionary (for archival purposes), and then extracts them to perform the calculation, and then
# prints the results

def present_value_function_compl(discount_rate_key,annual_discount_rate_fn_compl):
    new_loan[discount_rate_key] = annual_discount_rate_fn_compl
    present_value_fn_compl = new_loan.get("future_value") / (1 + new_loan.get(discount_rate_key)/ 12) ** new_loan.get("remaining_months")
    print(f"The present value as a result of the complex present value function is {present_value_fn_compl}.")

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.

#Calls both functions defined above

present_value_function_simp(1000,12,0.2)

present_value_function_compl("discount_rate",0.2)


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

list_of_loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]



# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = []
print(f"At this point, the inexpensive_loans list is: {inexpensive_loans}.")

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list


# Separate the list of dictionaries into 4 separate dictionaries

l1, l2, l3, l4 = [(l5) for l5 in list_of_loans]

# check the four dictionaries for loan price of $500 and under

for cheap_loans1 in l1:
    l1_cont_price = l1["loan_price"]
    if l1_cont_price <= 500:
        l1_cont_str = (l1.values())
        inexpensive_loans.append(list(l1_cont_str))
        break

for cheap_loans1 in l1:
    l1_cont_price = l2["loan_price"]
    if l1_cont_price <= 500:
        l1_cont_str = (l2.values())
        inexpensive_loans.append(list(l1_cont_str))
        break

for cheap_loans1 in l1:
    l1_cont_price = l3["loan_price"]
    if l1_cont_price <= 500:
        l1_cont_str = (l3.values())
        inexpensive_loans.append(list(l1_cont_str))
        break

for cheap_loans1 in l1:
    l1_cont_price = l4["loan_price"]
    if l1_cont_price <= 500:
        l1_cont_str = (l4.values())
        inexpensive_loans.append(list(l1_cont_str))
        break

print(f"The inexpensive loans are {inexpensive_loans}.")


# @TODO: Print the `inexpensive_loans` list, and the expensive_loans list


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""


# Separate the values from inexpensive_loans for rows

l6, l7 = [(l8) for l8 in inexpensive_loans]

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
# creates a list of a list so that the header and data doesn't open a csv with letters separated by commas
headers = [header]
rows2 = [l6]
rows3 = [l7]


# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.


# Contains the arguemnt to open the csv file in w mode
file = open(output_path, 'w+',newline='')
# Opens csv file
with file:
    write = csv.writer(file)
    # Write the rows for header
    write.writerows(headers)
    write.writerows(rows2)
    write.writerows(rows3)

print("This module was completed on Apr 06, 2022 at 12:11 PM")