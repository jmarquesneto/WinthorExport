import pyautogui
import pyperclip
import time
import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Addons'))
from acoes_winthor import pasta_exportacao

#------------------------------------------------------------------
#GERAR
#------------------------------------------------------------------

def g8551_1(dtInicio, dtFinal):
    print("\n > Iniciando 8551 Loja 1")
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

#------------------------------------------------------------------
#EXPORTAR
#------------------------------------------------------------------

def e8551_1(dtInicio, dtFinal):
    print("     - Aguardando 5min para exportar 8551 Loja 1")
    time.sleep(300)
    print("     - Exportando rotina 8551 Loja 1")
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

    print("     - Finalizado rotina 8551 Loja 1")
