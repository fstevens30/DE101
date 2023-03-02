# Lab 2-1-1 Question 6
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Get the staff members first name
# Get the customers first name
# Get the customers order quantities
# Get the customers special instructions
# Print the order summary

# Const Variables
MEAL_1_PRICE = float(7)
MEAL_2_PRICE = float(8.5)
MEAL_3_PRICE = float(10)

COFFEE_PRICE = float(4)

TAX_RATE = float(0.15) # This represents the 15% tax rate.
TAX_RATE_PERCENTAGE = 15

# Get the staff members first name
staff_name = input('Please enter the first name of the staff member: ').strip().capitalize()

# Get the customers first name
customer_name = input('Please enter the first name of the customer: ').strip().title()

# Order quantities
meal_1_quantity = int(input("How many meal #1's (Veggie burger) are required? "))
meal_2_quantity = int(input("How many meal #2's (Veggie burger with some chips) are required? "))
meal_3_quantity = int(input("How many meal #3's (Veggie burger with heaps of chips) are required? "))
coffee_quantity = int(input('How many coffees are required? '))
special_instructions = input('Special instructions: ').strip().capitalize()

# Math
meal_1_total = meal_1_quantity * MEAL_1_PRICE
meal_2_total = meal_2_quantity * MEAL_2_PRICE
meal_3_total = meal_3_quantity * MEAL_3_PRICE
coffee_total = coffee_quantity * COFFEE_PRICE

subtotal = meal_1_total + meal_2_total + meal_3_total + coffee_total
total = subtotal + (subtotal * TAX_RATE)

# Print the order summary

print() # Blank line for formatting
print(f'Your meal was prepared by {staff_name}.')
print('You have ordered the following:')
print(f"Meal #1's: {meal_1_quantity}")
print(f"Meal #2's: {meal_2_quantity}")
print(f"Meal #3's: {meal_3_quantity}")
print(f'Drinks: {coffee_quantity}')
print() # Blank line for formatting
print(f'Special instructions: {special_instructions}')
print(f'Nett subtotal: ${subtotal:.2f}')
print(f'Total including tax at {TAX_RATE_PERCENTAGE}% is: ${total:.2f}')
print(f'Thank you for your order {customer_name}.')