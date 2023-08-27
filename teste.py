import sys
argumentos = {}
for arg in sys.argv[1:]:
    chave, valor = arg.split("=")
    argumentos[chave.lstrip('-').strip()] = valor.strip()

print(argumentos)
