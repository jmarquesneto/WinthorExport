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

def g8770(dtInicio, dtFinal):
    print("\n > Iniciando 8770 Loja 1")
    time.sleep(5)

    pyautogui.write('8770')
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.write(dtInicio)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(dtFinal)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab', presses=2)
    time.sleep(1)
    pyautogui.press('enter')

#------------------------------------------------------------------
#EXPORTAR
#------------------------------------------------------------------

def e8770(dtInicio, dtFinal):
    print("     - Aguardando 30seg para exportar 8770 Loja 1")
    time.sleep(30)
    print("     - Exportando rotina 8770 Loja 1")
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
    pyautogui.write(f'8770 - {dtFormatada}')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('left')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(90)
    pyautogui.hotkey('alt', 'f')
    time.sleep(5)
    pyautogui.hotkey('alt', 'f')

    print("     - Finalizado rotina 8770 Loja 1")


