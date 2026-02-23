# 🎙 Emotion-Aware Neural Text-to-Speech System

An AI-powered emotion-aware Text-to-Speech (TTS) system that converts plain text into emotionally expressive speech.

This project integrates NLP-based sentiment analysis with neural speech synthesis to dynamically modulate voice characteristics such as pitch, rate, stability, and speaking style based on detected emotional intensity.

Built using **FastAPI (backend)**, **Streamlit (frontend)**, and **ElevenLabs neural TTS API**, and fully containerized using Docker for cloud deployment.

---

## 🚀 Features

- Emotion detection using VADER Sentiment Analysis (NLTK)
- Dynamic prosody control (pitch, rate, stability)
- Neural speech synthesis via ElevenLabs API
- FastAPI-based REST backend
- Streamlit interactive frontend
- Dockerized backend for portable deployment
- Secure environment variable configuration
- Cloud deployable (Render / Streamlit Cloud)

---

## 🧠 System Architecture

```

User Input
↓
Streamlit Frontend
↓ (HTTP Request)
FastAPI Backend
↓
Emotion Detection (VADER)
↓
ElevenLabs Neural TTS API
↓
Emotionally Expressive Audio Output (.wav)

```

---

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- Streamlit
- NLTK (VADER Sentiment Analyzer)
- ElevenLabs API
- Docker
- Uvicorn
- Requests

---

## 📂 Project Structure

```

.
├── main.py                  # FastAPI backend
├── frontend.py              # Streamlit frontend
├── emotion.py               # Emotion detection logic
├── tts_engine_elevenlabs.py # Neural TTS integration
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── output/
└── speech.wav

````

---

## ⚙️ Setup Instructions (Local Development)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```

ELEVENLABS_API_KEY=your_api_key_here

```

---

## ▶️ Running the Application

### Start Backend

```bash
python -m uvicorn main:app --reload
```

Backend runs at:

```

http://127.0.0.1:8000/docs

```

### Start Frontend (New Terminal)

```bash
python -m streamlit run frontend.py
```

Frontend runs at:

```

http://localhost:8501

```

---

## 🐳 Docker Setup

### Build Docker Image

```bash
docker build -t emotion-tts .
```

### Run Container

```bash
docker run -p 8000:8000 -e ELEVENLABS_API_KEY=your_api_key emotion-tts
```

---

## ☁ Deployment

* Backend: Render (Docker-based deployment)
* Frontend: Streamlit Community Cloud
* Environment variables managed securely in deployment dashboard

---

## 🎯 Design Highlights

### Emotion Classification

Uses VADER compound sentiment score:

* ≥ 0.4 → Positive
* ≤ -0.4 → Negative
* Otherwise → Neutral

Intensity is derived from absolute compound score.

---

### Prosody Mapping Logic

| Emotion  | Stability | Similarity Boost | Style      |
| -------- | --------- | ---------------- | ---------- |
| Positive | Low       | High             | Expressive |
| Negative | High      | Moderate         | Calm       |
| Neutral  | Balanced  | Balanced         | Natural    |

---

## 🌱 Future Improvements

* Transformer-based emotion classification (multi-class)
* Real-time streaming audio
* Multiple voice profiles
* Multilingual support
* Kubernetes deployment
* Caching & rate limiting

---

## 👨‍💻 Author

**Deepesh Lodhi**
AI & Data Science Enthusiast
IIT Delhi

---

## ⭐ If You Found This Interesting

Feel free to star the repository or contribute!
