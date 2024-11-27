import streamlit as st
from initializer import *

initialize_session_state()

load_custom_styles()

col1, col2, col3 = st.columns([1, 6.5, 1])
with col2:
    st.markdown("""

                <div style="
                    background-color: #555555;
                    color: white;
                    padding: 10px;
                    text-align: center;
                    border-radius: 5px;
                    font-weight: bold;
                    ">
                    <span style="font-size: 30px;">AI기반 구인구직 통합지원 솔루션 개발 및 실증</span><br>
                    <span style="font-size: 25px;">- 구인공고 작성지원 모델 성능평가 -</span>
                </div>

                <div style="font-size: 15px; line-height: 1.8; margin-top: 20px;"> 
                    <br>안녕하십니까?<br>
                    (주)원티드랩에서는 'AI기반 구인구직 통합지원 솔루션 개발 및 실증' 과제를 수행 중에 있습니다.
                    금일 거대 언어모델을 통해 생성된 구인공고 작성지원 모델의 성능 평가에 협조해 주셔서 감사드립니다.
                    평과결과는 정확하고 유용한 구인공고 작성지원 시스템을 수립하기 위한 중요한 지표로 이용될 것입니다. </div>

                <div style="fint-size: 18px; margin-top: 20px;"> 
                    [평가 방법]<br>
                    1. 모든 평가는 평가자 PC에 실행되고 있는 성능평가 프로그램을 통해서 진행합니다.<br>
                    2. 평가자는 회사명, 주요 서비스/상품, 모집 직무 등이 포함된 구인 상황을 부여받게 됩니다.<br>
                    3. 해당 상황을 파악한 후 모집 직무에 대한 내용을 2~3문장 내외로 작성합니다.<br>
                    4. 작성 후 추천된 추천직무, 추천직종, 직종키워드, 추천 자격증 중 적절한 것들을 선택합니다.<br>
                    5. 이후 모델이 작성한 구인공고를 확인하고 평가지를 작성합니다.<br>
                    6. 총 20개의 상황을 대상으로 평가를 진행 후 종료합니다.<br>
                    <br>본 평가의 결과는 본 과제의 결과 보고 외의 목적으로는 사용되지 않습니다.<br><br>
                </div>

                ##### [개인정보 수집 및 이용 동의]

                <div style='font_size: 16px; lien-height: 1.8;'>
                    본 설문조사는 귀하의 이름, 재직 회사명, 재직 연차, 직무 정보를 수집하여 설문 결과 분석에 활용하고자 합니다.<br>
                    수집된 개인정보는 오직 본 설문조사의 목적을 위해서만 사용되며, 설문 종료 후에는 안전하게 폐기될 예정입니다.<br>
                    - 수집 항목: 이름, 재직 회사명, 재직 연차, 직무<br>
                    - 수집 목적: 설문 조사 결과의 정확한 분석 및 통계 자료 작성<br>
                    - 보유 기간: 설문 종료 후 6개월 이내 폐기<br><br>
                    귀하는 개인정보 수집 및 이용을 동의하지 않을 권리가 있으며, 동의하지 않을 시 설문 참여가 불가능합니다.<br><br>
                </div>""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col3:
        st.session_state['agree'] = st.radio(' ', ['동의합니다.', '동의하지 않습니다.'],
                                             index=0 if st.session_state['agree'] == "동의합니다." else 1, horizontal=True,
                                             label_visibility='collapsed')

    st.markdown("""<hr style='border: 0; height: 1; background-color: black; margin-top: 20px; margin-bottom: 20px'>
                    <div style='font_size: 16px; lien-height: 1.8;'>
                    평가주관기관: (주)원티드랩<br>
                    평가위탁기관: (주)어니컴<br>
                    평가수행기관: (주)팀와이</div>
                    <hr style='border: 0; height: 1; background-color: black; margin-top: 20px; margin-bottom: 20px'>""",
                unsafe_allow_html=True)

