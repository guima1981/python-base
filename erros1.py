#!/usr/bin/python3

import os
import sys
#names = ["Marcelo","Maria","Joao"]

# EAFP - Easy to Ask Forgiveness than permission
# É mais fácil pedir perdão do que permissão

try:
    names = open("names.txt").readlines() #FileNotFoundError
    1 / 0 # ZeroDivisionError
    print(names.banana) # AttributeError
#except (FileNotFoundError,ZeroDivisionError) as e:
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] You cant divide by Zero!!!")
    sys.exit(1)
except AttributeError:
    print("[Error] List doesnt have banana")
    sys.exit(1)

try:
    print(names[2])
except:
    print("[Error] Missing name in te list")
    sys.exit(1)
