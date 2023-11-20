import pyautogui

ss = pyautogui.screenshot()

ss.save('screenshot.png')

from PIL import ImageGrab
ss=ImageGrab.grab()
ss.save("screenshot2.png")