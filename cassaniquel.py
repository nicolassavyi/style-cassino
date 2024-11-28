import itertools
import random
import streamlit as st
from time import sleep

st.set_page_config(
    page_title="My App",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f5; /* Background color */
    }
    .header {
        background-color: #007bff; /* Header color */
        color: white;
        padding: 10px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="header"><h1>My Awesome App</h1></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

image1 = Image.open("ihttps://github.com/nicolassavyi/cassaniquel.py/blob/main/assets/BACKGROUND.png") # Substitua pelos caminhos das suas imagens
image2 = Image.open("image2.jpg")
image3 = Image.open("image3.jpg")


with col1:
    st.image(image1, caption="Image 1", use_column_width=True)

with col2:
    st.image(image2, caption="Image 2", use_column_width=True)

with col3:
    st.image(image3, caption="Image 3", use_column_width=True)