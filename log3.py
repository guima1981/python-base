#!/usr/bin/python3

import os
import logging
from logging import handlers

# no SO: export LOG_LEVEL=error
log_level = os.getenv("LOG_LEVEL","WARNING").upper()

# Nossa instancia de log
#log = logging.Logger("Marcelo",logging.DEBUG)
log = logging.Logger("Marcelo",log_level)

# Level
#ch = logging.StreamHandler() # ch = console handler -> console/terminal/stderr
#ch.setLevel(logging.DEBUG)
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
        "meulog.log", 
        maxBytes=300, # Recomendado 10**6 (1MB) 
        backupCount=10,
) # File Handler
fh.setLevel(log_level)

# Formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)

# Destino
#log.addHandler(ch)
log.addHandler(fh)

log.debug("Mensagem pro Dev, qe, sysadmin")
log.info("Mensagem geral para usuários")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral. Ex.: Falha como banco de dados")

print("---")

try:
    1 / 0 
except ZeroDivisionError as e:
    # print(f"[ERRO] Deu erro {str(e)}")
    log.error("Deu erro %s", str(e))
