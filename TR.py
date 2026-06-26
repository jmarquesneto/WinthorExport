import pyautogui
import pyperclip
import time
import os
import shutil
import csv
import importlib
import win32com.client
import sys
import logging
import locale
import json
import yaml
from datetime import datetime, timedelta
from pywinauto.application import Application
from getpass import getpass
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Addons'))
sys.path.insert(0, r'02 - Rotinas')

from acoes_winthor import (
    abrir_appcontroller,
    clicar_imagem,
    aguardar_imagem,
    pasta_exportacao,
)

from TransArquivos import (
    compilar8598,
    transferBdRotinas,
)

def carregar_rotina(nome):
    return importlib.import_module(nome)

#------------------------------------------------------------------
#INPUT DAS INFORMAÇÕES
#------------------------------------------------------------------
def gerarRelatorio():
    dtInicio = input("Digite a data de início (dd/mm/aaaa): ")
    dtFinal = input("Digite a data final (dd/mm/aaaa): ")
    dtEstInicio = input("Digite a data de início do estoque (dd/mm/aaaa): ")
    return dtInicio, dtFinal, dtEstInicio

def agendarRelatorio():
    dtGerar = input("\nDigite a data de geração (dd/mm/aaaa): ")
    hrGerar = input("Digite a hora de geração (hh:mm): ")
    agendado = datetime.strptime(f'{dtGerar} {hrGerar}', '%d/%m/%Y %H:%M')
    agora = datetime.now()
    if agendado <= agora:
        print("\nData/hora já passou, iniciando imediatamente...")
        return
    espera = (agendado - agora).total_seconds()
    print(f"\nAguardando até {agendado.strftime('%d/%m/%Y %H:%M')} para iniciar... ({int(espera // 3600)}h {int((espera % 3600) // 60)}m)")
    time.sleep(espera)


if __name__ == "__main__":

    #INPUT DOS DADOS
    dtInicio, dtFinal, dtEstInicio = gerarRelatorio()

    #CREDENCIAIS
    usuario = input("\n > Digite seu usuário do Winthor: ").upper()
    while True:
        senha = getpass(" > Digite sua senha do Winthor: ")
        senha_confirm = getpass(" > Confirme sua senha: ")
        if senha == senha_confirm:
            print("Senha confirmada.")
            break
        print("As senhas não coincidem. Tente novamente.")

    #AGENDAR RELATORIO
    agendarRelatorio()

    #INICIO CONTABILIZAR TEMPO
    start = datetime.now()
    print(f"\n > Início da execução: {start.strftime('%d/%m/%Y %H:%M:%S')}")

    #ABRIR WINTHOR
    time.sleep(2)
    abrir_appcontroller(usuario, senha)

    #GERAR E EXPORTAR ROTINAS
    carregar_rotina('8588').g8588(dtInicio, dtFinal)
    carregar_rotina('8588').e8588(dtInicio)

    carregar_rotina('8524').g8524(dtInicio, dtFinal)
    carregar_rotina('8524').e8524(dtInicio, dtFinal)

    carregar_rotina('8680').g8680(dtInicio, dtFinal)
    carregar_rotina('8680').e8680(dtInicio, dtFinal)

    carregar_rotina('8688').g8688(dtInicio, dtFinal)
    carregar_rotina('8688').e8688(dtInicio, dtFinal)

    carregar_rotina('8685').g8685(dtInicio, dtFinal, dtEstInicio)
    carregar_rotina('8685').e8685(dtInicio, dtFinal, dtEstInicio)

    carregar_rotina('8770').g8770(dtInicio, dtFinal)
    carregar_rotina('8770').e8770(dtInicio, dtFinal)

    carregar_rotina('8796').g8796(dtInicio, dtFinal)
    carregar_rotina('8796').e8796(dtInicio, dtFinal)

    carregar_rotina('8551_1').g8551_1(dtInicio, dtFinal)
    carregar_rotina('8551_1').e8551_1(dtInicio, dtFinal)

    carregar_rotina('8551_4').g8551_4(dtInicio, dtFinal)
    carregar_rotina('8551_4').e8551_4(dtInicio, dtFinal)

    rotina_8598 = carregar_rotina('8598')
    partes_8598 = rotina_8598.particionar_datas(dtInicio, dtFinal)
    for i, (ini, fim) in enumerate(partes_8598, 1):
        parte = None if i == 1 else i
        rotina_8598.g8598(ini, fim)
        rotina_8598.e8598(ini, fim, parte=parte)
    
    carregar_rotina('8536_1').g8536_1(dtInicio, dtFinal)
    time.sleep(5)
    print("\n > Clicando no botão Conectar")
    if not clicar_imagem('LogoTotvs2.PNG, duplo=True'):
        print("Botão não encontrado!")
    carregar_rotina('8536_4').g8536_4(dtInicio, dtFinal)

    carregar_rotina('8536_4').e8536_4(dtInicio, dtFinal)
    carregar_rotina('8536_1').e8536_1(dtInicio, dtFinal)

    #FINAL CONTABILIZAR TEMPO
    stop = datetime.now()
    print(f"\n > Término da execução: {stop.strftime('%d/%m/%Y %H:%M:%S')}")
    tempo_total = stop - start
    print(f" > Tempo total de execução: {tempo_total}")

    compilar8598(dtInicio)

    transferBdRotinas()

    transferBdRotinas(dtInicio)