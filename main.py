import hashlib
import random


boolean = True
string = "grnegjg"
float = 123.43
lista = [1, "2", True, [4], 5, 1]
tupla = (1, 2, True, 4, 5)
dictionar = {
    "key1": 1,
    "key2": "2",
    "key3": True,
    "key4": [4],
    "key5": 5
}
seturi = {1, 2, True, 4, 5}

def get_random_number(a: int, b: int = 100):
    """Get a random number between a and b."""
    # PEP 8 de citit
    numar: int = random.randint(a, b)
    return numar

print(get_random_number(1, 100))

def get_hash(text):
    """
    Function to get the hash of a given text.
    """
    return hashlib.sha256(text.encode()).hexdigest()

# print(get_hash("numar"))