import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="EC2 Streamlit 배포 실습",
    page_icon="💻",
    layout="centered"
)

st.title("💻 EC2 Streamlit 배포 실습 앱")

st.divider()

st.subheader("📌 과제 정보")
st.write("이 앱은 AWS EC2 환경에서 Streamlit 앱을 배포하는 실습용 앱입니다.")
st.write("브라우저에서 앱을 조작하면 EC2 터미널에 로그가 출력됩니다.")

st.divider()

# 이전 입력값 저장용
if "last_name" not in st.session_state:
    st.session_state.last_name = ""

if "click_count" not in st.session_state:
    st.session_state.click_count = 0

st.subheader("📝 사용자 입력")

name = st.text_input("이름을 입력하세요")

# 입력값이 바뀌었을 때 터미널 로그 출력
if name != st.session_state.last_name:
    print(
        f"[LOG] 입력값 변경됨 | 입력값: {name} | 시간: {datetime.now()}",
        flush=True
    )
    st.session_state.last_name = name

st.write(f"현재 입력값: {name}")

st.divider()

st.subheader("✅ 동작 확인")

if st.button("확인 버튼 클릭"):
    st.session_state.click_count += 1

    st.success(f"{name}님, Streamlit 앱이 EC2에서 정상 실행 중입니다!")

    print(
        f"[LOG] 버튼 클릭됨 | 입력값: {name} | 클릭 횟수: {st.session_state.click_count} | 시간: {datetime.now()}",
        flush=True
    )

st.write(f"버튼 클릭 횟수: {st.session_state.click_count}")

st.divider()

st.caption("OSS 실습 3 - EC2 Streamlit 배포 과제")
