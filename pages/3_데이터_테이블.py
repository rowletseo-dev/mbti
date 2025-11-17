import streamlit as st
import pandas as pd

st.title("📘 전체 데이터 테이블")

@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

st.write("업로드된 MBTI 데이터:")
st.dataframe(df)

st.download_button(
    label="📥 CSV 다운로드",
    data=df.to_csv(index=False),
    file_name="mbti_data.csv",
    mime="text/csv"
)
