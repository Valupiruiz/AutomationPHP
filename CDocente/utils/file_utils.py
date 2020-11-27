from pathlib import Path
import pyperclip
import pyautogui
import time

project_path = Path(__file__).parent.parent


class FileUtils:
    @staticmethod
    def seleccionar_img_gui(ruta):
        pyperclip.copy(ruta)
        time.sleep(1.5)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')
