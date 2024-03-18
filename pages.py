# pages
import streamlit as st
import pandas as pd
from streamlit_image_select import image_select
from pandas import json_normalize
from langchain.callbacks.base import BaseCallbackHandler
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import ChatMessage
from dotenv import load_dotenv
from openai import OpenAI
import requests
import time
import random
import os


def home():
    st.title("머피타로에 방문하신걸 환영합니다")
    st.subheader("🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮")

    st.markdown("""<img src ="https://img.shields.io/badge/Python-071D49?logo=Python&logoColor=white"/> <img src ="https://img.shields.io/badge/Kaggle-20BEFF?logo=Kaggle&logoColor=white"/> <img src ="https://img.shields.io/badge/OpenAI-00A3E0?logo=OpenAI&logoColor=white"/>""", unsafe_allow_html=True)
    st.markdown("""                      

        ## Description

        **머피의 법칙이 존재하는가**

        🃏 "우리는 우리의 운명을 선택하지만, 우리의 운명은 우리를 선택한다."

        🃏 "타로는 우리가 내면의 지혜를 발견하고 우리의 여정을 이해할 수 있는 도구이다."

        🃏 "우리의 삶은 한 장의 카드와 같다. 어떻게 그것을 잡을지는 우리에게 달려있다."

        `Python`, `Kaggle`, `OpenAI API`로 제작된 타로점술 웹 애플리케이션입니다.
        사용자는 세장의 타로카드를 뽑아 Kaggle에서 받아온 타로카드의 정보를 담고 있는 Json파일에서 각 카드에 해당하는 정보를 GPT API에 전달하여 조합된 내용을 통해 결과를 도출합니다. 머피타로를 사용하면 타로점술 결과로 위험이 도사리고 있는 지역이나 장소 또는 행운을 불러오는 장소나 지역 등 지도에 있는 마커를 통해 확인을 할 수 있습니다. 즐거운 시간이 됐으면 좋겠습니다.

        ## 추가예정

        ...

        ## Reference sites

        ### https://www.kaggle.com/datasets/lsind18/tarot-json
    """)
    # JSON 파일을 DataFrame으로 읽어서 cardsImgs에 저장
    cardsImgs = pd.read_json('./tarotimg/tarot-images.json', orient='records')
    # JSON 파일의 데이터를 정규화 Pandas DataFrame의 행으로 변환
    cardsImgs = json_normalize(cardsImgs['cards'])
    st.write(cardsImgs)
    

