# 🔮 Murphy's_Tarot

<img src ="https://img.shields.io/badge/Python-071D49?logo=Python&logoColor=white"/> <img src ="https://img.shields.io/badge/Kaggle-20BEFF?logo=Kaggle&logoColor=white"/> <img src ="https://img.shields.io/badge/OpenAI-00A3E0?logo=OpenAI&logoColor=white"/>

## Description

**머피의 법칙이 존재하는가**

🃏 "우리는 우리의 운명을 선택하지만, 우리의 운명은 우리를 선택한다."

🃏 "타로는 우리가 내면의 지혜를 발견하고 우리의 여정을 이해할 수 있는 도구이다."

🃏 "우리의 삶은 한 장의 카드와 같다. 어떻게 그것을 잡을지는 우리에게 달려있다."

`Python`, `Kaggle`, `OpenAI API`로 제작된 타로점술 웹 애플리케이션입니다.
사용자는 세장의 타로카드를 뽑아 Kaggle에서 받아온 타로카드의 정보를 담고 있는 Json파일에서 각 카드에 해당하는 정보를 GPT API에 전달하여 조합된 내용을 통해 결과를 도출합니다. ~~머피지도는 타로점술 결과로 위험이 도사리고 있는 지역이나 장소 또는 행운을 불러오는 장소나 지역 등 지도에 있는 마커를 통해 확인을 할 수 있습니다~~. 머피지도는 아직 찾지 못했습니다.. 타로이미지 생성페이지 에서는 선택한 타로카드 정보와 사용자 입력 키워드를 기반으로 DALL-E 모델을 사용하여 이미지를 생성합니다. 이 페이지는 선택한 카드 이미지와 함께 사용자가 입력한 키워드에 맞는 AI 생성 이미지를 표시합니다. 즐거운 시간이 됐으면 좋겠습니다.

## Getting Tarot

https://github.com/GordPark/Murphys_Tarot/assets/134121857/ef8e7f70-9fd8-483d-aab9-c1da237b70f2

### ⭕CHOICE

![choice](https://github.com/GordPark/Murphys_Tarot/assets/134121857/a7fa8e52-4eb9-44cd-8ab4-30a20636bb97)
![choice_info](https://github.com/GordPark/Murphys_Tarot/assets/134121857/b3e1d0b5-1e29-410d-8989-5465f160dc7a)

### ⭕AI_Tarot_ChatBot

![chatbot](https://github.com/GordPark/Murphys_Tarot/assets/134121857/6e4012b7-eb4c-47ba-ae1d-14ed624105fc)

### ⭕AI_Tarot_Image

![ai_image](https://github.com/GordPark/Murphys_Tarot/assets/134121857/728a45e5-776a-4b73-9387-7a9c5ff4dc28)

`Record.mp4`

## Environment

~/miniconda3/python `v.3.10.0`

streamlit `v.1.31.1`

streamlit-image-select `v.0.6.0`

pandas `v.2.2.1`

langchain `v.0.1.12`

openai `v.1.13.3`

## Reference sites

### https://www.kaggle.com/datasets/lsind18/tarot-json

| index | name               | number | arcana       | suit  | img     | ... |
| ----- | ------------------ | ------ | ------------ | ----- | ------- | --- |
| 0     | The Fool           | 0      | Major Arcana | Trump | m00.jpg | ... |
| 1     | The Magician       | 1      | Major Arcana | Trump | m01.jpg | ... |
| 2     | The High Priestess | 2      | Major Arcana | Trump | m02.jpg | ... |
| ...   | ...                | ...    | ...          | ...   | ...     | ... |
