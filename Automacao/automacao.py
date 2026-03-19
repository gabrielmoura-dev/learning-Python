import pyautogui as pa
import time
import pyperclip

pa.PAUSE = 1

# esse código pesquiva o browser no pc, abre, cola a url do youtube, pesquisa o vídeo da Fiap e dá play
pa.press('win')
pa.write('brave')
pa.press('ENTER')
pa.write("youtube.com")
pa.press('ENTER')
time.sleep(3)
pa.click(x=729, y=142)
pa.click(x=729, y=142)
pyperclip.copy("Fiap next 2025")
pa.hotkey('ctrl', 'v')
pa.press('ENTER')
time.sleep(1)
pa.click(x=698, y=494)