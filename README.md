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

...
## Environment

~/miniconda3/python     v.3.10.0
streamlit               v.1.31.1
streamlit-image-select  v.0.6.0
pandas                  v.2.2.1
langchain               v.0.1.12
openai                  v.1.13.3

## Reference sites

### https://www.kaggle.com/datasets/lsind18/tarot-json
|index|name|number|arcana|suit|img|fortune_telling|keywords|...|
|---|---|---|---|---|---|---|---|
|0|The Fool|0|Major Arcana|Trump|m00.jpg|Watch for new projects and new beginnings Prepare to take something on faith Something new comes your way; go for it|freedom faith inexperience innocence|
|1|The Magician|1|Major Arcana|Trump|m01.jpg|A powerful man may play a role in your day Your current situation must be seen as one element of a much larger plan|freedom faith inexperience innocence|
|2|The High Priestess|2|Major Arcana|Trump|m02.jpg|A mysterious woman arrives A sexual secret may surface Someone knows more than he or she will reveal|intuition reflection purity initiation|


|기본값|왼쪽 정렬|가운데 정렬|오른쪽 정렬|
|---|:---|:---:|---:|
|내용 1|내용 2|내용 3|내용 4|
|내용 5|내용 6|내용 7|내용 8|
|내용 9|내용 10|내용 11|내용 12|
