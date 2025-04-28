"""
Cerința
Se dă un număr natural n cu cel puțin două cifre, care conține atât cifre pare cât și cifre impare.
Calculați suma dintre cea mai mică cifră pară și cea mai mare cifră impară a lui n.

Date de intrare
Programul citește de la tastatură numărul n.

Date de ieșire
Programul va afișa pe ecran suma cerută.

Restricții și precizări
10 ≤ n ≤ 1.000.000.000
Exemplu:
Intrare

57289
Ieșire

11
Explicație
Cea mai mică cifră pară a lui 57289 este 2, iar cea mai mare impară este 9.
"""

# while
# // -> 5 // 2 = 2 (nu 2.5)
# % -> 5 % 2 = 1 ======= 2 % 2 = 0

n = int(input("n: "))
cifra_min = None
cifra_max = None
suma_cifre = 0

"""
# Mergem prin fiecare cifra a lui n

# 986403
# 98649 3
# 986403 // 10 = 98640

# 98640
# 9864 0
# 98640 // 10 = 9864

...

# 9
# . 9
# 9 // 10 = 0
"""

while n != 0:
    ultima_cifra = n % 10

    # Par
    if ultima_cifra % 2 == 0:
        if cifra_min == None:
            cifra_min = ultima_cifra
        elif ultima_cifra < cifra_min:
            cifra_min = ultima_cifra
    
    # Impar
    elif ultima_cifra % 2 == 1:
        if cifra_max == None:
            cifra_max = ultima_cifra
        elif ultima_cifra > cifra_max:
            cifra_max = ultima_cifra

    n = n // 10

suma = cifra_min + cifra_max
print(suma)
