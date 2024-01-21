# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------
NOME..: main.py
LANG..: Python3
TITULO: Inicializador do programa
DATA..: 21/01/2024
VERSÃO: 0.1.00
HOST..: diversos
LOCAL.: diversos
OBS...: colocar nas linhas abaixo informações importantes sobre o programa
- Biblioteca com as funções mais utilizadas
DEPEND: (informar nas linhas abaixo os recursos necessários para utilização)
-------------------------------------------------------------------------
Modifications.....:
Date          Rev    Author           Description
21/01/2024    0      Thomas Campos    Elaboração
-------------------------------------------------------------------------

"""

import logging

# Módulos do programa
from start import start

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":

    logger.info(f"=== Definindo variaveis do programa ===")
    pathLocal = '/Users/thoma/Documents/tmp/recebidos/'
    pathDest = '/Users/thoma/Documents/tmp/recebidos/executados/'
    url = 'https://github.com/cambridgecoding/machinelearningregression/blob/master/data/bikes.csv'

    start(pathLocal, pathDest, url )
