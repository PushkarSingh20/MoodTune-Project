import cv2
from deepface import DeepFace
import tkinter as tk
from tkinter import messagebox
import threading
import webbrowser

# --- Playlist dictionary based on emotion ---
playlists = {
    "happy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
    "sad": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
    "angry": "https://open.spotify.com/playlist/37i9dQZF1DWYxwmBaMqxsl",
    "surprise": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0",
    "neutral": "https://open.spotify.com/playlist/37i9dQZF1DX3Ogo9pFvBkY",
    "fear": "https://open.spotify.com/playlist/37i9dQZF1DX0FOF1IUWK1W",
    "disgust": "https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634"
}

# --- Webcam detection function ---
def detect_emotion():
    cap = cv2.VideoCapture(0)
    emotion_counts = {}

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = analysis[0]['dominant_emotion']

            # Count occurrences of each emotion
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1

            # Display emotion on webcam window
            cv2.putText(frame, f"Emotion: {emotion}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Emotion Detection', frame)

        except Exception as e:
            print("Error:", e)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Find the dominant (most frequent) emotion
    if emotion_counts:
        dominant_emotion = max(emotion_counts, key=emotion_counts.get)
        show_playlist(dominant_emotion)
    else:
        messagebox.showinfo("Result", "No emotion detected.")

# --- Function to show playlist based on emotion ---
def show_playlist(emotion):
    emotion = emotion.lower()
    messagebox.showinfo("Emotion Detected", f"You seem {emotion}!")
    if emotion in playlists:
        webbrowser.open(playlists[emotion])
    else:
        messagebox.showinfo("Playlist", "No playlist found for your emotion.")

# --- Threading to avoid freezing GUI ---
def start_detection_thread():
    threading.Thread(target=detect_emotion).start()

# --- GUI Setup ---
root = tk.Tk()
root.title("MoodTune 🎧")
root.geometry("400x300")
root.configure(bg="#1e1e2f")

label = tk.Label(root, text="🎵 MoodTune - AI Emotion Music Recommender 🎵",
                 bg="#1e1e2f", fg="white", font=("Helvetica", 12, "bold"), wraplength=350)
label.pack(pady=30)

start_btn = tk.Button(root, text="Start Emotion Detection 🎥",
                      command=start_detection_thread,
                      bg="#00adb5", fg="white", font=("Helvetica", 11, "bold"),
                      relief="raised", padx=10, pady=5)
start_btn.pack(pady=20)

info_label = tk.Label(root, text="Press 'q' to stop webcam",
                      bg="#1e1e2f", fg="gray", font=("Helvetica", 9))
info_label.pack(pady=10)

root.mainloop()
