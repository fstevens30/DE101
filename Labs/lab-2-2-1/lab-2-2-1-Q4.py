# Lab 2-2-1 Question 4
# Flynn Stevens
# fas0265@arastudent.ac.nz

word_orig = input('Please enter a word that starts with a capital letter and with subsequent letters in lower case: ').strip()
word_cap = word_orig.capitalize()

checker = str(word_orig == word_cap).lower() # Is the word the same as the word with the first letter capitalized?

print(f'It is {checker} that {word_orig} starts with a capital letter and all subsequent letters are in lower case.')