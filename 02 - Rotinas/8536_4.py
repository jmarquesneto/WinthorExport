import pyautogui
import pyperclip
import time
import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Addons'))
from acoes_winthor import pasta_exportacao, aguardar_imagem

#------------------------------------------------------------------
#GERAR
#------------------------------------------------------------------

def g8536_4(dtInicio, dtFinal):
    print("\n > Iniciando 8536 Loja 4")
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

#------------------------------------------------------------------
#EXPORTAR
#------------------------------------------------------------------

def e8536_4(dtInicio, dtFinal):
    print("     - Aguardando geração do relatório 8536 Loja 4...")
    if not aguardar_imagem('Concluido.PNG', timeout=3600):
        print("       - Aviso: tela de conclusão não detectada, prosseguindo mesmo assim.")
    print("     - Exportando rotina 8536 Loja 4")
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

    print("     - Finalizado rotina 8536 Loja 4")
