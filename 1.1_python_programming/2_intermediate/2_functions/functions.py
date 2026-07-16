"""
Module: Functions and modular code
Description: Foundational material for Functions and modular code.

Tutor guide:
  - Type code examples, explanations, and live demos under each topic section.

Topics:
  1. Functions and modular code
"""

# 1. Functions and modular code
# Tutor note: write teaching examples and code snippets here.

# def example_functions_and_modular_code_1():
#     # Add example code for functions_and_modular_code here
#     pass

# practicing kwargs

# pass arguments as dictionaries

def my_info(**kwargs):
       print(kwargs)
 
  
my_info(
  name="Gita",
  email="fonyuyjudegita@gmail.com",
  about="A young developer ready to innovate"
)

# 22 immutable laws of branding and marketting

# A5. Decorators — functions that wrap functions

# Once you accept "functions are objects" and "closures capture enclosing variables," a decorator is nothing more than: *a function that takes a function as input and returns a new function as output, usually one that calls the original and adds behavior around it.*

def announce(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished.")
        return result
    return wrapper

def add(a, b):
    return a + b

add = announce(add)   # manually "decorating"
add(2, 3)
# Calling add...
# add finished.