import pyautogui
import pyperclip
import time
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Addons'))
from acoes_winthor import pasta_exportacao, aguardar_imagem

#------------------------------------------------------------------
#GERAR
#------------------------------------------------------------------

def g8588(dtInicio, dtFinal):
    print("\n > Iniciando rotina 8588 Loja 1 & 4")
    time.sleep(5)
    pyautogui.write('8588')
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.write(dtInicio)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(dtFinal)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('F3')
    time.sleep(2)

#------------------------------------------------------------------
#EXPORTAR
#------------------------------------------------------------------

def e8588(dtInicio):
    print("     - Aguardando geração do relatório 8588 Loja 1 & 4...")
    if not aguardar_imagem('Concluido.PNG', timeout=30):
        print("       - Aviso: tela de conclusão não detectada, prosseguindo mesmo assim.")
    print("     - Exportando rotina 8588 Loja 1 & 4")
    caminho = pasta_exportacao(para_winthor=True)
    
    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.press('i')
    time.sleep(0.2)
    pyautogui.press('a')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(10)
    pyperclip.copy(caminho)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.write('8588 - CUPOM, TKM E CESTA MEDIA POR DIA')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('left')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(30)
    pyautogui.hotkey('alt', 'f')
    time.sleep(5)
    pyautogui.hotkey('alt', 'f')
    print("     - Finalizado rotina 8588 Loja 1 & 4")