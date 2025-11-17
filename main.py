import streamlit as st

st.set_page_config(page_title="나라별 MBTI 분석", layout="wide")

st.title("🌍 나라별 MBTI 분석 사이트")
st.write("""
이 사이트는 GitHub + Streamlit 으로 제작되었으며,
나라별 MBTI 데이터를 다양한 방식으로 시각화합니다.
왼쪽 사이드바에서 페이지를 이동할 수 있습니다.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/MBTI_types.png/640px-MBTI_types.png", 
         caption="MBTI 유형 안내")
