import pyautogui
import pandas
import time
pyautogui.PAUSE = 0.5
tabela = pandas.read_csv("produtos.csv")

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# print(pyautogui.position())

pyautogui.click(x=446, y=371)
pyautogui.write("emailTeste123456@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.click(x=677, y=537)
time.sleep(3)


for linha in tabela.index:
    #para cada linha da tabela ele vai repetir
    pyautogui.doubleClick(x=435, y=257)
    
    codigo = tabela.loc[linha,"codigo"]#[linha,coluna]  pega o valor do codigo com base na linha e coluna fornecida
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        #se o campo nao for vazio ele sera preenchido
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)

