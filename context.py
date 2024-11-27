import numpy as np
import pandas as pd
import streamlit as st
from initializer import *

initialize_session_state()
load_custom_styles()

# 질문 반복 처리를 위한 함수 생성
def render_questions(context_key, category_key, questions, options):
    responses = st.session_state[context_key][category_key]['responses']
    all_completed = True

    for i, question in enumerate(questions):
        st.markdown(f'<div class="question-radio">{question}</div>', unsafe_allow_html=True)
        response = st.radio(" ", options, key=f'{context_key}_{category_key}_question_{i}', index=options.index(responses[i]) if responses[i] in options else 0, horizontal=True, label_visibility='collapsed')
        responses[i] = response
        if response == '선택하세요 ⇒':
            all_completed = False

    st.session_state[context_key][category_key]['responses'] = responses
    st.session_state[context_key][category_key]['completed'] = all_completed
    return all_completed


def context(n, context_input):
    # 각 상황을 처리하는 컨텍스트 함수 생성
        context_key = f'context{n}'
        st.subheader(f'상황 {n}')
        st.markdown(f'<div class="context-box2">{context_input}</div>', unsafe_allow_html=True)

        categories = [
            ('정확성 평가', 'acc', ["작성하신 직무 내용에 기반하여 추천된 '추천 직무'는 적절했습니까?",
                               "작성하신 직무 내용에 기반하여 추천된 '추천 직종'은 적절했습니까?",
                               "작성하신 직무 내용에 기반하여 추천된 '직종 키워드'는 적절했습니까?",
                               "작성하신 직무 내용에 기반하여 추천된 '추천 자격증'은 적절했습니까?",
                               "작성하신 직무 내용에 기반하여 추천된 '채용 정보 검색어'는 적절했습니까?"]),
            ('완전성 평가', 'comp', ["6. 생성된 구인공고 초안의 '제목'은 해당 구인에 대한 내용을 잘 반영했습니까?",
                                "7. 생성된 구인공고 초안은 '추천 직무'에서 선택한 내용을 잘 반영했습니까?",
                                "8. 생성된 구인공고 초안은 '추천 직종'에서 선택한 내용을 잘 반영했습니까?",
                                "9. 생성된 구인공고 초안은 '직종 키워드'에서 선택한 내용을 잘 반영했습니까?",
                                "10. 생성된 구인공고 초안은 '혜택 및 복지'의 내용을 잘 반영했습니까?",
                                "11. 생성된 구인공고 초안은 '채용 전형'의 내용을 잘 반영했습니까?",
                                "12. 생성된 구인공고 초안의 '직무 소개'의 내용은 적절히 작성되었습니까?",
                                "13. 생성된 구인공고 초안의 '주요 업무'의 내용은 적절히 작성되었습니까?",
                                "14. 생성된 구인공고 초안의 '우대 사항'의 내용은 적절히 작성되었습니까?",
                                "15. 생성된 구인공고 초안의 '기술 스택'의 내용은 적절히 작성되었습니까?"]),
            ('문법성 평가', 'gram', ["16. 생성된 구인공고 초안에는 오탈자가 몇 개 있었습니까?",
                                "17. 생성된 구인공고 초안에는 비문이 몇 개 있었습니까? (주술호응 부적절, 조사 부당 생략, 중의적 표현 등)"]),
            ('유창성 평가', 'flue', ["18. 생성된 구인공고 초안의 '격식있게' 기능은 자연스럽게 반영되었습니까?",
                                "19. 생성된 구인공고 초안의 '친근하게' 기능은 자연스럽게 반영되었습니까?"]),
            ('유용성 평가', 'usef', ["20. 생성된 구인공고 초안의 내용은 실제 구직자에게 유용한 정보를 제공합니까?",
                                "21. 생성된 구인공고 초안의 내용은 실제 구직자에게 매력적으로 보일 것 같습니까?"])
            # gram, flue 등 다른 카테고리도 유사하게 추가
        ]

        options = ['선택하세요 ⇒', '매우 아니다', '아니다', '보통이다', '그렇다', '매우 그렇다']
        all_completed = True

        for category_name, category_key, questions in categories:
            st.write(f"#### {category_name}")
            category_completed = render_questions(context_key, category_key, questions, options)
            if not category_completed:
                all_completed = False

        st.session_state[context_key]['all_completed'] = all_completed
        st.session_state['all_completed'][n - 1] = all_completed


