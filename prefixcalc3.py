#!/usr/bin/python3

"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serao salvos em prefixcal.log
"""
__version__ = "0.1.0"

import sys
import os
from datetime import datetime

arguments = sys.argv[1:]

if not arguments:
    operation = input("operacao:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
else len(arguments) != 3:
    print("Numero de argumentos invalidos")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mult", "div")

if operation not in valid_operations:
    print("Operacao invalida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".","").isdigit():
        print(f"Numero invalido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

try:
    n1, n2 = validated_nums
except ValueErro as e:
    print(str(e))
    sys.exit(1)

if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mult":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"O resultado e {result}")

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user}, {operation},{n1},{n2} = {result}\n")
except PermissionError as e:
    print(str(e))
    sys.exit(1)
