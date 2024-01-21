# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------
NOME..: start.py
LANG..: Python3
TITULO: Módulo executa download de um arquivo csv e move-o para outra pasta;
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

import sys
from os import path 
from shutil import move
import logging
from glob import glob
from utils.global_function import moveFile, downloadCsvFile, listFile

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start(pathLocal: str, pathDest: str, url: str):
    """
        Função responsavel por processar download de arquivo csv e trato do mesmo
    :param pathLocal: (str) - Pasta local aonde é realizado download do arquivo
    :param pathDest: (str) - Pasta pasta destino aonde é encaminhado arquivo csv após validação
    """
    
    logger.info("=== Função: %s ===" % (sys._getframe().f_code.co_name))
    logger.info("=== Parâmetros recebidos ===")
    logger.info(f"pathLocal ...: type {type(pathLocal)}, content {pathLocal}")
    logger.info(f"pathDest ....: type {type(pathDest)}, content {pathDest}")
    logger.info(f"url .........: type {type(url)}, content {url}")
    
    try:

        logger.info(f"=== validando parâmetros recebidos ===")
        if not pathLocal or not url or not pathDest:
            logger.error("Parâmetros inválidos. Certifique-se de fornecer valores para pathLocal, url e pathDest.")
            return False

        logger.info(f"==== Iniciando donwload de arquivo csv ===")
        resultCsv =  downloadCsvFile(url, pathLocal)
        if not resultCsv:
            logger.error("Erro ao baixar o arquivo CSV. Verifique a URL fornecida.")
            return False

        logger.info(f"=== Verificando arquivo csv em pathLocal")
        if pathLocal is None:
            logger.error(f"Erro pathLocal está vazia, não contém arquivo")
            return False
        
        sendDataList = {
            "pathLocal": pathLocal,
            "filePrefix": '',
            "fileExtension": ['.txt', '.csv', '.json', '.ini'],
            "fileRules": ''
        }

        resulList = listFile(sendDataList)
        if not resulList:
            logger.error(f"Erro listar arquivo em {pathLocal}")
            return False

        file = resulList[0]
        logger.info(f"file ...: type {type(file)}, content {file}")     

        sendData = {
            "file": file,
            "pathLocal": pathLocal,
            "pathLocalDest": pathDest
        }
        logger.info(f"file ...: type {type(file)}, content {file}")

        logger.info(f"=== Preparando mover arquivo ===")
        resultPath = moveFile(sendData)
        if not resultPath:
            logger.error("Erro ao mover o arquivo CSV para o destino.")
            return False
        
    except BaseException as errorMsg:
        logger.error("Erro inesperado, verifique o log")
        logger.error("Exception occurred", exc_info=True)
        logger.error(errorMsg)
        return False