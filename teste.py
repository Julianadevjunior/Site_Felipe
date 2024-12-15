import streamlit as st
from PIL import Image
import os
import pandas as pd

caminho = os.listdir('./midia')


def capas():
    capa = []
    caminho_midia = os.listdir('./midia')
    for midia in caminho_midia:
        imagem = os.listdir(f'./midia/{midia}')[0]
        capa.append(f'./midia/{midia}/{imagem}')
    return capa

def infs():
    df = pd.read_excel(r'C:\Users\jucar\Documents\Landpage\page001\imovel_infos.xltx')

    dict_infos = {}

    for linha in range(0, len(df)):
        colunas = df.iloc[linha]
        lista = colunas.values
        dict_infos[f'{lista[0]}'] = lista[1:]

    return dict_infos

def valor(num):
    origem = f"{num:,.2f}"
    if ',' in origem:
        origem = origem.replace(',', '-')

    if '.' in origem:
        origem = origem.replace('.', ',')

    if '-' in origem:
        origem = origem.replace('-', '.')

    valor = f'R${origem}'

    return valor


def imagens():
    image = []
    caminho_midia = os.listdir('./midia')
    for midia in caminho_midia:
        imagem = os.listdir(f'./midia/{midia}')
        image.append(f'./midia/{midia}/{imagem}')
    return image

print(capas())