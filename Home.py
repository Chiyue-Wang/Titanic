import streamlit as st

# 设置页面标题
st.set_page_config(page_title="Titanic App Home", page_icon="🚢")

# 页面主标题
st.title("Welcome to the Titanic App 🚢")

# 简短说明
st.write("""
This simple web app allows you to **analyze** the Titanic dataset  
and **predict** passenger survival probability using a trained model.
""")

if st.button("Go to Titanic App"):
    st.switch_page("app")

