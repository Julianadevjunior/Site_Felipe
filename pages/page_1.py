import streamlit as st
from PIL import Image
import os
import teste

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("### Corretor Felipe Carlos")

st.divider()

col1_1, col2_1, col3_1 = st.columns([10, 0.1, 10], vertical_alignment="top")

with col1_1:
    st.text("Whatsapp: (13) 97424-2919")
    st.text("Telefone: (13) 99626-0027")

with col3_1:
    st.link_button(label='Entrar em contato', url='https://wa.me/5513974242919')

box_infos = st.container(border=True)

caminho = "./midia"

# Número de colunas
num_colunas = 2

# Criar colunas
colunas = st.columns(num_colunas)

# Distribuir imagens nas colunas
for i, caminho_imagem in enumerate(teste.capas()):
    with colunas[i % num_colunas]:
        img = Image.open(caminho_imagem)
        # st.image(img, caption=f"Imagem {i + 1}", use_container_width=True)
        imagem_resized = img.resize((300, 300), Image.Resampling.LANCZOS)
        ct = st.container(border=True)
        with ct:
            valor = teste.infs()[f'ap{i+1}'][0]
            iptu = teste.infs()[f'ap{i+1}'][1]
            cond = teste.infs()[f'ap{i+1}'][2]
            st.image(imagem_resized, caption=f"IPTU:{teste.valor(iptu)} | Cond.{teste.valor(cond)}")
            col1, col2, col3 = st.columns([3, 2, 2])
            font_size = [18, 11]
            with col1:
                st.markdown(f"""<p style='font-size:{font_size[0]}px'><b>{teste.valor(valor)}</b></p>""", unsafe_allow_html=True)
                st.markdown(f"""<p style='font-size:{font_size[1]}px'><b>{teste.infs()[f'ap{i+1}'][3]}</b></p>""", unsafe_allow_html=True)

            with col2:
                st.markdown(f"""<p style='font-size:{font_size[1]}px'><b>Quartos: 🛏️{teste.infs()[f'ap{i+1}'][4]}</b></p>""", unsafe_allow_html=True)
                st.markdown(f"""<p style='font-size:{font_size[1]}px'><b>Área: 📐{teste.infs()[f'ap{i+1}'][5]}</b></p>""", unsafe_allow_html=True)

            with col3:
                st.markdown(f"""<p style='font-size:{font_size[1]}px'><b>Banheiro: 🚽{teste.infs()[f'ap{i+1}'][6]}</b></p>""", unsafe_allow_html=True)
                st.markdown(f"""<p style='font-size:{font_size[1]}px'><b>Vaga: 🚘{teste.infs()[f'ap{i+1}'][7]}</b></p>""", unsafe_allow_html=True)

            # bt = st.button('Fotos', key=f'ap{i}', use_container_width=True)
            with st.container(border=True):
                i = i+1
                bt = st.page_link(label=f'Fotos {i}', page=f'pages/page_{i+1}.py', use_container_width=True)
                print(bt)
            # if bt == True and i == 0:
            #     st.session_state['page_image'] = f'ap{i}'
            # elif bt == True and i == 1:
            #     st.session_state['page_image'] = f'ap{i}'
            # elif bt == True and i == 2:
            #     st.session_state['page_image'] = f'ap{i}'
print(st.session_state['page_image'])