def choice():
    st.title("CHOICE")
    st.info("💡 카드 3장을 신중하게 골라주세요.")
    folder_path = "./tarotimg/cards/"
    back_card = "./tarotimg/back.jpg"
    # 확장자.jpg인 파일 리스트형태로 저장
    image_files = [file for file in os.listdir(folder_path) if file.endswith('.jpg')]
    
    cards_path = []
    # 이후에 사용될 change버튼 3번이상 클릭 시 disabled기능 세션에 저장
    if 'change_disabled' not in st.session_state:
        st.session_state.change_disabled = False

    # 랜덤으로 생성된 카드는 버튼 클릭 시 계속 생길 수 있어 세션으로 추적관리
    if 'image_paths' not in st.session_state:
        random_cards = random.sample(image_files,3)
        # 폴더경로와 합쳐 리스트 저장
        cards_path = [folder_path + i for i in random_cards]
        st.session_state.image_paths = cards_path      
              
    left_co, cent_co,last_co = st.columns(3)
    # 이미지 인덱스를 기억하기 위한 변수
    if 'image_index' not in st.session_state:
        # 기본 back카드가 따로 있어 인덱스는 -1로 시작
        st.session_state.image_index = -1
    # 버튼을 클릭할 때 갤러리에 정보를 저장할 변수
    if 'gallery_images' not in st.session_state:
        st.session_state.gallery_images = []

    # 이미지 인덱스를 기반으로 현재 이미지 경로를 가져옴
    current_image_index = st.session_state.image_index
    current_image_path = st.session_state.image_paths[current_image_index]
    current_gallery_path = st.session_state.gallery_images
    
    # 3개의 열중 중간에 해당되는 변수로 중앙정렬
    with cent_co:               
        selected_image = st.image(back_card, caption="선택 카드")
        
        # 이미지 변경 버튼 disabled 키를 통해 버튼표시
        if st.button("Change Image", use_container_width=True, disabled=st.session_state.change_disabled):
            # 다음 이미지 인덱스로 이동
            current_image_index = (current_image_index + 1) % len(st.session_state.image_paths)
            # 저장한 이미지 인덱스를 현재 인덱스에 할당
            st.session_state.image_index = current_image_index
            # 할당된 인덱스에 해당하는 이미지를 변수에 불러옴
            current_image_path = st.session_state.image_paths[current_image_index]
            st.session_state.gallery_images.append(current_image_path)
            # 불러온 이미지를 캡션정보(현재 인덱스번호)와 함께 표시
            selected_image.image(current_image_path, caption=f"현재 선택카드 번호: {current_image_index}")
            
            # 현재 인덱스가 2일 경우 0.0001초 뒤 버튼 표시안함
            if current_image_index == 2:
                st.session_state.change_disabled = True
                time.sleep(0.0001)
                # 재실행 후 잠금
                st.rerun()
    # 이후에 사용될 선택한 이미지 정보를 세션에 초기화
    if 'gallery_image_info' not in st.session_state:
        st.session_state.gallery_image_info = []
    st.subheader("이미지를 선택해서 정보를 확인해보세요")
    try: 
        with st.expander("💾 __저장된 카드 갤러리__"):
            st.error("🚨갤러리에 있는 카드를 다 확인 후 데이터가 저장됩니다.🚨")
            # 선택한 이미지의 경로를 selected_image에 저장
            selected_image = image_select(label="Gallery",images=current_gallery_path)

            # 선택한 이미지 표시
            if selected_image:
                # JSON 파일을 DataFrame으로 읽어서 cardsImgs에 저장
                cardsImgs = pd.read_json('./tarotimg/tarot-images.json', orient='records')
                # JSON 파일의 데이터를 정규화 Pandas DataFrame의 행으로 변환
                cardsImgs = json_normalize(cardsImgs['cards'])
                # 이미지 중앙정렬
                left_ga_co,cent_ga_co,right_ga_co = st.columns(3)
                with cent_ga_co:
                    st.image(selected_image)                
                # 선택한 이미지 경로를 "/"로 나눠서 끝부분인 *.jpg 형식으로 저장
                target_img = selected_image.split("/")[-1]

                 # cardsImgs의 img열로 인덱스 설정
                cardsImgs.set_index('img', inplace=True)
                # 'img'열 기준으로 선택한 이미지의 행을 저장
                matching_cards = cardsImgs.loc[target_img]
                # matching_cards를 딕셔너리 형태로 변환
                matching_cards_dict = matching_cards.to_dict()
                st.write("선택한 카드 Json파일정보", matching_cards_dict)

                # 선택된 이미지가 랜덤으로 생성된 3개의 이미지 리스트에 있는지 확인
                if selected_image in st.session_state.image_paths:
                    # 선택된 이미지를 가진 image_paths 경로의 인덱스 가져오기
                    info_index = st.session_state.image_paths.index(selected_image)
                    # gallery_image_info 리스트의 길이가 info_index보다 작으면 확장(인덱스에러 방지)
                    while len(st.session_state.gallery_image_info) <= info_index:
                        st.session_state.gallery_image_info.append([])
                    # 해당 인덱스에 이미지 정보가 없으면 추가(중복방지)
                    if not st.session_state.gallery_image_info[info_index]:
                        st.session_state.gallery_image_info[info_index].append(matching_cards_dict)

    # image가 없을 때 예외처리            
    except ValueError as e:
        print(e)
    
