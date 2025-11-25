# Automação de Sistemas e Processos com Python
# Desafio:
# Todos os dias, o nosso sistema atualiza as vendas do dia anterior. O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, 
# assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior

# E-mail da diretoria: danilo.sibov@gmail.com
# Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/152iE5z_PIynJiz__jb2CJiaTB0yta4DQ

# Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

# Referência do pyautogui: https://pyautogui.readthedocs.io/en/latest/quickstart.html

# Bibliotecas necessárias: pyautogui, pandas, pyperclip, time
# Comandos para instalar as bibliotecas:
# pip install pyautogui pandas pyperclip

import pyautogui
import time
import pandas as pd
import pyperclip


# Dar um tempo de 5 segundos para o usuário posicionar o mouse
pyautogui.PAUSE = 1

# Desabilitar fail-safe (permite clicar em cantos da tela)
pyautogui.FAILSAFE = False

# Comandos principais do pyautogui:
# pyautogui.click -> clicar
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> conjunto de teclas
# pyautogui.write -> escreve um texto


# Passo 1.1: Abrir o navegador e selecionar um perfil clicando
pyautogui.hotkey("win", "r")
# Digita o comando para abrir o Chrome e pressiona Enter
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)

# Passo 1.2: Selecionar um perfil o navegador
pyautogui.click(x=870, y=470, clicks=2)

# Passo 3: Entrar no sistema da empresa (no nosso caso é o link do drive)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/152iE5z_PIynJiz__jb2CJiaTB0yta4DQ")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)



# Passo 4.1: Navegar no sistema e encontrar a base de vendas e fazer o download
# Selecionar o arquivo
pyautogui.click(x=880, y=588, clicks=2)
time.sleep(2)

# Passo 4.2: Fazer o download da base de vendas
pyautogui.click(x=1706, y=580, clicks=2) #clicar no fazer download

#pyautogui.click(x=2716, y=1523) # clicar no fazer download
#time.sleep(5) # esperar o download acabar