from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from emotion import detect_emotion
from tts_engine_elevenlabs import generate_speech
import os

app = FastAPI(title="Empathy Engine API")


class TextRequest(BaseModel):
    text: str


@app.post("/generate")
def generate_audio(request: TextRequest):

    emotion, intensity = detect_emotion(request.text)
    audio_path = generate_speech(request.text, emotion, intensity)

    return {
        "emotion": emotion,
        "intensity": round(intensity, 2),
        "audio_file": audio_path
    }
@app.get("/audio")
def get_audio():
    return FileResponse("output/speech.wav", media_type="audio/wav")