#!/usr/bin/python3

import logging

logging.debug("Mensagem pro Dev, qe, sysadmin")
logging.info("Mensagem geral para usuários")
logging.warning("Aviso que nao causa erro")
logging.error("Erro que afeta uma unica execucao")
logging.critical("Erro geral. Ex.: Falha como banco de dados")

print("---")

try:
    1 / 0 
except ZeroDivisionError as e:
    # print(f"[ERRO] Deu erro {str(e)}")
    logging.error("Deu erro %s", str(e))
