import win32com.client
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Addons'))
from acoes_winthor import MESES_PT
from config import CAMINHO_BD_VDA, CAMINHO_RELATORIOS

def atualizar_ferramentas(dtInicio):
    data = datetime.strptime(dtInicio, '%d/%m/%Y')

    ano      = data.strftime('%Y')
    mes_num  = f"{data.month:02d}"
    mes      = f"{mes_num} - {MESES_PT[data.month]}"
    mes_nome = MESES_PT[data.month].upper()

    nome_bd_venda = f"01. BD_VENDA_{mes_nome}_{ano}.xlsb"
    caminho_bd_venda = os.path.join(CAMINHO_BD_VDA, ano, mes, nome_bd_venda)

    pasta_comercial = os.path.join(CAMINHO_RELATORIOS, 'Comercial', 'Venda', ano, mes)
    pasta_operacoes = os.path.join(CAMINHO_RELATORIOS, 'Operações', 'Venda', ano, mes)

    arquivos = [
        os.path.join(pasta_comercial, f"FERRAMENTA COMERCIAL_{mes_nome}_{ano}.xlsb"),
        os.path.join(pasta_comercial, f"01. Relatório Venda {mes_nome}_{ano} - Loja 01.xlsb"),
        os.path.join(pasta_comercial, f"02. Relatório Venda {mes_nome}_{ano} - Loja 02 - 146.xlsm"),
        os.path.join(pasta_operacoes, f"FERRAMENTA DE VENDAS - OPERAÇÕES - {mes_num}.{ano}.xlsb"),
    ]

    if not os.path.exists(caminho_bd_venda):
        print(f"\n > Arquivo não encontrado: {nome_bd_venda}")
        return False

    print(f"\n > Abrindo: {nome_bd_venda} (fonte das tabelas dinâmicas)")
    excel = win32com.client.Dispatch('Excel.Application')
    excel.Visible = False

    wb_bd_venda = excel.Workbooks.Open(Filename=caminho_bd_venda)

    for caminho in arquivos:
        nome_arquivo = os.path.basename(caminho)

        if not os.path.exists(caminho):
            print(f"    - Arquivo não encontrado: {nome_arquivo}")
            continue

        print(f"    - Abrindo: {nome_arquivo}")
        wb = excel.Workbooks.Open(Filename=caminho)

        for conn in wb.Connections:
            try:
                conn.OLEDBConnection.BackgroundQuery = False
            except Exception:
                pass
        wb.RefreshAll()
        excel.CalculateUntilAsyncQueriesDone()

        wb.Save()
        wb.Close(SaveChanges=False)
        print(f"      - {nome_arquivo} atualizado, salvo e fechado com sucesso.")

    wb_bd_venda.Close(SaveChanges=False)
    excel.Quit()

    print("    - Ferramentas atualizadas com sucesso.")
    return True
