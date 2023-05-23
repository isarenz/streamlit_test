import streamlit as st
import mymodel as m

st.write("""
# Sales model""")

window = st.slider("Forecast")
st.write(m.run(window=window))
