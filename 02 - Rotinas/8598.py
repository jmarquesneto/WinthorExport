import pyautogui
import pyperclip
import time
import sys
import os
from datetime import datetime, timedelta
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Addons'))
from acoes_winthor import pasta_exportacao, aguardar_imagem

#------------------------------------------------------------------
#PARTICIONAR DATAS (até 3 partes de 10 dias)
#------------------------------------------------------------------

def particionar_datas(dtInicio_str, dtFinal_str):
    fmt = '%d/%m/%Y'
    inicio = datetime.strptime(dtInicio_str, fmt)
    final = datetime.strptime(dtFinal_str, fmt)
    total_dias = (final - inicio).days + 1

    if total_dias <= 10:
        return [(dtInicio_str, dtFinal_str)]
    elif total_dias <= 20:
        meio = inicio + timedelta(days=9)
        pt2_inicio = inicio + timedelta(days=10)
        return [
            (inicio.strftime(fmt), meio.strftime(fmt)),
            (pt2_inicio.strftime(fmt), dtFinal_str),
        ]
    else:
        pt1_fim = inicio + timedelta(days=9)
        pt2_inicio = inicio + timedelta(days=10)
        pt2_fim = inicio + timedelta(days=19)
        pt3_inicio = inicio + timedelta(days=20)
        return [
            (dtInicio_str, pt1_fim.strftime(fmt)),
            (pt2_inicio.strftime(fmt), pt2_fim.strftime(fmt)),
            (pt3_inicio.strftime(fmt), dtFinal_str),
        ]

#------------------------------------------------------------------
#GERAR
#------------------------------------------------------------------

def g8598(dtInicio, dtFinal):
    print("\n > Iniciando 8598 Loja 4")
    time.sleep(5)

    pyautogui.write('8598')
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.press('4')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(dtInicio)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(dtFinal)
    time.sleep(1)
    pyautogui.press('tab', presses=2)
    time.sleep(1)
    pyautogui.press('enter')

#------------------------------------------------------------------
#EXPORTAR
#------------------------------------------------------------------

def e8598(dtInicio, dtFinal, parte=None):
    print("     - Aguardando geração do relatório 8598 Loja 4...")
    if not aguardar_imagem('Concluido.PNG', timeout=600):
        print("       - Aviso: tela de conclusão não detectada, prosseguindo mesmo assim.")
    print("     - Exportando rotina 8598 Loja 4")
    caminho = pasta_exportacao(para_winthor=True)

    dtFormatada = datetime.strptime(dtInicio, '%d/%m/%Y').strftime('%Y.%m')
    nome = f'8598 - {dtFormatada}' if parte is None else f'8598 - {dtFormatada} - PT{parte}'

    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.press('i')
    time.sleep(0.2)
    pyautogui.press('a')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(10)
    pyautogui.write(nome)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('left')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(90)
    pyautogui.hotkey('alt', 'f')
    time.sleep(5)
    pyautogui.hotkey('alt', 'f')

    print("     - Finalizado rotina 8598 Loja 4")
