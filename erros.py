#!/usr/bin/python3

import os
import sys
#names = ["Marcelo","Maria","Joao"]


# LBYL - Look Before You Leap


if os.path.exists("names.txt"):
    print("O arquivo existe")
    input("...") # Race condition
    names = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found.")
    sys.exit(1)

# LBYL - Look Before You Leap

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in te list")
    sys.exit(1)
