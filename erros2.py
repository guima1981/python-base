#!/usr/bin/python3

import os
import sys
#names = ["Marcelo","Maria","Joao"]

# EAFP - Easy to Ask Forgiveness than permission
# É mais fácil pedir perdão do que permissão

try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e))

try:
    names = open("names.txt").readlines() #FileNotFoundError
#except (FileNotFoundError,ZeroDivisionError) as e:
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # retry
else:
    print("Sucesso!!")
finally: 
    print("Exexute isso sempre")


try:
    print(names[2])
except:
    print("[Error] Missing name in te list")
    sys.exit(1)
