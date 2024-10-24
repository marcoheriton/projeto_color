import streamlit as st

# Set the background color using Streamlit's markdown feature
st.markdown(
    """
    <style>
    .stApp {
        background-color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Simple Streamlit App")
st.write("This app has a blue background!")
