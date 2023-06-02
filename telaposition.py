import pyautogui
import keyboard

while True:
    keyboard.wait('p')
    print('\nPosição e Cor da Tela:')
    pyautogui.displayMousePosition()