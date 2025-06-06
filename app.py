import streamlit as st
import sounddevice as sd
import numpy as np
import time

fs = 44100

def record_and_loop(duration_sec, loop_minutes):
    st.info("Recording started....")
    recording = sd.rec(int(duration_sec * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    st.success("Recording finished. Looping now...")

    end_time = time.time() + (loop_minutes * 60)
    while time.time() < end_time:
        sd.play(recording, samplerate=fs)
        sd.wait()

    st.success("Done looping!")

st.title("Voice Loop App")
duration = st.slider("Record Duration (seconds)", 1, 10, 5)
loop_time = st.slider("Loop Time (minutes)", 1, 5, 1)

if st.button("Start Recording and Loop"):
    record_and_loop(duration, loop_time)