def feedback():
    st.write("")
    st.markdown('#### 피드백 작성')
    feed_questions = [
        "1. '추천 직무', '추천 직종', '직종 키워드', '추천 자격증', '채용 정보 검색어'에 대해 미흡한 점 또는 개선할 점이 있다면 작성해주세요.",
        "2. 생성된 구인공고 초안의 미흡한 점 또는 개선할 점이 있다면 작성해주세요."
    ]
    for i, question in enumerate(feed_questions):
        st.markdown(f'<div class="question-radio">{question}</div>', unsafe_allow_html=True)
        response = st.text_area(' ', key=f'feedback{i}', value=st.session_state['feedback'][i], label_visibility='collapsed')
        st.session_state['feedback'][i] = response


def check_all_completed():
    return all(st.session_state['all_completed'])


# 제출 버튼 처리
def submit():
    incomplete_sections = []
    for i in range(1, 21):
        context = st.session_state[f'context{i}']
        for category_key in ['acc', 'comp', 'gram', 'flue', 'usef']:
            if not context[category_key]['completed']:
                category_names = {'acc': '정확성', 'comp': '완전성', 'gram': '문법성', 'flue': '유창성', 'usef': '유용성'}
                incomplete_sections.append((i, category_names[category_key]))

    # 피드백 미완료 항목 확인
    for i, feedback in enumerate(st.session_state['feedback']):
        if feedback.strip() == '':
            incomplete_sections.append(('피드백', f'{i + 1}번 피드백'))

    if incomplete_sections:
        # for section in incomplete_sections:
        #     st.warning(f'상황 {section[0]}의 {section[1]} 평가 문항이 완료되지 않았습니다. 평가를 완료해주세요.')
        for section in incomplete_sections:
            if section[0] == '피드백':
                st.warning(f'{section[1]} 문항이 완료되지 않았습니다. 답변을 작성해주세요.')
            else:
                st.warning(f'상황 {section[0]}의 {section[1]} 평가 문항이 완료되지 않았습니다. 평가를 완료해주세요.')
        st.warning('모든 문항의 답을 작성하셔야 제출 버튼이 활성화됩니다.')
    else:
        st.success('모든 평가가 완료되었습니다. 제출 버튼을 눌러주세요.')
        if st.button('제출하기'):
            gen_csv()


# CSV 파일 생성 함수
def gen_csv():
    data = {}
    max_length = 0

    # 각 상황의 최대 길이 확인
    for i in range(1, 21):
        context = st.session_state[f'context{i}']
        max_length = max(max_length, len(context['acc']['responses']),
                         len(context['comp']['responses']),
                         len(context['gram']['responses']),
                         len(context['flue']['responses']),
                         len(context['usef']['responses']))

    # 최대 길이에 맞게 데이터를 확장하여 균일하게 맞추기
    for i in range(1, 21):
        context = st.session_state[f'context{i}']
        data[f'상황{i}_정확성'] = context['acc']['responses'] + [''] * (max_length - len(context['acc']['responses']))
        data[f'상황{i}_완전성'] = context['comp']['responses'] + [''] * (max_length - len(context['comp']['responses']))
        data[f'상황{i}_문법성'] = context['gram']['responses'] + [''] * (max_length - len(context['gram']['responses']))
        data[f'상황{i}_유창성'] = context['flue']['responses'] + [''] * (max_length - len(context['flue']['responses']))
        data[f'상황{i}_유용성'] = context['usef']['responses'] + [''] * (max_length - len(context['usef']['responses']))

    # 피드백 부분도 최대 길이에 맞추기
    data['피드백'] = st.session_state['feedback'] + [''] * (max_length - len(st.session_state['feedback']))

    # 데이터프레임 생성
    df = pd.DataFrame(data)
    st.write(df)
    df.to_csv(f'{st.session_state["name"]}_{st.session_state["company"]}.csv', encoding='utf-8-sig')



