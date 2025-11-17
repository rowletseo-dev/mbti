import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 세계 지도 기반 MBTI 시각화")

@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

mbti_types = [col for col in df.columns if col not in ["country", "code"]]

selected = st.selectbox("MBTI 선택", mbti_types)

fig = px.choropleth(
    df,
    locations="code",
    color=selected,
    hover_name="country",
    color_continuous_scale="Viridis",
    title=f"세계 지도 - {selected} 비율"
)

st.plotly_chart(fig, use_container_width=True)
