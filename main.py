import hashlib
import random

### Python Basics
number = 123
boolean = True
string = "I'm a string"
float_number = 123.43
mixed_list = [1, "2", True, [4], 5, 1]  # mutable list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # list of lists / 2D list
mixed_tuple = (1, 2, True, 4, 5)  # immutable list
dictionary = {  # key-value pairs
    "key1": 1,
    "key2": "2",
    "key3": True,
    "key4": [4],
    "key5": 5,
}
number_set = {1, 2, 3, 4, 5}  # only has unique values


### Functions
def get_random_number(a: int, b: int = 100):
    """
    Get a random number between a and b.
    :param a: lower bound
    :param b: upper bound (default is 100)
    """
    random_number: int = random.randint(a, b)
    return random_number


# Display the random number between 1 and 100
# print(get_random_number(1, 100))


def get_hash(text):
    """Function to get the hash of a given text."""
    # Hash the text using SHA-256 algorithm
    return hashlib.sha256(text.encode()).hexdigest()


# Display the hash of the string "Buna, eu sunt un string"
# print(get_hash("Buna, eu sunt un string"))


# Create a function that takes two numbers as arguments and returns their sum here
...

# Create a function that takes a string as an argument and returns its length here
...

"""
Hint: Hover over the function name to see the docstring.

Exercises:
1. Create a function that takes two numbers as arguments and returns their sum.
2. Create a function that takes a string as an argument and returns its length. (Hint: Use the len() function)
3. Commit your newly created functions to Github.

Nice to read:
- https://peps.python.org/pep-0008/ (PEP 8 - Style Guide for Python Code)

Next time:
- We'll learn to create a virtual environment (crucial to development)
- We'll create a game of Snake using Pygame - https://github.com/luca-matei/snake
"""
