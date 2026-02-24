# 🎙 Emotion-Aware Neural Text-to-Speech System

An **AI-based Emotion-Aware Text-to-Speech (TTS) system** that converts plain text into **emotionally expressive speech**.

The system analyzes the emotional tone of input text using **sentiment analysis** and adjusts voice characteristics such as **stability, speaking style, and intensity** before generating speech with a **neural TTS model**.

The project uses **FastAPI for the backend**, **Streamlit for the frontend**, and the **ElevenLabs neural TTS API** for high-quality speech synthesis.

---

## 🚀 Features

* Emotion detection using **VADER Sentiment Analysis (NLTK)**
* Emotion-based voice modulation
* Neural speech generation using ElevenLabs API
* FastAPI REST backend
* Interactive Streamlit frontend
* Environment-variable based API key configuration
* Real-time text-to-speech generation

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
Neural TTS Generation (ElevenLabs)
   ↓
Emotionally Expressive Audio Output (.wav)
```

---

## 🛠 Tech Stack

* Python 3.10+
* FastAPI
* Streamlit
* NLTK (VADER Sentiment Analyzer)
* ElevenLabs API
* Uvicorn
* Requests

---

## 📂 Project Structure

```
.
├── main.py                  # FastAPI backend
├── frontend.py              # Streamlit frontend
├── emotion.py               # Emotion detection module
├── tts_engine_elevenlabs.py # ElevenLabs TTS integration
├── requirements.txt
└── output/
    └── speech.wav
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/Mac**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project directory:

```
ELEVENLABS_API_KEY=your_api_key_here
```

Replace with your actual ElevenLabs API key.

---

## ▶️ Running the Application

### Start Backend

```bash
python -m uvicorn main:app --reload
```

Backend API will run at:

```
http://127.0.0.1:8000/docs
```

---

### Start Frontend

Open a new terminal and run:

```bash
streamlit run frontend.py
```

Frontend will run at:

```
http://localhost:8501
```

---

## 🎯 Core Design

### Emotion Detection

The system uses **VADER sentiment analysis** to determine the emotional tone of the input text.

Compound sentiment score:

* **≥ 0.4 → Positive**
* **≤ -0.4 → Negative**
* Otherwise → Neutral

Emotion intensity is calculated using the absolute value of the compound score.

---

### Voice Parameter Mapping

The detected emotion is mapped to different voice settings:

| Emotion  | Stability | Similarity Boost | Style      |
| -------- | --------- | ---------------- | ---------- |
| Positive | Low       | High             | Expressive |
| Negative | High      | Moderate         | Calm       |
| Neutral  | Balanced  | Balanced         | Natural    |

These parameters are passed to the ElevenLabs API to produce expressive speech.

---

## 🌱 Future Improvements

Possible enhancements include:

* Transformer-based emotion classification
* Real-time streaming audio
* Multiple voice options
* Multilingual support
* Deployment support
* Performance optimization

---

## 👨‍💻 Author

**Deepesh Lodhi**
AI & Data Science Enthusiast
IIT Delhi

If you want, I can make a **🔥 "FAANG-level README" version** that looks like a serious AI research project (great for internships).
