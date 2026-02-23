import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/generate"

st.title("🎙️ Empathy Engine")

text = st.text_area("Enter text")

if st.button("Generate Emotional Speech"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            response = requests.post(API_URL, json={"text": text})

            if response.status_code == 200:
                data = response.json()

                st.success(f"Detected Emotion: {data['emotion'].capitalize()}")
                st.info(f"Emotion Intensity: {data['intensity']}")

                # Load audio file separately
                audio_response = requests.get("http://127.0.0.1:8000/audio")
                st.audio(audio_response.content, format="audio/wav")
            else:
                st.error(f"Backend Error: {response.text}")

        except Exception as e:
            st.error(f"Connection Error: {e}")