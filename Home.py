import streamlit as st

def main():
    st.set_page_config(page_title="Welcome to the Titanic App 🚢🚢🚢", page_icon="🚢")
    st.title("Titanic Model App 🚢")
    st.write(
        """
        This simple web app allows you to **analyze** the Titanic dataset  
        and **predict** passenger survival probability using a trained model.
        """
    )
    if st.button("Go to Titanic App"):
        st.switch_page("pages/app.py")
    if st.button("Go to Titanic Prediction"):
        st.switch_page("pages/titanic-prediction.py")

if __name__ == "__main__":
    main()