def tarot_chat():
    st.title("타로 ChatBot")
    # .env파일의 환경변수에 접근 
    load_dotenv()

    # API_KEY 할당 및 모델 선택
    API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL = "gpt-4-0125-preview"

    class StreamHandler(BaseCallbackHandler):
        def __init__(self, container, initial_text=""):
            self.container = container # 대화 내용을 표시할 streamlit 컨테이너
            self.text = initial_text    # 대화의 초기 텍스트

        # 새로운 토큰이 생성 될때마다 호출
        def on_llm_new_token(self, token: str, **kwargs) -> None:
            self.text += token  # 새로운 내용 계속 더하겠다, 대화 내용 지속적으로 업데이트
            self.container.markdown(self.text) # 새로운 내용을 마크다운 형식으로 컨테이너에 표시

    want_to = """너는 타로카드의 JSON파일정보를 기반으로 3개의 카드정보를 조합해서 질의응답을 하는 타로주술사야.
    content
    {}
    """

    content={}
    # 각 이미지의 정보를 content 딕셔너리에 저장
    for index, item in enumerate(st.session_state.gallery_image_info):
        # 각 이미지의 첫 번째 딕셔너리 정보를 가져와서 content에 저장
        content[index] = item[0]

    # Tarot_ChatBot 사이드 바 열었을 때 gallery_images가 없는 경우도 있기에 미리 생성
    if 'gallery_images' not in st.session_state:
        st.session_state.gallery_images = []

    st.info("타로와 관련된 정보를 알아볼 수 있는 Q&A 로봇입니다.")
    # 3개의 열에 선택한 이미지 표시
    col1, col2, col3 = st.columns(3)
    # 카드를 선택하기전 오류 예외처리
    try:
        with col1:
            st.image(st.session_state.gallery_images[0], width=50)
            st.write("1번 카드")        
        with col2:
            st.image(st.session_state.gallery_images[1], width=50)
            st.write("2번 카드")
        with col3:
            st.image(st.session_state.gallery_images[2], width=50)
            st.write("3번 카드")
    except IndexError as i:
        print(i)

    # StreamlitAPIException 예외처리 오류..
    try:
        options = []
        # 이미지 3장 각각의 추천질문을 반복하여 뽑아온다
        for item in st.session_state.gallery_image_info:
            # 해당 키값의 내용을 question에 저장
            question = item[0]["Questions to Ask"]
            # options리스트에 추가한다
            options.append(question)
         # options 리스트가 비어 있는지 확인하고, 비어 있으면 예외 발생
        if not options:
            raise StreamlitAPIException("추천 질문이 없습니다.")

        selected_questions = st.multiselect("추천 질문 리스트", options)
        st.write('You selected:', selected_questions)
    except StreamlitAPIException as e:
        st.error(str(e))   

    

    if "messages" not in st.session_state: 
        # 세션상태 초기화 assistant역할로 content를 세션상태 message에 추가
        st.session_state["messages"] = [ChatMessage(role="assistant", content="안녕하세요! 타로를 알려주는 Q&A 로봇입니다. 어떤 내용이 궁금하신가요?")]

    for msg in st.session_state.messages:
        # role에 해당하는 역할의 채팅메세지를 streamlit 채팅 메세지 컴포넌트에 작성
        st.chat_message(msg.role).write(msg.content)

    if prompt := st.chat_input(): # 사용자에게 채팅입력 요청, 입력 한다면
        # 사용자의 입력메세지를 user역할로 설정 후 세션 상태의 message에 추가
        # if "축제" in prompt:
        st.session_state.messages.append(ChatMessage(role="user", content=prompt))
        # 사용자가 입력한 메세지를 streamlit 채팅 메세지 컴포넌트에 작성
        st.chat_message("user").write(prompt)

        if not API_KEY: # API_KEY가 비어있다면
            # 정보메세지로 문자열 메세지 표시
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        with st.chat_message("assistant"): # streamlit에서 assistant역할의 메세지 표시
            stream_handler = StreamHandler(st.empty()) # 비어 있는 컨테이너에 후속 메시지 표시
            # streaming스트리밍모드 사용여부 callbacks콜백 핸들러 목록
            llm = ChatOpenAI(openai_api_key=API_KEY, streaming=True, callbacks=[stream_handler], model_name=MODEL)
            # system 역할의 메세지 와 사용자로부터 받은 입력
            response = llm([ ChatMessage(role="system", content=want_to.format(content))]+st.session_state.messages)
            # reponse에서 받은 대화의 응답을 assistant 역할의 메세지로 변환 후 세션상태 메세지 목록에 추가
            st.session_state.messages.append(ChatMessage(role="assistant", content=response.content))

