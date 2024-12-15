import streamlit as st

page1 = st.Page('pages/page_1.py')
page2 = st.Page('pages/page_2.py')
page3 = st.Page('pages/page_3.py')
page4 = st.Page('pages/page_4.py')
pg = st.navigation([page1, page2, page3, page4])

if 'page_image' not in st.session_state:
    st.session_state['page_image'] = 'ap0'

pg.run()