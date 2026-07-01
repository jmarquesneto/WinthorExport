import win32com.client
import os
import sys
import time
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Addons'))
from acoes_winthor import MESES_PT
from config import CAMINHO_BD_VDA, CAMINHO_RELATORIOS

CAMINHO_QUEBRA = os.path.join(CAMINHO_RELATORIOS, 'Operações', 'Quebra')

def atualizar_ajuste_quebra(dtInicio):
    data = datetime.strptime(dtInicio, '%d/%m/%Y')
    ano = data.strftime('%Y')

    nome_arquivo = f"AJUSTE QUEBRA DESCONHECIDA {ano}.xlsx"
    caminho = os.path.join(CAMINHO_QUEBRA, ano, '05 - AJUSTE QUEBRA DESCONHECIDA', nome_arquivo)

    if not os.path.exists(caminho):
        print(f"\n > Arquivo não encontrado: {nome_arquivo}")
        return False

    print(f"\n > Abrindo: {nome_arquivo}")
    excel = win32com.client.Dispatch('Excel.Application')
    excel.Visible = False

    wb = excel.Workbooks.Open(Filename=caminho)

    for nome_aba in ['BASE']:
        try:
            ws = wb.Sheets(nome_aba)
            for tabela in ws.PivotTables():
                tabela.PivotCache().Refresh()
            print(f"    - Aba '{nome_aba}' atualizada.")
        except Exception as e:
            print(f"    - Erro ao atualizar aba '{nome_aba}': {e}")

    try:
        ws = wb.Sheets('AJUSTE')
        for tabela in ws.PivotTables():
            tabela.RefreshTable()
        print("    - Tabela dinâmica 'AJUSTE' atualizada.")
    except Exception as e:
        print(f"    - Erro ao atualizar tabela dinâmica 'AJUSTE': {e}")

    wb.Save()
    wb.Close(SaveChanges=False)
    excel.Quit()

    print("    - Ajustes de Quebra atualizados, salvos e arquivo fechado.")
    return True


def atualizar_acordos_quebra(dtInicio):
    data = datetime.strptime(dtInicio, '%d/%m/%Y')
    ano = data.strftime('%Y')

    nome_arquivo = "ACORDOS QUEBRA.xlsx"
    caminho = os.path.join(CAMINHO_QUEBRA, ano, '03 - ACORDOS QUEBRA', nome_arquivo)

    if not os.path.exists(caminho):
        print(f"\n > Arquivo não encontrado: {nome_arquivo}")
        return False

    print(f"\n > Abrindo: {nome_arquivo}")
    excel = win32com.client.Dispatch('Excel.Application')
    excel.Visible = False

    wb = excel.Workbooks.Open(Filename=caminho)

    for nome_aba in ['8524 - ACORDOS', '8524 - IMPORT']:
        try:
            ws = wb.Sheets(nome_aba)
            for tabela in ws.PivotTables():
                tabela.PivotCache().Refresh()
            print(f"    - Aba '{nome_aba}' atualizada.")
        except Exception as e:
            print(f"    - Erro ao atualizar aba '{nome_aba}': {e}")

    wb.Save()
    wb.Close(SaveChanges=False)
    excel.Quit()

    print("    - Acordos de Quebra atualizados, salvos e arquivo fechado.")
    return True


def atualizar_ferramenta_quebra(dtInicio):
    data = datetime.strptime(dtInicio, '%d/%m/%Y')

    ano      = data.strftime('%Y')
    mes_num  = f"{data.month:02d}"
    mes      = f"{mes_num} - {MESES_PT[data.month]}"
    mes_nome = MESES_PT[data.month].upper()

    nome_bd_venda = f"01. BD_VENDA_{mes_nome}_{ano}.xlsb"
    caminho_bd_venda = os.path.join(CAMINHO_BD_VDA, ano, mes, nome_bd_venda)

    nome_arquivo = f"FERRAMENTA DE QUEBRA - {ano}.{mes_num}.xlsb"
    caminho = os.path.join(CAMINHO_QUEBRA, ano, nome_arquivo)

    if not os.path.exists(caminho_bd_venda):
        print(f"\n > Arquivo não encontrado: {nome_bd_venda}")
        return False

    if not os.path.exists(caminho):
        print(f"\n > Arquivo não encontrado: {nome_arquivo}")
        return False

    print(f"\n > Abrindo: {nome_bd_venda} (fonte das tabelas dinâmicas)")
    excel = win32com.client.Dispatch('Excel.Application')
    excel.Visible = False

    wb_bd_venda = excel.Workbooks.Open(Filename=caminho_bd_venda)

    print(f"    - Abrindo: {nome_arquivo}")
    wb = excel.Workbooks.Open(Filename=caminho)

    for conn in wb.Connections:
        try:
            conn.Refresh()
        except Exception as e:
            print(f"    - Erro ao atualizar conexão: {e}")
    excel.CalculateUntilAsyncQueriesDone()

    for nome_aba in ['AJUSTE', 'VISÃO - ENCARREGADO']:
        try:
            ws = wb.Sheets(nome_aba)
            for tabela in ws.PivotTables():
                tabela.RefreshTable()
            print(f"    - Tabela dinâmica '{nome_aba}' atualizada.")
        except Exception as e:
            print(f"    - Erro ao atualizar tabela dinâmica '{nome_aba}': {e}")

    wb.Save()
    wb.Close(SaveChanges=False)

    wb_bd_venda.Close(SaveChanges=False)
    excel.Quit()

    print("    - Ferramenta de Quebra atualizada, salva e fechada com sucesso.")
    return True
