import streamlit as st
import random

st.title("베스킨라빈스 31 게임 🎲")

if "current_num" not in st.session_state:
    st.session_state.current_num = 0
if "turn" not in st.session_state:
    st.session_state.turn = "user"
if "message" not in st.session_state:
    st.session_state.message = ""

def computer_move(current):
    target = 31
    for i in range(1, 4):
        if current + i == target:
            return i
    remainder = (target - current - 1) % 4
    if remainder == 0:
        return random.randint(1, 3)
    else:
        return remainder

def reset_game():
    st.session_state.current_num = 0
    st.session_state.turn = "user"
    st.session_state.message = ""

def computer_turn():
    comp_count = computer_move(st.session_state.current_num)
    next_num = st.session_state.current_num + comp_count
    st.write(f"컴퓨터가 {comp_count}개 숫자를 부릅니다.")
    if next_num >= 31:
        st.session_state.message = f"컴퓨터가 {next_num}을 부르면서 졌습니다! 당신이 이겼어요! 🎉"
        reset_game()
    else:
        st.session_state.current_num = next_num
        st.session_state.turn = "user"
        st.session_state.message = ""

st.write(f"현재 숫자: **{st.session_state.current_num}**")
st.write(f"턴: **{st.session_state.turn}**")

if st.session_state.message:
    st.info(st.session_state.message)

if st.session_state.turn == "user":
    count = st.number_input("몇 개의 숫자를 부르시겠어요? (1~3)", min_value=1, max_value=3, step=1, key="user_input")
    if st.button("말하기"):
        next_num = st.session_state.current_num + count
        if next_num >= 31:
            st.session_state.message = f"{next_num}을 부르셨네요. 당신이 졌습니다! 😢"
            reset_game()
            st.experime
