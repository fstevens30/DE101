# Lab 2-2-2 CHALLENGE
# Flynn Stevens
# fas0265@arastudent.ac.nz

# Pizza chooser!

# Intro
print('The pizza chooser.')

# Questions
is_veggie = input('Are you a vegetarian? ').strip().lower()
is_vegan = input('Are you a vegan? ').strip().lower()
is_carni = input('Are you a meat eater? ').strip().lower()
wants_pizza = input('Would you like to eat a pizza? ').strip().lower()

# Answers
wants_veggie = str(is_veggie[0] == 'y' and is_vegan != 'y' and is_carni != 'y' and wants_pizza[0] == 'y').lower() # User is vegetarian and not vegan or carnivore and wants pizza
wants_vegan = str(is_vegan[0] == 'y' and is_veggie != 'y' and is_carni != 'y' and wants_pizza[0] == 'y' or is_vegan[0] != 'y' and is_veggie == 'y' and is_carni != 'y' and wants_pizza[0] == 'y').lower() # User is vegan and not vegetarian or carnivore and wants pizza or user is vegetarian and not vegan or carnivore and wants pizza
wants_carni = str(is_carni[0] == 'y' and is_veggie != 'y' and is_vegan != 'y' and wants_pizza[0] == 'y').lower() # User is carnivore and not vegetarian or vegan and wants pizza

# Print the results
print()
print(f'It is {wants_veggie} that you would like a veggie pizza.')
print(f'It is {wants_vegan} that you would like a vegan pizza.')
print(f'It is {wants_carni} that you would like a carnivore pizza.')