# 업데이트 예정
def murphys_map():
    st.title("머피지도")
    st.info("💡 머피지도는 아직 발견되지 못했습니다.")
    st.markdown("## 찾으신 분 연락주세요.. ")

def tarot_image():
    st.title("AI가 만들어주는 타로이미지")
    st.info("💡 현재 선택한 카드의 데이터로 이미지가 생성됩니다.")
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    MODEL = "dall-e-3"
    # 선택한 카드와 연결하고 싶은 키워드 keyword에 저장    
    keyword = st.text_input('키워드를 입력하세요: ', '')
    # 폰트 색상 황금색 
    st.markdown(f'입력한 키워드: <h2 style="color:#FFD700; font-weight:bold;">{keyword}</h2>', unsafe_allow_html=True)
    
    contents = {}    
    
    # gallery_image_info 속성을 초기화
    if 'gallery_image_info' not in st.session_state:
        st.session_state.gallery_image_info = []
    # 선택한 카드 데이터 반복해서 가져옴
    for index,item in enumerate(st.session_state.gallery_image_info):
        # 각 이미지의 해당 키값의 내용을 contents에 저장
        contents[index] = {"name": item[0]["name"],
        "fortune_telling":item[0]["fortune_telling"],
        "keywords":item[0]["keywords"]
        }
    # 선택한 이미지 표시하기 위해 초기화
    if 'gallery_images' not in st.session_state:
        st.session_state.gallery_images = []
    st.subheader("선택한 카드")
    col1,col2,col3 = st.columns(3)   
    # 선택한 이미지 표시
    try:
        with col1:
            st.image(st.session_state.gallery_images[0], width=50)
            st.write("1번 카드")        
        with col2:
            st.image(st.session_state.gallery_images[1], width=50)
            st.write("2번 카드")
        with col3:
            st.image(st.session_state.gallery_images[2], width=50)
            st.write("3번 카드")
    except IndexError as i:
        print(i)
    # 버튼을 누를 때만 이미지 생성    
    if st.button("Dall-e"):
        client = OpenAI(api_key=openai_api_key)
        # DALL-E에 이미지 생성 요청 보내기
        response = client.images.generate(
            model=MODEL,
            # 이름 / 운세 / 키워드 데이터를 가져온 contents와 입력받은 키워드를 prompt에 전달
            prompt=        
            f"""
            타로카드 3개의 JSON파일정보를 기반으로 조합한 contents를 입력해준 키워드에 맞게 이미지를 생성해줘.
            contents
            {contents}
            keyword
            {keyword}
            """,
            size="1024x1024",
            # 품질 높게하려면 high 시간과 리소스도 더 많이 들어감
            quality="standard",
            # 생성할 이미지 수
            n=1,
        )
        # 생성된 이미지 URL 가져오기
        image_url = response.data[0].url

        # 저장 파일 이름 설정
        filename = f"{keyword}.jpg"
        # URL에서 GET 요청을 수행하여 response_img 변수에 저장
        response_img = requests.get(image_url)
        # 이미지 데이터를 해당 파일에 바이너리 쓰기 모드('wb')로 저장
        with open(filename, 'wb') as f:
            f.write(response_img.content)
        
        ai_left,ai_center,ai_right = st.columns(3)
        with ai_center:
            st.image(filename)

        