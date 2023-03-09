# Lab 3-2-2 CHALLENGE
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Const triangle types
EQUILATERAL = 'an equilateral'
ISOSCELES = 'an isosceles'
SCALENE = 'a scalene'

# Getting inputs (I used a, b, c so the variables match the triangle theory)
a = input('Enter the length of side 1: ').strip()
b = input('Enter the length of side 2: ').strip()
c = input('Enter the length of side 3: ').strip()

# Check that all inputs are valid
if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit() and c.replace('.', '', 1).isdigit():

    # Convert inputs to floats
    a = float(a)
    b = float(b)
    c = float(c)

    # Check that the sum of any two sides is greater than the third
    if a + b > c and a + c > b and b + c > a:

        # Check that all sides are equal
        if a == b == c:
            print(f'A triangle with sides {a}, {b} and {c} is {EQUILATERAL} triangle.')

        # Check that two sides are equal
        elif a == b or a == c or b == c:
            print(f'A triangle with sides {a}, {b} and {c} is {ISOSCELES} triangle.')

        # Check that no sides are equal
        else:
            print(f'A triangle with sides {a}, {b} and {c} is {SCALENE} triangle.')
    else:
        print('The triangle inequality theorem requires the sum of two sides to be greater than the third.')
else:
    print('One or more of the sides was invalid.')