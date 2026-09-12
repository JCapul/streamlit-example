import streamlit as st

st.set_page_config(page_title="Forecast dashboard", page_icon="☀️")
st.title("Forecast dashboard")
st.write("A small public Streamlit application for deployment acceptance.")

days = st.slider("Forecast horizon", min_value=1, max_value=14, value=7)
st.line_chart({"temperature": [18 + (day % 4) for day in range(days)]})
