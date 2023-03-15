# Python Syntax Cheatsheet

***

Made by Flynn Stevens for DE101, Test 1 (S1, 2023)

This is a cheatsheet for Python syntax that I will use for DE101 Test 1. It is a consolidation of all of my notes from the first week of class.

***

## Python Basics

- Indentation is important in Python. It is used to show what code is part of a loop or function.
- Compared to other languages, Python is very easy to read.
- Semi-colons are not used in Python, rather it uses line breaks and indentation to show where code ends.

### Commenting Code

Comments are made using the `#` symbol. Anything after the `#` symbol will not be read by the computer. Multi-line comments can be made using `"""` or `'''`, however this is not recommended as it is primarily used for docstrings (multi line strings).

```python
# This is a comment
```

### Assigning Variables

We can assign variables using the `=` assignment operator. We can also assign multiple variables at once.

### Printing

We can print in Python using the `print()` function. What we wants to print goes inside the parentheses.

```python
x = "Hello World"
print(x) 
# Output: Hello World
```

### User Input

User input can be taken using the `input()` function. The input will be stored as a string.

```python
x = input("Enter your name: ") 
print("Hello " + x)
# User Input: Flynn
# Output: Hello Flynn
```

***

## Python Data Types

### Numbers

Numbers include `int` (integer) and `float` (floating point number).

```python
x = 1 # int
y = 1.0 # float
```
