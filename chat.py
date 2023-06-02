import pyautogui
import keyboard
import sys
import random
import winsound
from datetime import datetime
import imgurpython
from imgurpython import ImgurClient
from twilio.rest import Client

X_CHAT = 360
Y_CHAT = 634
RBG_CHAT = (255, 85, 85)

X_BOX_CHAT = 292
Y_BOX_CHAT = 632

X_SERVER_CHAT = 420
Y_SERVER_CHAT = 634

X_ANCORA = 448
Y_ANCORA = 89
RBG_ANCORA = (210, 209, 205)

X_LOOT = 1329
Y_LOOT = 565
RGB_LOOT = (19,  28,  58)

LIST_MSG1 = ['Oi','Ja volto','Qq houve','Ue','Opa', 'Q bug', 'aaaaaa']
LIST_MSG2 = ['Oi','Já volto','Td bem','Iai','Opa','Hi','Diga']

def send_msg1():
    msg1 = random.choice(LIST_MSG1)
    pyautogui.write(msg1)

def send_msg2():
    msg2 = random.choice(LIST_MSG2)
    pyautogui.write(msg2)

def beep():
    frequency = 2500
    duration = 1000
    winsound.Beep(frequency, duration)

# def print_screen():
#     now = datetime.now().strftime('%d-%m-%Y-%H-%M')
#     file_name = now + '.png'
#     pyautogui.screenshot(file_name)
#     return file_name

# def load_img(file_name):
#     client_id = ''
#     client_secret = ''
#     client = ImgurClient(client_id, client_secret)
#     result = client.upload_from_path(file_name)
#     print('Upload realizado com sucesso!')
#     return result['link']

# def send_whatsapp_msg(url):
#     account_sid = ''
#     auth_token = ''
#     client = Client(account_sid, auth_token)

#     message = client.messages.create(
#     from_='whatsapp:',
#     body=url,
#     to='whatsapp:'
#     )
#     print('Mensagem enviada com sucesso!\n')

programa_em_execucao = True

def parar_programa():
    global programa_em_execucao
    programa_em_execucao = False
    print('\nPrograma encerrado!')
    sys.exit()

keyboard.add_hotkey('page up', parar_programa)

