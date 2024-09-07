# from PIL import Image
# import numpy as np
import os
import time
import pyautogui
import random
import datetime


def screenShot():
        diretorio = r"C:\Users\Andre Campos\Desktop\portfolio\wydemPython\imagens"
        contador = 0
        while True:
                time.sleep(5)

                numero_aleatorio = random.randint(1, 100)
                data = datetime.datetime.now()
                dia = data.day
                mes = data.month
                ano = data.year
                nome_imagem = f"{dia}{mes}{ano}{numero_aleatorio}.png"
                pasta_imagens = os.path.join(diretorio, nome_imagem)

                img = pyautogui.screenshot()
                img.save(pasta_imagens)
               
                time.sleep(10)

                contador += 1
                if contador == 5:
                        break




screenShot()