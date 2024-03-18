# main
import streamlit as st 
from pages import *


page_bg_img = """
<style>
body {
background-image: linear-gradient(45deg, #444cf7, #444cf7);
<!-- opacity: 0.8; -->

}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# 뒷면의 카드를 랜덤으로 선택한 카드로 바꿈
def change_image(image_url):
    st.markdown(
        f'<img src="{image_url}" id="dynamic-image">',
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <script>
        var imageIndex = 0;
        var images = ["image1.jpg", "image2.jpg", "image3.jpg"]; // 이미지 파일 경로 리스트

        function updateImage() {
            var img = document.getElementById('dynamic-image');
            img.src = images[imageIndex];
            imageIndex = (imageIndex + 1) % images.length;
        }

        setInterval(updateImage, 5000); // 이미지 변경 간격 설정 (밀리초)
        </script>
        """,
        unsafe_allow_html=True
    )

# Streamlit 앱 생성


if 'page' not in st.session_state:
    st.session_state['page'] = 'HOME'



menus = {"HOME":home,"CHOICE":choice, "AI_Tarot_ChatBot":tarot_chat, "Murphys_Map":murphys_map, "AI_Tarot_Image":tarot_image}

with st.sidebar:
    for menu in menus.keys():
        if st.button(menu,use_container_width=True, type="primary" if st.session_state['page']==menu else 'secondary'):
            st.session_state['page']=menu
            st.rerun() # 클릭한 곳에 색깔을 입힘
        

for menu in menus.keys():
    if st.session_state['page']==menu:
        menus[menu]()


# with st.sidebar:
#     with st.echo():
#         st.write("This code will be printed to the sidebar.")

#     with st.spinner("Loading..."):
#         time.sleep(5)
#     st.success("Done!")

# # Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )
