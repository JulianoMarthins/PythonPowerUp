from time import sleep
import pyautogui as gui
import pandas as pd

# Faz MOLO000192    Logitech     pausa a cada comando do pyauto gui
gui.PAUSE = 0.7

# Acessar a página da empresa
gui.press('win')
gui.write('edge')
gui.press('enter')

# Link da página de cadastro dos produtos
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
sleep(3)
gui.write(link)
gui.press('enter')

# Realização de login
gui.click(x=780, y=396) # Localização do mouse configurado para resolução 1080p
gui.write('JulianoMarthins@Yahoo.com.br')
gui.press('tab')
gui.write('123456')
gui.click(x=939, y=557)
gui.press('enter')

# Lendo arquivo dos produtos
tabela = pd.read_csv('produtos.csv')

# Cadastrando produto
for linha in tabela.index:

    # Código do produto
    gui.click(x=909, y=274)
    codigo = tabela.loc[linha, 'codigo']
    gui.write(codigo)

    # Marca do produto
    gui.press('tab')
    marca = tabela.loc[linha, 'marca']
    gui.write(marca)

    # Tipo do produto
    gui.press('tab')
    tipo = str(tabela.loc[linha, 'tipo'])
    gui.write(tipo)

    # Categoria do produto
    gui.press('tab')
    categoria = str(tabela.loc[linha, ('categoria')])
    gui.write(categoria)

    # Preço unitário
    gui.press('tab')
    preco = str(tabela.loc[linha, 'preco_unitario'])
    gui.write(preco)

    # Custo do produto
    gui.press('tab')
    custo = str(tabela.loc[linha, 'custo'])
    gui.write(custo)

    # Observação
    gui.press('tab')
    obs = tabela.loc[linha, 'obs']

    if not pd.isna(obs):
        gui.write(obs)

    # Salvar
    gui.press('tab')
    gui.press('enter')

    # Retornar ao topo da tela
    gui.scroll(1000)

