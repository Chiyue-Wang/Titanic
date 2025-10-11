import streamlit as st

def main():
    st.set_page_config(page_title="Welcome to the Titanic Model App")
    st.title("Titanic Model App")
    st.write(
        """
        Welcome to the Titanic Model Streamlit Application!  
        Use the button below to navigate to the main app page for model predictions and analysis.
        """
    )
    if st.button("Go to App"):
        st.switch_page("pages/app.py")

if __name__ == "__main__":
    main()
