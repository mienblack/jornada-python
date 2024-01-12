import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1 #Pausa de 1s a cada comando do pyautogui

#Abrir o Navegador
pyautogui.press("win") #Pressionar tecla windows
pyautogui.write("edge") #Escrever edge
pyautogui.press("enter") #Pressionar enter

#espera de 3s
time.sleep(3)

#Acessar um link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#espera de 5s
time.sleep(5)

#Fazer Login
pyautogui.click(x=1053, y=487) #Clicar no input de email
pyautogui.write("mimimi@gmail.com") #Digitar email
pyautogui.press("tab") #Ir para o input de senha
pyautogui.write("minha-senha") #Digitar a senha
pyautogui.press("tab") #Ir para o botão de logar
pyautogui.press("enter") #Logar

#espera de 5s
time.sleep(5)

#Importar base de dados
tabela = pd.read_csv(r"\Users\damie\Documents\Programação\jornada-python\aula_01\produtos.csv")
print(tabela)
print("colunas: ", tabela.columns.tolist())


#Cadastrar produtos na tabela
for linha in tabela.index:
    time.sleep(2)
    pyautogui.click(x=1008, y=338) #Clicar no primeiro input
    pyautogui.write(str(tabela.loc[linha, "codigo"])) #Código do produto
    pyautogui.press("tab") #Ir para o próximo input
    pyautogui.write(str(tabela.loc[linha,"marca"])) #Marca do produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"])) #Tipo do produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"])) #Categoria do produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"])) #Preço unitário do produto
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"])) #Custo do produto
    pyautogui.press("tab")
    #Tratamento do obs caso seja NaN
    obs = tabela.loc[linha,"obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs)) #Obs do produto
    pyautogui.press("tab")
    pyautogui.press("enter") #Enviar Produto
    pyautogui.press("home") #Voltar ao início da tela