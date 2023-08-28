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

    try:
        key, value = arg.split("=")
    except ValueError as e:
        print(f"[ERROR] {str(e)}")
        print("You need to use `=`")
        print(f"You passed {arg}")
        print("try with --key-value")
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid option {key}")
        sys.exit()

    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
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
"""
# LBYL
if current_language in msg:
    message = msg[current_language]
else:
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)
"""

# EAFP 
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[EROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

# Ou com valor default - Dicionarios tem esta opcao 
message = msg.get(current_language, msg["en_US"]) 

print(message * int(arguments["count"]))

