import streamlit as st
from PIL import Image
from mood import interpret_mood
from filters import apply_mood_filter

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

if uploaded_image:
    image = Image.open(uploaded_image).convert("RGB")
    st.markdown("### Original Image")
    st.image(image, use_container_width=True)

if apply_button and uploaded_image:
    detected_mood = interpret_mood(mood_text)

    st.markdown("### Mood Analysis")
    st.write(f"**Detected mood:** `{detected_mood}`")
    st.write(f"**Effect intensity:** `{intensity}`")

    processed_image = apply_mood_filter(
        image=image,
        mood=detected_mood,
        intensity=intensity
    )

    st.markdown("### Processed Image")
    st.image(processed_image, use_container_width=True)

if apply_button and not uploaded_image:
    st.warning("Please upload an image first.")
