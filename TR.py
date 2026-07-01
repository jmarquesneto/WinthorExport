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

from Relatorios.vdaTLMK import atualizar_vda_tlmk
from Relatorios.bdEstoque import atualizar_bd_estoque
from Relatorios.bdVDA import atualizar_bd_venda
from Relatorios.ferramentas import atualizar_ferramentas
from Relatorios.quebra import (
    atualizar_ajuste_quebra,
    atualizar_acordos_quebra,
    atualizar_ferramenta_quebra,
)

def carregar_rotina(nome):
    return importlib.import_module(nome)

#------------------------------------------------------------------
#LOG
#------------------------------------------------------------------
class _Tee:
    """Espelha stdout para o terminal e para um arquivo de log simultaneamente."""
    def __init__(self, *streams):
        self._streams = streams
    def write(self, data):
        for s in self._streams:
            s.write(data)
    def flush(self):
        for s in self._streams:
            s.flush()

def _iniciar_log():
    log_dir = Path(__file__).parent / 'Logs'
    log_dir.mkdir(exist_ok=True)
    log_path = log_dir / f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    log_file = open(log_path, 'w', encoding='utf-8')
    sys.stdout = _Tee(sys.__stdout__, log_file)
    print(f" > Log iniciado: {log_path}")
    return log_file

def _encerrar_log(log_file):
    sys.stdout = sys.__stdout__
    log_file.close()

#------------------------------------------------------------------
#INPUT DAS INFORMAÇÕES
#------------------------------------------------------------------
def _ler_data(prompt):
    while True:
        valor = input(prompt).strip()
        try:
            datetime.strptime(valor, '%d/%m/%Y')
            return valor
        except ValueError:
            print("   [!] Data inválida. Use o formato dd/mm/aaaa (ex: 01/06/2026).")

def _ler_hora(prompt):
    while True:
        valor = input(prompt).strip()
        try:
            datetime.strptime(valor, '%H:%M')
            return valor
        except ValueError:
            print("   [!] Hora inválida. Use o formato hh:mm (ex: 03:00).")

def gerarRelatorio():
    dtInicio = _ler_data("Digite a data de início (dd/mm/aaaa): ")
    dtFinal = _ler_data("Digite a data final (dd/mm/aaaa): ")
    dtEstInicio = _ler_data("Digite a data de início do estoque (dd/mm/aaaa): ")
    return dtInicio, dtFinal, dtEstInicio

def agendarRelatorio():
    dtGerar = _ler_data("\nDigite a data de geração (dd/mm/aaaa): ")
    hrGerar = _ler_hora("Digite a hora de geração (hh:mm): ")
    agendado = datetime.strptime(f'{dtGerar} {hrGerar}', '%d/%m/%Y %H:%M')
    agora = datetime.now()
    if agendado <= agora:
        print("    - Data/hora já passou, iniciando imediatamente...")
        return
    espera = (agendado - agora).total_seconds()
    print(f"    - Aguardando até {agendado.strftime('%d/%m/%Y %H:%M')} para iniciar... ({int(espera // 3600)}h {int((espera % 3600) // 60)}m)")
    time.sleep(espera)


if __name__ == "__main__":

    #INPUT DOS DADOS
    dtInicio, dtFinal, dtEstInicio = gerarRelatorio()

    log_file = _iniciar_log()

    #CREDENCIAIS
    usuario = input("\n > Digite seu usuário do Winthor: ").upper()
    while True:
        senha = getpass("    - Digite sua senha do Winthor: ")
        senha_confirm = getpass("    - Confirme sua senha: ")
        if senha == senha_confirm:
            print("\n      - Senha confirmada.")
            break
        print("\n      [!] As senhas não coincidem. Tente novamente.")

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
    carregar_rotina('8536_1').e8536_1(dtInicio, dtFinal)

    carregar_rotina('8536_4').g8536_4(dtInicio, dtFinal)
    carregar_rotina('8536_4').e8536_4(dtInicio, dtFinal)


    #FINAL CONTABILIZAR TEMPO (GERAR E EXPORTAR)
    stop1 = datetime.now()
    print(f"\n > Término de gerar e exportar: {stop1.strftime('%d/%m/%Y %H:%M:%S')}")
    tempo_total = stop1 - start
    print(f"    - Tempo de execução: {tempo_total}")

    compilar8598(dtInicio)

    transferBdRotinas(dtInicio, dtFinal)
    time.sleep(2)
    atualizar_vda_tlmk(dtInicio)
    time.sleep(2)
    atualizar_bd_estoque(dtInicio)
    time.sleep(2)
    atualizar_bd_venda(dtInicio)
    time.sleep(2)
    atualizar_ferramentas(dtInicio)
    time.sleep(2)
    atualizar_ajuste_quebra(dtInicio)
    time.sleep(2)
    atualizar_acordos_quebra(dtInicio)
    time.sleep(2)
    atualizar_ferramenta_quebra(dtInicio)

    #FINAL CONTABILIZAR TEMPO TOTAL
    stop2 = datetime.now()
    print(f"\n > Término: {stop2.strftime('%d/%m/%Y %H:%M:%S')}")
    tempo_total = stop2 - start
    print(f"    - Tempo total de execução: {tempo_total}")

    _encerrar_log(log_file)