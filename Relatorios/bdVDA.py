import win32com.client
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Addons'))
from acoes_winthor import MESES_PT
from config import CAMINHO_BD_VDA, CAMINHO_BD

def atualizar_bd_venda(dtInicio):
    data = datetime.strptime(dtInicio, '%d/%m/%Y')

    ano     = data.strftime('%Y')
    ano_mes = f"{ano}.{data.month:02d}"
    mes     = f"{data.month:02d} - {MESES_PT[data.month]}"
    nome_arquivo = f"01. BD_VENDA_{MESES_PT[data.month].upper()}_{ano}.xlsb"
    caminho = os.path.join(CAMINHO_BD_VDA, ano, mes, nome_arquivo)

    csvs = [
        os.path.join(CAMINHO_BD, '8536', ano, f'8536 - {ano_mes}.csv'),
        os.path.join(CAMINHO_BD, '8536', ano, f'8536 02 - {ano_mes}.csv'),
        os.path.join(CAMINHO_BD, '8598', ano, f'8598 - {ano_mes}.csv'),
    ]

    if not os.path.exists(caminho):
        print(f" > Arquivo não encontrado: {nome_arquivo}")
        return False

    print(f"\n > Abrindo: {nome_arquivo}")
    excel = win32com.client.Dispatch('Excel.Application')
    excel.Visible = False

    wbs_csv = []
    for csv_path in csvs:
        if os.path.exists(csv_path):
            print(f"    - Abrindo: {os.path.basename(csv_path)}")
            wbs_csv.append(excel.Workbooks.Open(Filename=csv_path))
        else:
            print(f"    - CSV não encontrado: {os.path.basename(csv_path)}")

    wb = excel.Workbooks.Open(Filename=caminho)

    print("    - Atualizando consultas...")
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

    for wb_csv in wbs_csv:
        wb_csv.Close(SaveChanges=False)

    excel.Quit()

    print("    - BD Venda atualizado, salvo e fechado com sucesso.")
    return True
