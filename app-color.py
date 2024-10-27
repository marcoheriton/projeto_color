import streamlit as st
import socket

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

hostname = socket.gethostname()
st.title("Simple Streamlit App")
st.write("This app has a blue background!")
st.write(f"O nome desta vm é {hostname}")