"""
Cerința
Se dau două numere naturale x și y. Calculați ultima cifră a sumei lor.

Date de intrare
Programul citește de la tastatură numerele x și y.

Date de ieșire
Programul va afișa pe ecran ultima cifră a sumei x+y.

Restricții și precizări
1 ≤ x,y < 1.000.000
Exemplu:
Intrare

25 78
Ieșire

3
"""

# %
# 3 % 2 = 1

x = int(input("Numarul x: "))
y = int(input("Numarul y: "))

ultima_cifra = x % 10 + y % 10
ultima_cifra = ultima_cifra % 10

print(ultima_cifra)

"""

39
15
--
 4
+1

36 / 12 = 3

"""

# 34 / 10 = 3 rest 4
# 34 % 10 = 4
# 3 * 10 + 4 = 34