# Projeto de automação fazendo cadastros de produtos #

# pip install pyautogui
# pip install pandas openpyxl numpy

import pyautogui
import time
#-------------------------------------------------------------------------------#
# pyautogui.click - Para clicar com o mouse
# pyautogui.write - Para escrever um texto
# pyautogui.press - Para apertar uma tecla
# pyautogui.hotkey - Para apertar combinaçoes de teclas (ex: ctrl + C)
# pyautogui.scroll - Para rolar a tela, para cima ou para baixo
#-------------------------------------------------------------------------------#

pyautogui.PAUSE = 0.5

# Passo 1 - Entrar no sistema
# Abrir o navegador
pyautogui.press('win')
pyautogui.write('Brave')
pyautogui.press('enter')
time.sleep(1)
# Com o navegador aberto, entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3)

# Passo 2 - Fazer Login
pyautogui.click(x=572, y=370) # Clicar no campo de login
pyautogui.hotkey('ctrl', 'a') # Selecionar qualquer coisa escrita na area de login para apagar
pyautogui.write('exemplo@hotmail.com')
pyautogui.press('tab') # Passar para o campo de senha
pyautogui.write('minha senha')
pyautogui.press('enter')
time.sleep(3) # Para aguardar a pagina carregar e continuar

# Passo 3 - importar base de dados
import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)

# Passo 4 - Cadastrar o produto
# para cara linha da minha tabela:
for linha in tabela.index:
    # codigo
    pyautogui.click(x=564, y=250)
    codigo = str(tabela.loc[linha, 'codigo']) # str = string = texto
    pyautogui.write(codigo)
    # marca
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    #marca = str(tabela.loc[linha, 'marca'])
    #pyautogui.write(marca)
    # tipo
    pyautogui.press('tab')
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    # categoria
    pyautogui.press('tab')
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    # preco_unitario
    pyautogui.press('tab')
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    # custo
    pyautogui.press('tab')
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    # obs
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs !='nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter') # cadastra o produto (botão enviar)
    # dar escroll de tudo pra cima
    pyautogui.scroll(5000)

# Passo 5 - Repetir para todos os produtos - para todas as linhas da tabela
