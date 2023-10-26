import streamlit as st

st.header("Newsletter Singup")

with st.form("NewsLetter", clear_on_submit=True):
    st.text_input("Name")
    st.text_input("Email Address")
    st.selectbox(
        "Gender",
        ('Female', 'Male', 'Attack Helicopter', 'Xbox 360', 'Other')
    )
    st.slider("Age", 0, 130)

    st.form_submit_button("Submit")