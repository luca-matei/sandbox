"""
Cerinţa
Se dau n numere întregi. Calculaţi cel mai mic dintre cele n numere date.

Date de intrare
Programul citește de la tastatură numărul n, iar apoi n numere întregi, separate prin spaţii.

Date de ieşire
Programul afișează pe ecran numărul MIN, reprezentând cel mai mic dintre cele n numere date.

Restricţii şi precizări
1 ≤ n ≤ 1000
cele n numere citite vor avea cel mult 9 cifre
Exemplu:
Date de intrare

5
7 6 9 6 8
Date de ieșire

9
"""

n = input("Numarul n: ")
n = int(n)
min = None

for i in range(n):
    x = input("Numar intreg: ")
    x = int(x)

    if min == None:
        min = x
    elif x < min:
        min = x

print(min)
