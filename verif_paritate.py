"""
Cerința
Se citesc n numere naturale. Determinați pentru fiecare dintre ele dacă este par sau impar.

Date de intrare
Programul citește de la tastatură numărul n, iar apoi n numere naturale.

Date de ieșire
Programul va afișa pe ecran n valori 0 sau 1, separate prin spații. Dacă numărul corespunzător este par se va afișa 0, iar dacă este impar se va afișa 1.

Restricții și precizări
1 ≤ n ≤ 1000
cele n numere citite se pot reprezenta pe 64 de biți, fără semn;
se recomandă utilizarea operațiilor pe biți
Exemplu:
Intrare

5
1 2 3 4 5
Ieșire

1 0 1 0 1
"""

n = int(input("N: "))

for i in range(n):
    x = int(input("X: "))

    if x % 2 == 0:
        print("Par!")
    else:
        print("Impar!")
