"""
Author: Collins Nuamah Brobbey

Purpose: Meal price calculator

"""
import math

print()

#Data collection
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children_number = int(input("How many children are there? "))
adult_number = int(input("How many adults are there? "))

print()

#Subtotal: $36.00
child_total = child_meal * children_number
adult_total = adult_meal * adult_number
subtotal = child_total + adult_total
print(f"Subtotal:  ${subtotal:.2f} \n")

#Calculating sales tax and total
sales_tax_rate = int(input("What is the sales tax rate? "))
sales_tax = subtotal * sales_tax_rate / 100
print(f"Sales Tax:  ${sales_tax:.2f}")

Total = subtotal + sales_tax
print(f"Total: ${Total:.2f}\n")

#Collecting payment amount and displaying change
payment_amount = int(input("What is the payment amount? "))
change = payment_amount - Total
print(f"Change: ${change:.2f}\n" )
