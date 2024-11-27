import streamlit as st
from initializer import *


if st.session_state['agree'] == '동의합니다.':
    with st.container(border=True):
        st.write('성함을 입력해주세요.')
        st.session_state['name'] = st.text_input(" ", value = st.session_state['name'], key='name_iunput', label_visibility='collapsed')
        st.write('재직중인 회사명을 입력해주세요.')
        st.session_state['company'] = st.text_input(" ", value = st.session_state['company'], key='company_input', label_visibility='collapsed')
        st.write('재직 연차를 입력해주세요. (숫자만 입력해주세요.)')
        st.session_state['experience_years'] = st.text_input(" ", value = st.session_state['experience_years'], key='experience_years_input', label_visibility='collapsed')
        st.write('맡고 계시는 직무를 입력해주세요.')
        st.session_state['task'] = st.text_input(" ", value = st.session_state['task'], key='task_input', label_visibility='collapsed')


else:
    st.warning('개인정보수집에 동의하지 않으셔서 설문에 참여하실 수 없습니다.')