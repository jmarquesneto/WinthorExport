import pyautogui
import pyperclip
import time
import sys
import os
from datetime import datetime, timedelta
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Addons'))
from acoes_winthor import pasta_exportacao, aguardar_imagem

def fechamento(dtInicio):
    data = datetime.strptime(dtInicio, '%d/%m/%Y')
    primeiro_dia_mes_atual = data.replace(day=1)
    ultimo_dia_mes_anterior = primeiro_dia_mes_atual - timedelta(days=1)
    primeiro_dia_mes_anterior = ultimo_dia_mes_anterior.replace(day=1)

    dtInicio = primeiro_dia_mes_anterior.strftime('%d/%m/%Y')
    dtFinal = ultimo_dia_mes_anterior.strftime('%d/%m/%Y')

    #------------------------------------------------------------------
    #8536 FECHAMENTO LOJA 1
    #------------------------------------------------------------------
    # GERAR
    print("\n > Iniciando 8536 Fechamento Loja 1")
    time.sleep(5)

    pyautogui.write('8536')
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.write(dtInicio)
    pyautogui.press('enter')
    pyautogui.write(dtFinal)
    pyautogui.press('tab', presses=2)
    time.sleep(1)
    pyautogui.press('enter')

    # EXPORTAR
    print("     - Aguardando geração do relatório 8536 Fechamento Loja 1")
    if not aguardar_imagem('Concluido.PNG', timeout=3600):
        print("       - Aviso: tela de conclusão não detectada, prosseguindo mesmo assim.")
    print("     - Exportando rotina 8536 Fechamento Loja 1")
    caminho = pasta_exportacao(para_winthor=True)

    dtFormatada = datetime.strptime(dtInicio, '%d/%m/%Y').strftime('%Y.%m')

    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.press('i')
    time.sleep(0.2)
    pyautogui.press('a')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(10)
    pyautogui.write(f'8536 - {dtFormatada}')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('left')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(90)
    pyautogui.hotkey('alt', 'f')
    time.sleep(5)
    pyautogui.hotkey('alt', 'f')
    print("     - Finalizado rotina 8536 Fechamento Loja 1")

    #------------------------------------------------------------------
    #8536 FECHAMENTO LOJA 4
    #------------------------------------------------------------------
    # GERAR
    print("\n > Iniciando 8536 Fechamento Loja 4")
    time.sleep(5)

    pyautogui.write('8536')
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.write(dtInicio)
    pyautogui.press('enter')
    pyautogui.write(dtFinal)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('4')
    time.sleep(1)
    pyautogui.press('tab', presses=2)
    time.sleep(1)
    pyautogui.press('enter')

    # EXPORTAR
    print("     - Aguardando geração do relatório 8536 Fechamento Loja 4")
    if not aguardar_imagem('Concluido.PNG', timeout=3600):
        print("       - Aviso: tela de conclusão não detectada, prosseguindo mesmo assim.")
    print("     - Exportando rotina 8536 Fechamento Loja 4")
    caminho = pasta_exportacao(para_winthor=True)

    dtFormatada = datetime.strptime(dtInicio, '%d/%m/%Y').strftime('%Y.%m')

    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.press('i')
    time.sleep(0.2)
    pyautogui.press('a')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(10)
    pyautogui.write(f'8536 02 - {dtFormatada}')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('left')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(90)
    pyautogui.hotkey('alt', 'f')
    time.sleep(5)
    pyautogui.hotkey('alt', 'f')
    print("     - Finalizado rotina 8536 Fechamento Loja 4")

    #------------------------------------------------------------------
    #8551 FECHAMENTO LOJA 1
    #------------------------------------------------------------------
    # GERAR
    print("\n > Iniciando 8551 Fechamento Loja 1")
    time.sleep(5)

    pyautogui.write('8551')
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.write(dtInicio)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(dtFinal)
    time.sleep(1.5)
    pyautogui.press('enter', presses=3)
    time.sleep(5)
    pyautogui.write('1')
    time.sleep(1)
    pyautogui.press('space')
    pyautogui.press('enter')
    pyautogui.press('tab', presses=2)
    time.sleep(1)
    pyautogui.press('enter')

    # EXPORTAR
    print("     - Aguardando geração do relatório 8551 Fechamento Loja 1")
    if not aguardar_imagem('Concluido.PNG', timeout=300):
        print("       - Aviso: tela de conclusão não detectada, prosseguindo mesmo assim.")
    print("     - Exportando rotina 8551 Fechamento Loja 1")
    caminho = pasta_exportacao(para_winthor=True)

    dtFormatada = datetime.strptime(dtInicio, '%d/%m/%Y').strftime('%Y.%m')

    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.press('i')
    time.sleep(0.2)
    pyautogui.press('a')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(10)
    pyautogui.write(f'8551 - {dtFormatada}')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('left')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(90)
    pyautogui.hotkey('alt', 'f')
    time.sleep(5)
    pyautogui.hotkey('alt', 'f')
    print("     - Finalizado rotina 8551 Fechamento Loja 1")

    #------------------------------------------------------------------
    #8551 FECHAMENTO LOJA 4
    #------------------------------------------------------------------
    # GERAR
    print("\n > Iniciando 8551 Fechamento Loja 4")
    time.sleep(5)

    pyautogui.write('8551')
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.write(dtInicio)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(dtFinal)
    time.sleep(1.5)
    pyautogui.press('enter', presses=3)
    time.sleep(5)
    pyautogui.write('4')
    time.sleep(1)
    pyautogui.press('space')
    pyautogui.press('enter')
    pyautogui.press('tab', presses=2)
    time.sleep(1)
    pyautogui.press('enter')

    # EXPORTAR
    print("     - Aguardando geração do relatório 8551 Fechamento Loja 4")
    if not aguardar_imagem('Concluido.PNG', timeout=300):
        print("       - Aviso: tela de conclusão não detectada, prosseguindo mesmo assim.")
    print("     - Exportando rotina 8551 Fechamento Loja 4")
    caminho = pasta_exportacao(para_winthor=True)

    dtFormatada = datetime.strptime(dtInicio, '%d/%m/%Y').strftime('%Y.%m')

    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.press('i')
    time.sleep(0.2)
    pyautogui.press('a')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(10)
    pyautogui.write(f'8551 02 - {dtFormatada}')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('left')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(90)
    pyautogui.hotkey('alt', 'f')
    time.sleep(5)
    pyautogui.hotkey('alt', 'f')
    print("     - Finalizado rotina 8551 Fechamento Loja 4")