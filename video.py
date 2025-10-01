# utils/video.py
import os
from moviepy import VideoFileClip

def extract_audio(video_path):
    audio_path = video_path.replace(".mp4", ".mp3")
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
    return audio_path
