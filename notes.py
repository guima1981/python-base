#!/usr/bin/python3

"""
Bloco de notas

$ notes.py new "Minha Nota"
tag: taech
text:
Anotacao geral

$ notes.py read tech
...
..

"""

__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")
cmds = ("read", "new")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"titulo: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    title = arguments[1]
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:").strip(),
        ]
    with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")