while programa_em_execucao:
    chat = pyautogui.pixelMatchesColor(X_CHAT, Y_CHAT, RBG_CHAT)
    ancora = pyautogui.pixelMatchesColor(X_ANCORA, Y_ANCORA, RBG_ANCORA)
    loot = pyautogui.pixelMatchesColor(X_LOOT, Y_LOOT, RGB_LOOT)


    if ancora == False:
        print('\nSaiu da posição')

        # Alerta
        beep()

        # Parar Feebas
        pyautogui.sleep(4)
        pyautogui.press('esc')
        #parar_programa()
        # Andar
        pyautogui.sleep(2)
        # pyautogui.press('d')
        # pyautogui.press('d')

        # Abrir e escrever no chat
        pyautogui.sleep(2)
        pyautogui.moveTo(X_CHAT, Y_CHAT)
        pyautogui.click()
        pyautogui.sleep(1)

        # file_name = print_screen()
        # url = load_img(file_name)
        # send_whatsapp_msg(url)

        pyautogui.moveTo(X_BOX_CHAT, Y_BOX_CHAT)
        pyautogui.click()
        pyautogui.sleep(1)
        send_msg1()
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(1)
        send_msg1()
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.moveTo(X_BOX_CHAT, Y_BOX_CHAT)
        pyautogui.click()
        pyautogui.sleep(3)
        #pyautogui.press('tab')
        #pyautogui.sleep(1)

        # Sair do jogo
        pyautogui.sleep(2)
        pyautogui.moveTo(1339, 9)
        pyautogui.sleep(2)
        pyautogui.click()
        pyautogui.sleep(2)
        pyautogui.moveTo(688, 416)
        pyautogui.sleep(2)
        pyautogui.click()
        pyautogui.sleep(2)
        parar_programa()

        # # Voltar ao jogo
        # pyautogui.sleep(70)
        # pyautogui.moveTo(449, 279)
        # pyautogui.sleep(2)
        # pyautogui.click()
        # pyautogui.sleep(2)
        # pyautogui.moveTo(830, 472)
        # pyautogui.sleep(2)
        # pyautogui.click()
        # pyautogui.sleep(2)

        # # Voltar pro lugar de farm
        # pyautogui.sleep(2)
        # # pyautogui.press('w')
        # # pyautogui.press('w')
        # # pyautogui.sleep(2)

        # # Clicar no Poke, Server e Feebas
        # pyautogui.moveTo(23, 476)
        # pyautogui.sleep(2)
        # pyautogui.click()
        # pyautogui.sleep(2)
        # pyautogui.moveTo(421, 636)
        # pyautogui.sleep(2)
        # pyautogui.click()
        # pyautogui.sleep(2)
        # pyautogui.moveTo(25, 252)
        # pyautogui.sleep(2)
        # pyautogui.click()
        # pyautogui.sleep(2)

        # file_name = print_screen()
        # url = load_img(file_name)
        # send_whatsapp_msg(url)

        #sys.exit()

    # if loot == False:
    #     print('\nLoot lotado')

    #     # Alerta
    #     beep()

    #     # Parar Feebas
    #     pyautogui.sleep(4)
    #     pyautogui.press('esc')
    #     parar_programa()
    #     file_name = print_screen()
    #     url = load_img(file_name)
    #     send_whatsapp_msg(url)

    #     sys.exit()

    if chat:
        print('\nMensagem no chat')

        # Alerta
        beep()

        # Parar Feebas
        pyautogui.sleep(4)
        pyautogui.press('esc')
        #parar_programa()
        # Andar
        pyautogui.sleep(2)
        #pyautogui.press('s')

        # Abrir e escrever no chat
        pyautogui.sleep(2)
        pyautogui.moveTo(X_CHAT, Y_CHAT)
        pyautogui.click()
        pyautogui.sleep(1)

        # file_name = print_screen()
        # url = load_img(file_name)
        # send_whatsapp_msg(url)

        pyautogui.moveTo(X_BOX_CHAT, Y_BOX_CHAT)
        pyautogui.click()
        pyautogui.sleep(1)
        send_msg2()
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(1)
        send_msg2()
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.moveTo(X_BOX_CHAT, Y_BOX_CHAT)
        pyautogui.click()
        pyautogui.sleep(3)
        #pyautogui.press('tab')
        #pyautogui.sleep(1)

        # Sair do jogo
        pyautogui.sleep(2)
        pyautogui.moveTo(1339, 9)
        pyautogui.sleep(2)
        pyautogui.click()
        pyautogui.sleep(2)
        pyautogui.moveTo(688, 416)
        pyautogui.sleep(2)
        pyautogui.click()

        # Voltar ao jogo
        pyautogui.sleep(120)
        pyautogui.moveTo(449, 279)
        pyautogui.sleep(2)
        pyautogui.click()
        pyautogui.sleep(2)
        pyautogui.moveTo(840, 509)
        pyautogui.sleep(2)
        pyautogui.click()
        pyautogui.sleep(2)

        # Voltar pro lugar de farm
        pyautogui.sleep(2)
        # pyautogui.press('w')
        # pyautogui.press('w')
        # pyautogui.sleep(2)

        # Clicar no Poke, Server e Feebas
        pyautogui.moveTo(23, 472)
        pyautogui.sleep(2)
        pyautogui.click()
        pyautogui.sleep(2)
        pyautogui.moveTo(421, 636)
        pyautogui.sleep(2)
        pyautogui.click()
        pyautogui.sleep(2)
        pyautogui.moveTo(27, 288)
        pyautogui.sleep(2)
        pyautogui.click()
        pyautogui.sleep(2)

        # file_name = print_screen()
        # url = load_img(file_name)
        # send_whatsapp_msg(url)

        #sys.exit()


    

        





    