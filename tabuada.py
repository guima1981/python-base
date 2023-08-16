#!/usr/bin/python3

"""Imprime a tabuada do 1 ao 10.
---Tabuado do 1---

     1 x 1 = 1
     2 x 1 = 2
     3 x 1 = 3
...
#################
---Tabuada do 2---

     2 x 1 = 1
     2 x 2 = 4
...
#################
"""
__version__ = "0.1.1"
__author__ = "Marcelo"

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Iterable (percorriveis)
numeros = list(range(1, 11))

for n1 in numeros:
    print("{:-^18}".format(f"Tabuado do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}")) 
    print("#" * 18)
