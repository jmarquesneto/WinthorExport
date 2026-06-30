import win32com.client
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Addons'))
from acoes_winthor import MESES_PT
from config import CAMINHO_BD_VDA

NOME_ARQUIVO = '07. VENDA TELEMARKETING - A. CATRAMBI.xlsx'

def atualizar_vda_tlmk(dtInicio):
    data = datetime.strptime(dtInicio, '%d/%m/%Y')

    ano = data.strftime('%Y')
    mes = f"{data.month:02d} - {MESES_PT[data.month]}"
    caminho = os.path.join(CAMINHO_BD_VDA, ano, mes, NOME_ARQUIVO)

    if not os.path.exists(caminho):
        print(f"\n > Arquivo não encontrado: {NOME_ARQUIVO}")
        return False

    print(f"\n > Abrindo: {NOME_ARQUIVO}")
    excel = win32com.client.Dispatch('Excel.Application')
    excel.Visible = False

    wb = excel.Workbooks.Open(Filename=caminho)

    print("    - Atualizando consultas (DB VDA TMKT | 8770 - AV (PRODUTO))...")
    for conn in wb.Connections:
        try:
            conn.OLEDBConnection.BackgroundQuery = False
        except Exception:
            pass
    wb.RefreshAll()
    excel.CalculateUntilAsyncQueriesDone()
    print("    - Consultas atualizadas.")

    wb.Save()
    wb.Close(SaveChanges=False)
    excel.Quit()

    print("    - Venda Telemarketing atualizada, salva e fechada com sucesso.")
    return True
