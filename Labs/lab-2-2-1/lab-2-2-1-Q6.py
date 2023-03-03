# Lab 2-2-1 Question 6
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Write a program to ascertain if the user can go to the beach.

# Should we go?
should_we_go = input('Should we go to the beach? (y/n): ').strip().lower()

# Day validation
is_sat = input('Is it Saturday? (y/n): ').strip().lower()
is_sun = input('Is it Sunday? (y/n): ').strip().lower()

# Tide validation
is_low_tide = input('Is the tide out? (y/n): ').strip().lower()

#Answer
final_answer = str(should_we_go[0] == 'y' and (is_sat == 'y' and is_sun != 'y' or is_sun == 'y' and is_sat != 'y') and is_low_tide[0] == 'y').lower()

# Print the results
print()
print(f'It is {final_answer} that we can go to the beach today.')