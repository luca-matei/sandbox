"""
Cerința
Scrieți funcția având următorul antet:

def reverse_words(text)
Funcția primește ca parametru un text format din cuvinte separate prin câte un spațiu.
Cuvintele sunt formate doar din litere mici.
Funcția va returna, tot prin intermediul parametrului text, cuvintele în ordine inversă, separate tot prin câte un spațiu.

Exemplu:
După apelul reverse_words("dubai dubai viata ca in rai") text va fi "rai in ca viata dubai dubai"

Restricții și precizări
Lungimea șirului s este de cel mult 800.000 și conține cel puțin două cuvinte
șirul poate conține cuvinte de o literă
cuvintele din șir sunt separate prin exact un spațiu
șirul este indexat de la 0, începe cu o literă și se termină cu o literă
"""

# .split(" ")
text = input("Textul: ")  # "dubai dubai viata ca in rai"
cuvinte = text.split(" ")  # ["dubai", "dubai", "viata", "ca", "in", "rai"]

# Metoda 1
# sorted(cuvinte, reverse=True)

# Metoda 2
cuvinte_inversate = []
for idx in range(len(cuvinte) - 1, -1, -1):
    cuvinte_inversate.append(cuvinte[idx])

# Metoda 4
# cuvinte[::-1]

print(
    " ".join(cuvinte_inversate)
)
