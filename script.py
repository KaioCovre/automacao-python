#passo 1:entrar no sistema da empresa.

#  pyautogui.click  > clicar com mouse
#  pyautogui.write  > escrever um texto
#  pyautogui.press  > apertar uma tecla
#  pyautogui.hotkey > atalho (combinação de teclas)

import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
# abrir navegador
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

# entrar no link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

#esperar o site carregar
time.sleep(2)

#passo 2:fazer login.
pyautogui.click(x=830, y=452)
pyautogui.write('Emailempresa@email.com')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.press('tab')
pyautogui.press('enter')

#passo 3:importar a base de dados.

tabela = pandas.read_csv('produtos.csv')
print(tabela)

#passo 4:cadastrar produto.
for linha in tabela.index:

    codigo = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    custo = tabela.loc[linha, 'custo']
   


    pyautogui.click(x=661, y=292)
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))


    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(50000)
#passo 5:repetir o cadastro para todos os produtos.
