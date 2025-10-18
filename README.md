# 🎵 MoodTune – AI-Powered Mood-Based Music Recommender

> **"Let your mood choose the music."**  
> MoodTune uses **AI emotion detection** 🎭 and **Spotify integration** 🎧 to recommend playlists that match your vibe — in real time.

---

## 🧠 Overview

**MoodTune** captures your face using a webcam, detects your emotion (like happy, sad, angry, etc.) using **DeepFace**, and then recommends a **Spotify playlist** that fits your mood.  
It’s an awesome mix of **Computer Vision, AI, and Music APIs**!

---

## 🚀 Features

- 🎥 Real-time Emotion Detection via webcam  
- 🧠 AI-powered Facial Analysis with DeepFace  
- 🎶 Spotify Playlist Recommendations based on your mood  
- 🪟 Simple GUI built with Tkinter  
- 🧩 Combines Computer Vision + AI + Spotify API  

---

## 🧰 Tech Stack

| Category | Technology |
|-----------|-------------|
| **Language** | Python 🐍 |
| **AI/ML Library** | DeepFace, TensorFlow |
| **Computer Vision** | OpenCV |
| **API Integration** | Spotify Web API (Spotipy) |
| **GUI Framework** | Tkinter |

---

## 🧩 Architecture

```mermaid
flowchart TD
    A[User Webcam] --> B[OpenCV Capture]
    B --> C[DeepFace Emotion Detection]
    C --> D{Detected Emotion}
    D --> E[Map Emotion → Mood Keyword]
    E --> F[Spotify API Search (Spotipy)]
    F --> G[Top Playlist Recommendation]
    G --> H[Display in GUI]

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/MoodTune.git
cd MoodTune

### 2️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate    # For Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Setup Spotify API Credentials

CLIENT_ID = "your_client_id_here"
CLIENT_SECRET = "your_client_secret_here"

### 5️⃣ Run the App
python main.py
