import requests
import os

API_KEY = os.getenv("ELEVENLABS_API_KEY")

VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel (default high quality voice)

def generate_speech(text, emotion, intensity, filename="output/speech.wav"):

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    # Emotion → voice settings mapping
    emotion_settings = {
        "positive": {
            "stability": 0.25,
            "similarity_boost": 0.85
        },
        "negative": {
            "stability": 0.75,
            "similarity_boost": 0.45
        },
        "neutral": {
            "stability": 0.5,
            "similarity_boost": 0.6
        }
    }

    settings = emotion_settings.get(emotion, emotion_settings["neutral"])
        base = settings

        dynamic_settings = {
            "stability": min(max(base["stability"] + (intensity * 0.2), 0), 1),
            "similarity_boost": base["similarity_boost"]
    payload = {
        "text": text,
        "voice_settings": settings
    }

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    if not API_KEY:
        raise RuntimeError("ELEVENLABS_API_KEY is not set. Add it to a .env file or set the environment variable.")

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"ElevenLabs API Error: {response.status_code} - {response.text}")

    os.makedirs("output", exist_ok=True)

    with open(filename, "wb") as f:
        f.write(response.content)

    return filename

