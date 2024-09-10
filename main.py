# from PIL import Image
# import numpy as np
import os
import time
import pyautogui
import random
import datetime


def screenShot():
        # diretorio para salvar as imagens
        diretorio = r"C:\Users\Andre Campos\Desktop\portfolio\wydemPython\imagens"
        # contador opcional
        contador = 0
        # inicia um loop infinito
        while True:
                # inicia apos 5 segundos
                time.sleep(5)

                # gera um numero aleatorio para salvar a imagem com esse numro
                numero_aleatorio = random.randint(1, 100)
                # recupera a data do computador
                data = datetime.datetime.now()
                dia = data.day
                mes = data.month
                ano = data.year
                # cria uma string para ser o nome da imagem utilizando a data e o numero aleatorio concatenado com .png
                nome_imagem = f"{dia}{mes}{ano}{numero_aleatorio}.png"

                # recupara a pasta onde as imagens vão ser salvas
                pasta_imagens = os.path.join(diretorio, nome_imagem)

                # faz e salva na pasta os screenshort
                img = pyautogui.screenshot()
                img.save(pasta_imagens)
               # apos um timer de 10 segundo ele faz tudo novamente
                time.sleep(10)

                # contador opcional
                contador += 1

                # se o contador for igual a 5 o laço para.
                if contador == 5:
                        break




screenShot()