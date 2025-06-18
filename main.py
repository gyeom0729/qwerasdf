import streamlit as st
import random

# 한글 단어 리스트 (예시용 간단 단어들)
word_list = [
    "사과", "과일", "일기", "기차", "차표", "표범", "범죄", "죄수", "수박", "박수",
    "수염", "염소", "소나무", "무지개", "개미", "미소", "소금", "금붕어", "어항", "항구"
]

st.title("끝말잇기 게임 🎮")

# 상태 저장: 이전 단어와 게임 진행 상황
if "prev_word" not in st.session_state:
    st.session_state.prev_word = None
if "used_words" not in st.session_state:
    st.session_state.used_words = []

def get_last_char(word):
    return word[-1]

def get_first_char(word):
    return word[0]

def get_computer_word(last_char, used_words):
    # 마지막 글자로 시작하고 아직 사용 안 한 단어 중 랜덤 선택
    candidates = [w for w in word_list if get_first_char(w) == last_char and w not in used_words]
    if candidates:
        return random.choice(candidates)
    else:
        return None  # 더 이상 단어가 없으면 게임 끝

# 게임 시작 안내
if st.session_state.prev_word is None:
    st.write("끝말잇기를 시작합니다! 단어를 입력해 주세요.")
else:
    st.write(f"이전 단어: **{st.session_state.prev_word}**")

# 사용자 입력 받기
user_word = st.text_input("단어 입력", key="input")

if st.button("제출"):
    if not user_word:
        st.warning("단어를 입력해 주세요!")
    elif user_word in st.session_state.used_words:
        st.warning("이미 사용된 단어입니다!")
    elif st.session_state.prev_word and get_first_char(user_word) != get_last_char(st.session_state.prev_word):
        st.warning(f"단어가 이전 단어의 마지막 글자 '{get_last_char(st.session_state.prev_word)}'로 시작하지 않습니다!")
    elif user_word not in word_list:
        st.warning("단어 리스트에 없는 단어입니다!")
    else:
        # 사용자 단어 저장
        st.session_state.used_words.append(user_word)
        st.session_state.prev_word = user_word
        
        # 컴퓨터 차례
        comp_word = get_computer_word(get_last_char(user_word), st.session_state.used_words)
        if comp_word:
            st.session_state.used_words.append(comp_word)
            st.session_state.prev_word = comp_word
            st.success(f"컴퓨터가 선택한 단어: **{comp_word}**\n당신 차례입니다!")
        else:
            st.balloons()
            st.success("축하합니다! 컴퓨터가 더 이상 단어를 찾지 못해 당신이 이겼어요!")
            # 게임 초기화
            st.session_state.prev_word = None
            st.session_state.used_words = []

# 사용된 단어 보여주기
st.write("사용된 단어들:", ", ".join(st.session_state.used_words))
