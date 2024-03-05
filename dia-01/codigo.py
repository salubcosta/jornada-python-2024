# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5

url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# Pausa de 3 segundos para 
time.sleep(3)
# Passo 2: Fazer login
pyautogui.click(x=-1410, y=396)
pyautogui.write("salubcosta@gmail.com")
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.click(x=-1158, y=552)
time.sleep(3)
# Passo 3: Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
        
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=-1334, y=278)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)

    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)
# Passo 5: Repetir o processo de cadastro até acabar

