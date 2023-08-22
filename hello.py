#!/usr/bin/python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente
o programa exibe a mensagem correspondente.

Usage: 
    Tenha a variavel LANG devidamente configurada ex:
    
    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__autor__="Marcelo Guimaraes"
__license__="Unlicense"

import os
# Execução: LANG=fr_FR ./hello.py

current_language = "en_US"
#current_language = os.getenv("LANG","en_US")[:5]

# 01
# Sets (Hash Table) - O(1) - Constante
# dicts (Hash Table)
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}
print(msg[current_language])


# 02
# Ordem de Complexidade O(n) 
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"

print(msg)

