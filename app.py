import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.DataFrame({
    "date": pd.to_datetime([
        "2026-01-01", "2026-01-01", "2026-01-01",
        "2026-02-01", "2026-02-01", "2026-02-01",
        "2026-03-01", "2026-03-01", "2026-03-01",
        "2026-04-01", "2026-04-01", "2026-04-01",
        "2026-05-01", "2026-05-01", "2026-05-01",
        "2026-06-01", "2026-06-01", "2026-06-01",
    ]),
    "category": [
        "PC", "모바일", "주변기기",
        "PC", "모바일", "주변기기",
        "PC", "모바일", "주변기기",
        "PC", "모바일", "주변기기",
        "PC", "모바일", "주변기기",
        "PC", "모바일", "주변기기",
    ],
    "sales": [
        180, 140, 100,
        195, 150, 108,
        205, 165, 115,
        220, 180, 125,
        235, 205, 130,
        250, 225, 142,
    ],
    "profit": [
        42, 30, 18,
        45, 32, 19,
        48, 35, 21,
        52, 39, 23,
        56, 45, 24,
        60, 50, 27,
    ],
    "orders": [
        90, 75, 110,
        96, 80, 116,
        102, 88, 121,
        108, 96, 127,
        116, 105, 132,
        124, 115, 140,
    ],
})

fig = px.bar(
    df,
    x='category',
    y='sales'
)

selected_category = st.selectbox(
    '카테고리를 선택하세요',
    options=df['category'].unique()
)

filtered = df[df['category'] == selected_category]

fig = px.line(
    filtered,
    x='date',
    y='sales',
    markers=True,
    title=f'{selected_category} 월별 매출'
)

st.plotly_chart(
    fig,
    width='stretch'
)
