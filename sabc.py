"""
Dacă x și y sunt două numere naturale cu x ≤ y, atunci notăm cu s(x,y) suma numerelor naturale cuprinse între x și y. De exemplu, s(3,6) = 3+4+5+6 = 18, iar s(7,7) = 7.

Cerința
Se dau numerele naturale a, b și c, unde a ≤ b ≤ c. Calculați s(a,b), s(b,c) și s(a,c).

Date de intrare
Programul citește de la tastatură numerele naturale a, b și c.

Date de ieșire
Programul va afișa pe ecran, separate prin câte un spațiu, cele trei sume.

Restricții și precizări
1 ≤ a ≤ b ≤ c ≤ 10.000
Exemplu:
Intrare

3 10 20
Ieșire

52 165 207
Explicație
Suma numerelor de la 3 la 10 este 52, suma numerelor de la 10 la 20 este 165, iar suma numerelor de la 3 la 20 este 207.
"""

# Suma lui Gauss: n * (n + 1) / 2   1 + 2 + 3 + 4 + 5

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

suma_ab = 0
suma_bc = 0
suma_ac = 0

def suma_gauss(n: int):
    return int(n * (n + 1) / 2)

# a=3, b=5 -> rezultatul final
# a=1, b=5 -> SG 1
# a=1, b=2 -> SG 2
suma_ab = suma_gauss(b) - suma_gauss(a - 1)
suma_bc = suma_gauss(c) - suma_gauss(b - 1)
suma_ac = suma_ab + suma_bc - b

print(suma_ab)
print(suma_bc)
print(suma_ac)
