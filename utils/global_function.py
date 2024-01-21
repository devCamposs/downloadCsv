# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------
NOME..: global_function.py
LANG..: Python3
TITULO: Funções prontas modulo global implementadas para projeto
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
import os
import requests
from os import path 
from glob import glob
from shutil import move
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def moveFile(sendData: dict) -> bool:
    """
        Função para mover um arquivo da pasta origrem para pathDest
    :param sendData: dict com parâmetros
    :param sendData['file']: (str) - nome do arquivo
    :param sendData['pathLocal']: (str) - path origem do arquivo
    :param sendData['pathLocalDest']: (str) - path pathDest do arquivo
    :return: (bool) - True or False
    
    Modelo de uso do sendData:

    sendData = {
        "file": file,
        "pathLocal": pathLocal,
        "pathLocalDest": pathLocalDest
    }
    """
    logger.info("=== Função: %s ===" % (sys._getframe().f_code.co_name))
    logger.info("=== Parâmetros recebidos ===")
    logger.info(f"file...............: {type(sendData['file'])}, content {sendData['file']}")
    logger.info(f"pathLocal..........: {type(sendData['pathLocal'])}, content {sendData['pathLocal']}")
    logger.info(f"pathLocalDest......: {type(sendData['pathLocalDest'])}, content {sendData['pathLocalDest']}")
    try:
        if not isinstance(sendData, dict):
            logger.error(f"sendData fora do padrão, type {type(sendData)}")
            return False

        for listItem in ['file', 'pathLocal', 'pathLocalDest']:
            if listItem not in sendData:
                logger.error("Parâmetros necessários não informados")
                return False

        if not path.exists(sendData['pathLocal']):
            logger.error("Pasta origem dos dados não existe")
            return False

        if not path.exists(sendData['pathLocalDest']):
            logger.error("Pasta pathDest dos dados não existe")
            return False

        if not path.exists(sendData['pathLocal']+sendData['file']):
            logger.error("Arquivo origem não existe")
            return False

        move(sendData['pathLocal'] + sendData['file'], sendData['pathLocalDest'] + sendData['file'])
        logger.warning(f"{sendData['file']} movido para a pasta {sendData['pathLocalDest']}")
        return True

    except BaseException as errorMsg:
        logger.error("Erro ao listar arquivos")
        logger.error("Exception occurred", exc_info=True)
        logger.error(errorMsg)
        return False

def downloadCsvFile(url: str, pathLocal: str) -> bool:
    """
    Função para baixar um arquivo CSV da internet e salvar localmente
    :param url: (str) - URL do arquivo CSV para download
    :param pathLocal: (str) - Pasta de destino para salvar o arquivo baixado
    :return: (bool) - True se o download for bem-sucedido, False caso contrário
    """
    logger.info("=== Função: %s ===" % (__name__))
    logger.info("=== Parâmetros recebidos ===")
    logger.info(f"==> VAR: url TYPE: {type(url)}, CONTENT: {url}")
    logger.info(f"==> VAR: pathLocal TYPE: {type(pathLocal)}, CONTENT: {pathLocal}")

    try:
        
        # if not url.lower().endswith('.csv'):
        #     logger.error("A URL fornecida não aponta para um arquivo CSV.")
        #     return False
        
        if not pathLocal:
            logger.error(f"Erro parâmetro ausente pathLocal")
            return False

        response = requests.get(url)
        if response.status_code == 200:
            nome_arquivo = os.path.basename(url)
            caminho_destino = os.path.join(pathLocal, nome_arquivo)
            with open(caminho_destino, 'wb') as arquivo_destino:
                arquivo_destino.write(response.content)
            logger.warning(f"Arquivo CSV baixado e salvo em {caminho_destino}")
            return True
        else:
            logger.error(f"Falha ao baixar o arquivo CSV. Código de status: {response.status_code}")
            return False

    except BaseException as errorMsg:
        logger.error("Erro ao baixar arquivo CSV")
        logger.error("Exception occurred", exc_info=True)
        logger.error(errorMsg)
        return False

def listFile(sendData: dict) -> list:
    """
    Função para coletar arquivos numa pasta.
    
    :param sendData: dict com parâmetros
    :param sendData['pathLocal']: (str) - path local.
    :param sendData['filePrefix']: (str) - prefixo para filtrar nome de arquivos.
    :param sendData['fileExtension']: (list) - com as extensões de arquivo para filtro.
    :param sendData['fileRules']: (str) - informa situações especiais para filtro.
    :return listFiles: (list) - com os arquivos ou vazia quando não tem arquivos.
    
    Modelo de uso do sendData:
    
    sendData = {
        "pathLocal": pathLocal,
        "filePrefix": filePrefix,
        "fileExtension": fileExtension,
        "fileRules": fileRules
    }
    """
    logger.info("=== Função: %s ===" % (sys._getframe().f_code.co_name))

    try:
        if 'pathLocal' not in sendData:
            logger.error(f"Erro PathLocal ausente em sendData")
            return False

        if 'fileExtension' not in sendData:
            sendData['fileExtension'] = ["*"]

        if 'fileRules' not in sendData:
            sendData['fileRules'] = ""

        if 'filePrefix' not in sendData:
            sendData['filePrefix'] = "*"

        if len(sendData['filePrefix'].strip()) == 0:
            sendData['filePrefix'] = "*"

        logger.info("=== Parâmetros recebidos ===")
        logger.warning(f"pathLocal type {type(sendData['pathLocal'])}, content {sendData['pathLocal']}")
        logger.warning(f"filePrefix type {type(sendData['filePrefix'])}, content {sendData['filePrefix']}")
        logger.warning(f"fileExtension type {type(sendData['fileExtension'])}, content {sendData['fileExtension']}")
        logger.warning(f"fileRules type {type(sendData['fileRules'])}, content {sendData['fileRules']}")

        logger.info("=== Valida se a pasta existe ===")
        if not path.exists(sendData['pathLocal']):
            logger.warning(f"Pasta {sendData['pathLocal']} não existe")
            return False
        logger.info("Pasta local existe")

        logger.info(f"=== Coletando arquivos na pasta {sendData['pathLocal']} ===")
        listFiles = list()

        for extension in sendData['fileExtension']:
            searchPattern = path.join(sendData['pathLocal'], sendData['filePrefix'] + extension)
            matchingFiles = glob(searchPattern, recursive=False)

            if matchingFiles:
                logger.info(f"Encontrados {len(matchingFiles)} arquivo(s) com extensão {extension}")
                for filePath in matchingFiles:
                    if path.isfile(filePath):  # Verifica se é um arquivo, não uma subpasta
                        fileName = path.basename(filePath)
                        listFiles.append(fileName)
            else:
                logger.info(f"Nenhum arquivo encontrado com extensão {extension}")

    except BaseException as errorMsg:
        logger.error("Erro ao listar arquivos")
        logger.error("Exception occurred", exc_info=True)
        logger.error(errorMsg)
        return False

    logger.warning(f"listFiles type {type(listFiles)}, len {len(listFiles)}")

    return listFiles
