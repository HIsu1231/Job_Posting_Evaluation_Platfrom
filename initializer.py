import streamlit as st


def initialize_session_state():
    default_values = {
        'final_list': [], 'agree': '', 'name': '', 'company': '',
        'experience_years': '', 'task': '', 'feedback': [''] * 2,
        'feedback_response': [False] * 2, 'gen': False,
        'all_completed': [False] * 20
    }

    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value

    # 컨텍스트 관련 세션 상태 초기화 (딕셔너리 사용)
    for i in range(1, 21):
        if f'context{i}' not in st.session_state:
            st.session_state[f'context{i}'] = {
                'acc': {'responses': ['선택하세요 ⇒'] * 5, 'completed': False},
                'comp': {'responses': ['선택하세요 ⇒'] * 10, 'completed': False},
                'gram': {'responses': ['선택하세요 ⇒'] * 2, 'completed': False},
                'flue': {'responses': ['선택하세요 ⇒'] * 2, 'completed': False},
                'usef': {'responses': ['선택하세요 ⇒'] * 2, 'completed': False},
                'all_completed': False}


def load_custom_styles():
    styles = """
    <style>
    .question-radio {
        margin-bottom: -10px;
        font-size: 17px;}

    .question-text {
        margin-bottom: 10px;
        font-size: 17px;}

    .context-box {
        display: inline-block; 
        background-color: transparent; 
        color: #4d4d4d; 
        margin: 10px;
        padding: 10px 10px; 
        border-radius: 15px;
        font-size: 16px; 
        font-weight: bold; 
        margin-top: 4px;
        border: 2px solid #fae6e9;}
        
    .context-box2 {
        display: inline-block; 
        background-color: #333333; 
        color: white; 
        margin: 10px;
        padding: 10px 30px; 
        border-radius: 15px;
        font-size: 16px; 
        font-weight: bold; 
        margin-top: 4px;
    }
    </style>
    """
    st.markdown(styles, unsafe_allow_html=True)
