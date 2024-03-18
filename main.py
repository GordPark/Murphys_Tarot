# main
import streamlit as st 
from pages import *

# Streamlit 앱 생성
if 'page' not in st.session_state:
    st.session_state['page'] = 'HOME'
# sidebar메뉴 설정
menus = {"HOME":home,"CHOICE":choice, "AI_Tarot_ChatBot":tarot_chat, "Murphys_Map":murphys_map, "AI_Tarot_Image":tarot_image}

with st.sidebar:
    for menu in menus.keys():
        if st.button(menu,use_container_width=True, type="primary" if st.session_state['page']==menu else 'secondary'):
            st.session_state['page']=menu
            st.rerun() # 클릭한 곳에 색깔을 입힘 

for menu in menus.keys():
    if st.session_state['page']==menu:
        menus[menu]()
