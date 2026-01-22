import streamlit as st
from PIL import Image

st.set_page_config(page_title="MoodLens", layout="centered")

st.title("MoodLens")
st.subheader("Turn your mood into a visual style")

uploaded_image = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

mood_text = st.text_input(
    "How are you feeling right now?",
    placeholder="happy, sad, calm, angry..."
)

intensity = st.slider(
    "Effect intensity",
    min_value=0.0,
    max_value=1.0,
    value=0.5
)

apply_button = st.button("Apply Mood Filter")
