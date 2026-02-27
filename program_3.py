# Program #3: Tax Rate
# Author: Abrielle Nyei
# Date: 02/27/2026
# Description:
# This program calculates the state and county sales tax
# based on the total monthly sales entered by the user.
# The state tax rate is 5% and the county tax rate is 2.5%.

# Function to calculate taxes
def calculate_tax(total_sales):
    state_tax_rate = 0.05
    county_tax_rate = 0.025

    # Calculate individual taxes
    state_tax = total_sales * state_tax_rate
    county_tax = total_sales * county_tax_rate

    # Calculate total tax
    total_tax = state_tax + county_tax

    # Return all three values
    return state_tax, county_tax, total_tax


#########
# Mainline

# Ask user for total monthly sales
sales = float(input("Enter the total sales for the month: $"))

# Call the function
state_tax, county_tax, total_tax = calculate_tax(sales)

# Display results
print("\nSales Tax Report")
print("-----------------------")
print("County Sales Tax: $", round(county_tax, 2))
print("State Sales Tax: $", round(state_tax, 2))
print("Total Sales Tax: $", round(total_tax, 2))
