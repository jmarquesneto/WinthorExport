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

def g8688(dtInicio, dtFinal):
    print("\n > Iniciando rotina 8688 Loja 1 & 4")
    time.sleep(5)
    pyautogui.write('8688')
    pyautogui.press('enter')
    time.sleep(30)
    pyautogui.press('space')
    pyautogui.press('down')
    pyautogui.press('space')
    pyautogui.press('down', presses=2)
    time.sleep(1)
    pyautogui.press('space')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('A')
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

def e8688(dtInicio, dtFinal):
    print("     - Aguardando geração do relatório 8688 Loja 1 & 4...")
    if not aguardar_imagem('Concluido.PNG', timeout=180):
        print("       - Aviso: tela de conclusão não detectada, prosseguindo mesmo assim.")
    print("     - Exportando rotina 8688 Loja 1 & 4")
    caminho = pasta_exportacao(para_winthor=True)
    
    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.press('i')
    time.sleep(0.2)
    pyautogui.press('a')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    time.sleep(10)
    pyautogui.write('8688 - Arvore Mercadologica')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('left')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(60)
    pyautogui.hotkey('alt', 'f')
    time.sleep(5)
    pyautogui.hotkey('alt', 'f')
    time.sleep(20)
    print("     - Finalizado rotina 8688 Loja 1 & 4")
