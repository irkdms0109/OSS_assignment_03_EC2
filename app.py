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
st.write("과제: EC2 Streamlit 배포 실습")

st.divider()

st.subheader("✏️ 간단한 입력 테스트")

name = st.text_input("이름을 입력하세요", placeholder="예: 이가은")

info = st.text_area(
    "간단한 정보 작성하기",
    placeholder="예: 인공지능융합대학 정보융합학부 학생"
)

if st.button("작성한 내용 확인하기"):
    if name and info:
        st.success("입력이 완료되었습니다!")
        st.write(f"👤 이름: {name}")
        st.write(f"🎯 정보 : {info}")
        st.write(f"⏰ 작성 확인 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        st.info("Streamlit 앱이 정상적으로 실행되고 있습니다.")
    else:
        st.warning("이름과 정보를 모두 입력해주세요.")

st.caption("OSS 과제용 EC2 Streamlit 배포 실습 앱")