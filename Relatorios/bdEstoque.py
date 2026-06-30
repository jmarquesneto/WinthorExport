import win32com.client
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Addons'))
from acoes_winthor import MESES_PT
from config import CAMINHO_BD_VDA

NOME_ARQUIVO = '02. ESTOQUE DIARIO_JUNHO_2026.xlsb'

def atualizar_bd_estoque(dtInicio):
    data = datetime.strptime(dtInicio, '%d/%m/%Y')

    ano = data.strftime('%Y')
    mes = f"{data.month:02d} - {MESES_PT[data.month]}"
    caminho = os.path.join(CAMINHO_BD_VDA, ano, mes, NOME_ARQUIVO)

    if not os.path.exists(caminho):
        print(f" > Arquivo não encontrado: {NOME_ARQUIVO}")
        return False

    print(f"\n > Abrindo: {NOME_ARQUIVO}")
    excel = win32com.client.Dispatch('Excel.Application')
    excel.Visible = False

    wb = excel.Workbooks.Open(Filename=caminho)

    print("    - Atualizando consulta (8685 - ESTOQUE HISTÓRICO (SUBCATEGORIA))...")
    for conn in wb.Connections:
        try:
            conn.OLEDBConnection.BackgroundQuery = False
        except Exception:
            pass
    wb.RefreshAll()
    excel.CalculateUntilAsyncQueriesDone()
    print("    - Consulta atualizada.")

    wb.Save()
    wb.Close(SaveChanges=False)
    excel.Quit()

    print("    - Estoque atualizado, salvo e fechado com sucesso.")
    return True
