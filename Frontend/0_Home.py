import i18n
import streamlit as st

from utils.init import init_once
from PIL import Image
import base64

def load_image(image_path):
    return Image.open(image_path)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()

if __name__ == '__main__':

    # Custom CSS
    st.markdown(
        """
        <style>
        .stApp {{
             background-image: url("https://i.imgur.com/uqf3Cba.png");
             background-attachment: fixed;
             background-size: cover
             
         }}
        .centered-button {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100px;  /* Adjust height to move the button vertically */
        }
        .rounded-button {
            display: inline-block;
            padding: 10px 20px;
            font-size: 18px;
            color: white;
            background-color: #fcf9c0;
            border-radius: 12px;
            text-align: center;
            text-decoration: none;
        }
        .rounded-button:hover {
            background-color: #e6e5a3;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # Init
    init_once()

    # Load an image for the header
    header_image = load_image('./header1.png')  # Replace with your image path

    # Display the image
    st.image(header_image, use_column_width=True)

    # Show page description with a larger font size and custom style
    st.markdown(f"<h3 style='text-align: center; color: #4682B4;'>{i18n.t('common.description')}</h3>", unsafe_allow_html=True)

    link = "https://computer-system-team-17.dev.mobilex.kr/menu_picker"
    st.markdown(f'<div class="centered-button"><a href="{link}" class="rounded-button">GO</a></div>', unsafe_allow_html=True)


