import streamlit as st
from PIL import Image
import os
import teste

st.markdown('Page 4')
st.page_link(label=f'Voltar', page=f'pages/page_1.py')

ap = 'ap3'
caminho = f"./midia/{ap}"
imagens = os.listdir(caminho)

# Número de colunas
num_colunas = 2

# Criar colunas
colunas = st.columns(num_colunas)

# Distribuir imagens nas colunas
for i, caminho_imagem in enumerate(imagens):
    with colunas[i % num_colunas]:
        img = Image.open(f"./midia/{ap}/{caminho_imagem}")
        imagem_resized = img.resize((300, 400), Image.Resampling.LANCZOS)
        st.image(imagem_resized)