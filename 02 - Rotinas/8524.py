import pyautogui
import pyperclip
import time
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Addons'))
from acoes_winthor import pasta_exportacao

#------------------------------------------------------------------
#GERAR
#------------------------------------------------------------------

def g8524(dtInicio, dtFinal):
    print("\n > Iniciando 8524 Loja 1 & 4")
    time.sleep(1)
    pyautogui.write('8524')
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.write('01/01/2026')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(dtFinal)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('space')
    pyautogui.press('down')
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('down', presses=3)
    time.sleep(1)
    pyautogui.press('space')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab', presses=2)
    time.sleep(1)
    pyautogui.press('enter')

#------------------------------------------------------------------
#EXPORTAR
#------------------------------------------------------------------

def e8524(dtInicio, dtFinal):
    print("     - Aguardando 30seg para exportar 8524")
    time.sleep(30)
    print("     - Exportando rotina 8524")
    caminho = pasta_exportacao(para_winthor=True)

    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.press('i')
    time.sleep(0.2)
    pyautogui.press('a')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(10)
    pyautogui.write('8524')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('left')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(60)
    pyautogui.hotkey('alt', 'f')
    time.sleep(5)
    pyautogui.hotkey('alt', 'f')
    print("     - Finalizado rotina 8524")
