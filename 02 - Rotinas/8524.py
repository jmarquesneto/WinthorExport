import pyautogui
import pyperclip
import time
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
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
    time.sleep(2)

#------------------------------------------------------------------
#EXPORTAR
#------------------------------------------------------------------

def e8524(dtInicio, dtFinal):
    time.sleep(30)
    print("\n > Exportando rotina 8524")
    caminho = pasta_exportacao(para_winthor=True)

    pyautogui.keyDown('alt')   # Pressiona e segura ALT
    time.sleep(0.2)            # Pequeno intervalo, opcional
    pyautogui.press('i')       # Pressiona a tecla I
    time.sleep(0.2)            # Pequeno intervalo entre as teclas
    pyautogui.press('a')       # Pressiona a tecla A
    time.sleep(0.2)
    pyautogui.keyUp('alt')     # Solta a tecla ALT
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
    print("\n > Finalizado rotina 8524")