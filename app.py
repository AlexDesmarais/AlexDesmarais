# app.py
import streamlit as st
import tempfile
from video import extract_audio
from audio import split_audio
from recognition import recognize_song_chunks

st.set_page_config(page_title="Concert Setlist Builder", layout="centered")
st.title("🎶 Concert Video to Setlist")

uploaded_file = st.file_uploader("Upload Concert Video", type=["mp4", "mov"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_video:
        tmp_video.write(uploaded_file.read())
        video_path = tmp_video.name
        st.success("Video uploaded!")

    if st.button("Extract and Recognize"):
        with st.spinner("Processing video..."):
            audio_path = extract_audio(video_path)
            chunks = split_audio(audio_path)

            songs = recognize_song_chunks(chunks)
            if songs:
                st.subheader("🎵 Recognized Setlist")
                for i, title in enumerate(songs, 1):
                    st.write(f"{i}. {title}")
            else:
                st.warning("No songs recognized.")
