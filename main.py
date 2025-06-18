import streamlit as st
import random

st.title("베스킨라빈스 31 게임 🎲")

if "current_num" not in st.session_state:
    st.session_state.current_num = 0
if "turn" not in st.session_state:
    st.session_state.turn = "user"  # user 또는 computer

def computer_move(current):
    # 컴퓨터가 부를 숫자 개수 결정 (1~3)
    # 간단 전략: 현재 숫자 + (1~3) 중에서 31에 가까워지는 수 선택
    target = 31
    for i in range(1, 4):
        if current + i == target:
            return i
    # 아니면 랜덤
    return random.randint(1,3)

st.write(f"현재 숫자: **{st.session_state.current_num}**")
st.write(f"턴: **{st.session_state.turn}**")

if st.session_state.turn == "user":
    count = st.number_input("몇 개의 숫자를 부르시겠어요? (1~3)", min_value=1, max_value=3, step=1)
    if st.button("말하기"):
        # 사용자 차례
        next_num = st.session_state.current_num + count
        if next_num >= 31:
            st.error(f"{next_num}을 부르셨네요. 당신이 졌습니다! 😢")
            st.session_state.current_num = 0
            st.session_state.turn = "user"
            st.experimental_rerun()
        else:
            st.session_state.current_num = next_num
            st.session_state.turn = "computer"
            st.experimental_rerun()

else:
    # 컴퓨터 차례
    comp_count = computer_move(st.session_state.current_num)
    next_num = st.session_state.current_num + comp_count
    st.write(f"컴퓨터가 {comp_count}개 숫자를 부릅니다.")
    if next_num >= 31:
        st.success(f"컴퓨터가 {next_num}을 부르면서 졌습니다! 당신이 이겼어요! 🎉")
        st.session_state.current_num = 0
        st.session_state.turn = "user"
        st.experimental_rerun()
    else:
        st.session_state.current_num = next_num
        st.session_state.turn = "user"
        st.experimental_rerun()
