import pyautogui
import subprocess
import time
import os
from datetime import datetime
from config import CAMINHO_EXPORT, CAMINHO_WINTHOR, SERVIDOR_WINTHOR

CONFIANCA = 0.85
PASTA_IMGS = '01 - Imgs'

PASTA_BASE_EXPORT  = CAMINHO_EXPORT
PASTA_BASE_WINTHOR = CAMINHO_WINTHOR

MESES_PT = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março',    4: 'Abril',
    5: 'Maio',    6: 'Junho',    7: 'Julho',      8: 'Agosto',
    9: 'Setembro',10: 'Outubro', 11: 'Novembro',  12: 'Dezembro'
}

def pasta_exportacao(data=None, para_winthor=False):
    time.sleep(2)
    if data is None:
        data = datetime.today()
    elif isinstance(data, str):
        data = datetime.strptime(data, '%d/%m/%Y')

    ano   = data.strftime('%Y')
    mes   = f"{data.month:02d} - {MESES_PT[data.month]}"
    dia   = data.strftime('%Y-%m-%d')

    caminho_local = os.path.join(PASTA_BASE_EXPORT, ano, mes, dia)
    os.makedirs(caminho_local, exist_ok=True)

    if para_winthor:
        return os.path.join(PASTA_BASE_WINTHOR, ano, mes, dia)
    return caminho_local


def clicar_imagem(caminho_img, confianca=CONFIANCA, timeout=10, duplo=False):
    """Procura a imagem na tela e clica nela. Retorna True se encontrou."""
    inicio = time.time()
    while time.time() - inicio < timeout:
        try:
            local = pyautogui.locateCenterOnScreen(
                f'{PASTA_IMGS}/{caminho_img}',
                confidence=confianca
            )
            if local:
                if duplo:
                    pyautogui.doubleClick(local)
                else:
                    pyautogui.click(local)
                return True
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.5)
    return False


def aguardar_imagem(caminho_img, confianca=CONFIANCA, timeout=15):
    """Aguarda uma imagem aparecer na tela sem clicar. Retorna True se encontrou."""
    inicio = time.time()
    while time.time() - inicio < timeout:
        try:
            local = pyautogui.locateCenterOnScreen(
                f'{PASTA_IMGS}/{caminho_img}',
                confidence=confianca
            )
            if local:
                return True
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.5)
    return False

#------------------------------------------------------------------
#ABRIR O APPCONTROLLER
#------------------------------------------------------------------
def abrir_appcontroller(usuario, senha):
    print("\n > Abrindo AppController")
    time.sleep(5)
    caminhoAppController = r"C:\Program Files (x86)\GraphOn\AppController\AppController.exe"
    subprocess.Popen([
        caminhoAppController,
        "-h",
        SERVIDOR_WINTHOR,
        "-c"
    ])

    time.sleep(5)
    print("\n > Clicando no botão Conectar")
    if not clicar_imagem('WinConectar.PNG'):
        print("Botão não encontrado!")

    time.sleep(5)
    print("\n > Redefinindo botão do Winthor")
    if not clicar_imagem('LogoTotvs.PNG', duplo=True):
        print("Botão não encontrado!")

    time.sleep(5)
    print("\n > Clicando no botão Winthor")
    if not clicar_imagem('LogoWinthor.PNG', duplo=True):
        print("Botão não encontrado!")

    time.sleep(10)
    print("\n > Realizando login no Winthor")
    pyautogui.press('tab', presses=4)
    pyautogui.press('delete')
    pyautogui.write(usuario)
    pyautogui.press('tab')
    pyautogui.write(senha)
    if not clicar_imagem('Entrar.PNG'):
        print("Botão não encontrado!")

    time.sleep(30)