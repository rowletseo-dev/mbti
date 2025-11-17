import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 나라별 MBTI 비교")

@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    return df

df = load_data()

mbti_types = [col for col in df.columns if col != "country"]
selected = st.selectbox("MBTI 유형 선택", mbti_types)

fig = px.bar(
    df,
    x="country",
    y=selected,
    text=selected,
    color="country",
    title=f"{selected} 분포 비교"
)

fig.update_traces(textposition="outside")
st.plotly_chart(fig, use_container_width=True)
