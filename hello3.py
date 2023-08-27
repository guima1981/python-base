#!/usr/bin/python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente
o programa exibe a mensagem correspondente.

Usage: 
    Tenha a variavel LANG devidamente configurada ex:
    
    export LANG=pt_BR

    ou informe atraves do CLI 

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__autor__="Marcelo Guimaraes"
__license__="Unlicense"

# Execução: LANG=fr_FR ./hello.py
# ./hello3.py --lang=fr_FR

import os
import sys

#print(f"{sys.argv=}")

arguments = {
        "lang": None,
        "count": 1,
}

for arg in sys.argv[1:]:
#    print(f"{arg=}")
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid option {key}")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    if current_language is None:
        current_language = input("Choose a language: ")

current_language = current_language[:5]

# Sets (Hash Table) - O(1) - Constante
# dicts (Hash Table)
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}
print(msg[current_language] * int(arguments["count"]))

