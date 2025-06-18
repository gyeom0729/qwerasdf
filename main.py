import streamlit as st

st.title("간단 끝말잇기 게임")

if "prev_word" not in st.session_state:
    st.session_state.prev_word = None
if "used_words" not in st.session_state:
    st.session_state.used_words = []

def get_last_char(word):
    return word[-1]

def get_first_char(word):
    return word[0]

user_word = st.text_input("단어 입력", key="input")

if st.button("제출"):
    if not user_word:
        st.warning("단어를 입력해 주세요!")
    elif user_word in st.session_state.used_words:
        st.warning("이미 사용한 단어입니다!")
    elif st.session_state.prev_word and get_first_char(user_word) != get_last_char(st.session_state.prev_word):
        st.warning(f"이전 단어의 마지막 글자 '{get_last_char(st.session_state.prev_word)}'로 시작하는 단어를 입력하세요!")
    else:
        st.session_state.used_words.append(user_word)
        st.session_state.prev_word = user_word
        st.success(f"좋아요! '{user_word}' 입력 완료!")

st.write("이전 단어:", st.session_state.prev_word if st.session_state.prev_word else "없음")
st.write("사용한 단어들:", ", ".join(st.session_state.used_words))
