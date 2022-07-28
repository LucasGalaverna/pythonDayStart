import pyautogui
import pyperclip
import time


## Programa p/ iniciar o google chorme e deixar em pronto emprego as abas mais utilizadas. 
## Abre também o Sistema específico da empresa realizando login com senha. 

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1.2)
pyautogui.click(x=983, y=30)
pyperclip.copy("https://g1.globo.com/")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(1.5)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://app.pinkapp.com/home")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(1.5)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://www.websoma.com.br/somaWeb/pages/orcamentoVistoria/orcamentoVistoria.xhtml")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(1.5)
pyautogui.press("win")
pyautogui.write("live")
time.sleep(1.5)
pyautogui.click(x=159, y=115)
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=575, y=327)
pyperclip.copy("lg2606")
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=802, y=394)

