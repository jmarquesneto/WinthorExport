import sys
import os
import shutil
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from acoes_winthor import PASTA_BASE_EXPORT, MESES_PT
from config import CAMINHO_BD

#------------------------------------------------------------------
#COMPILAR TODAS AS PARTES DO RELATÓRIO 8598
#------------------------------------------------------------------
def compilar8598(dtInicio):
    time.sleep(2)

    # pasta = data de hoje (igual ao pasta_exportacao() sem argumento no e8598)
    hoje = datetime.today()
    ano  = hoje.strftime('%Y')
    mes  = f"{hoje.month:02d} - {MESES_PT[hoje.month]}"
    dia  = hoje.strftime('%Y-%m-%d')
    pasta = os.path.join(PASTA_BASE_EXPORT, ano, mes, dia)

    # nome do arquivo usa dtInicio para o formato AAAA.MM
    data = datetime.strptime(dtInicio, '%d/%m/%Y')
    dtFormatada = data.strftime('%Y.%m')
    nome_principal = f'8598 - {dtFormatada}.csv'
    caminho_principal = os.path.join(pasta, nome_principal)

    if not os.path.exists(caminho_principal):
        print(f"\n > Arquivo principal não encontrado: {nome_principal}")
        return

    print(f"\n > Compilando {nome_principal}")

    with open(caminho_principal, 'r', encoding='cp1252', newline='') as f:
        linhas_principal = f.readlines()

    for pt in [2, 3]:
        nome_parte = f'8598 - {dtFormatada} - PT{pt}.csv'
        caminho_parte = os.path.join(pasta, nome_parte)
        if os.path.exists(caminho_parte):
            with open(caminho_parte, 'r', encoding='cp1252', newline='') as f:
                linhas_parte = f.readlines()[1:]  # pula o cabeçalho
            linhas_principal.extend(linhas_parte)
            print(f"    > PT{pt} adicionada ({len(linhas_parte)} linhas)")

    with open(caminho_principal, 'w', encoding='cp1252', newline='') as f:
        f.writelines(linhas_principal)

    print(f"    > Compilação concluída: {nome_principal}")

#------------------------------------------------------------------
#TRANSFERIR ARQUIVOS PARA BD ROTINAS
#------------------------------------------------------------------
def transferBdRotinas(dtInicio):
    print('\n > Iniciando transferência dos arquivos...')

    hoje = datetime.today()
    pasta_origem = os.path.join(
        PASTA_BASE_EXPORT,
        hoje.strftime('%Y'),
        f"{hoje.month:02d} - {MESES_PT[hoje.month]}",
        hoje.strftime('%Y-%m-%d')
    )

    data      = datetime.strptime(dtInicio, '%d/%m/%Y')
    dtFmt     = data.strftime('%Y.%m')
    ano_ref   = data.strftime('%Y')
    mes_ref   = f"{data.month:02d} - {MESES_PT[data.month].upper()}"

    BD = CAMINHO_BD

    transferencias = [
        # Pasta raiz (sem ano/mês)
        (f'8588 - CUPOM, TKM E CESTA MEDIA POR DIA.csv', BD),
        (f'8680 - LOJAS - SEM AVARIA.csv',                BD),
        (f'8688 - Arvore Mercadologica.csv',               BD),
        # Com ano
        (f'8524.csv',                  os.path.join(BD, '8524', ano_ref)),
        (f'8770 - {dtFmt}.csv',        os.path.join(BD, '8770', ano_ref)),
        (f'8551 - {dtFmt}.csv',        os.path.join(BD, '8551', ano_ref)),
        (f'8551 02 - {dtFmt}.csv',     os.path.join(BD, '8551', ano_ref)),
        (f'8536 - {dtFmt}.csv',        os.path.join(BD, '8536', ano_ref)),
        (f'8536 02 - {dtFmt}.csv',     os.path.join(BD, '8536', ano_ref)),
        (f'8598 - {dtFmt}.csv',        os.path.join(BD, '8598', ano_ref)),
        # Com ano e mês
        (f'8685 - {dtFmt}.csv',        os.path.join(BD, '8685', ano_ref, mes_ref)),
    ]

    nao_encontrados = []

    for nome, destino in transferencias:
        origem = os.path.join(pasta_origem, nome)
        if os.path.exists(origem):
            os.makedirs(destino, exist_ok=True)
            shutil.copy2(origem, os.path.join(destino, nome))
            print(f"    > OK: {nome}")
        else:
            nao_encontrados.append(nome)

    if nao_encontrados:
        print(f"\n > {len(nao_encontrados)} arquivo(s) não encontrado(s):")
        for nome in nao_encontrados:
            print(f"    - {nome}")

    print('\n > Transferência concluída.')

