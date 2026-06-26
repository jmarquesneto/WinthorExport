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

def g8685(dtInicio, dtFinal, dtEstInicio):
    print("\n > Iniciando rotina 8685 Loja 1 & 4")
    time.sleep(5)

    pyautogui.write('8685')
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.write(dtEstInicio)
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
    pyautogui.press('tab', presses=2)
    time.sleep(1)
    pyautogui.press('enter')


#------------------------------------------------------------------
#EXPORTAR
#------------------------------------------------------------------

def e8685(dtInicio, dtFinal, dtEstInicio):
    time.sleep(480)
    print("\n > Exportando rotina 8685 Loja 1 & 4")
    caminho = pasta_exportacao(para_winthor=True)

    from datetime import datetime
    if isinstance(dtFinal, str):
        dtFinal = datetime.strptime(dtFinal, "%d/%m/%Y")
    dtFormatada = dtFinal.strftime("%Y.%m.%d")
    
    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.press('i')
    time.sleep(0.2)
    pyautogui.press('a')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(10)
    pyautogui.write(f'8685 - {dtFormatada}')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('left')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(90)
    pyautogui.hotkey('alt', 'f')
    time.sleep(5)
    pyautogui.hotkey('alt', 'f')
    time.sleep(20)

    print("\n > Finalizado rotina 8685 Loja 1 & 4")
