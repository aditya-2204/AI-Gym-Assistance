# AI Gym Assistance 🏋️‍♂️🤖

An intelligent, real-time AI workout coach and exercise form analyzer powered by Computer Vision and Large Language Models. **AI Gym Assistance** tracks body posture via camera stream, counts repetitions accurately, evaluates exercise form, and provides real-time voice and audio coaching feedback.

---

## 🌟 Key Features

- **Unified Single-App Experience**: Features an integrated landing page, biomechanics guide, and live camera workout studio in one cohesive web application.
- **Real-Time Pose Estimation & Form Analysis**: Utilizes Google MediaPipe and OpenCV to track 33 body landmarks with high precision and sub-100ms latency.
- **Accurate Repetition Counting & State Tracking**: Real-time geometric angle calculations and state machines for reliable repetition tracking.
- **AI Voice Coaching**: Powered by Groq LLMs and Google Text-to-Speech (gTTS) for conversational, motivating audio guidance during workouts.
- **5 Supported Exercises**:
  - 🦾 Biceps Curls (Elbow pin tracking & swing elimination)
  - 🏋️‍♂️ Squats (Depth angle tracking & spine verticality)
  - 🧘 Lunges (90° knee angle & balance tracking)
  - 💪 Push-ups (Elbow depth & body plank alignment)
  - 🏋️ Shoulder Press (Overhead lockout & arch monitor)
- **Webcam Streaming via WebRTC**: Low-latency video streaming in the browser via `streamlit-webrtc`.
- **User Authentication & Workout History**: SQLite-backed session persistence and historical exercise metrics.
- **100% Client-Side Camera Privacy**: Video frames are processed locally on your device and are never sent to external servers.

---

## 🏗️ Project Architecture

```
AI-Gym-Assistance/
├── main.py                    # Unified application entry point (Home + Studio + Analytics)
├── requirements.txt           # Python dependencies (Streamlit, MediaPipe, OpenCV, etc.)
├── packages.txt               # Linux system dependencies for Streamlit Cloud (libgl, libglib)
│
├── core/                      # Base exercise interfaces & abstract classes
├── detectors/                 # Exercise biomechanics & repetition detection logic
│   ├── biceps_curl.py
│   ├── lunges.py
│   ├── pushup.py
│   ├── shoulder_press.py
│   └── squat.py
├── ml_models/                 # MediaPipe pose landmarker models
├── services/                  # Modular backend & UI services
│   ├── auth/                  # User authentication wall
│   ├── coaching/              # Groq LLM coach, TTS, and voice pipeline
│   ├── config/                # Workout configuration & joint angle thresholds
│   ├── persistence/           # SQLite database & history storage
│   ├── state/                 # Streamlit session state management
│   ├── tracking/              # Repetition & metrics synchronization
│   ├── ui/                    # CSS, fonts, and landing page views
│   └── vision/                # WebRTC video frame processor
├── static/                    # Stylesheets and font assets
└── README.md
```

---

## ☁️ Deploy in 1 Click (Streamlit Community Cloud)

You can deploy this entire application to **[Streamlit Community Cloud](https://share.streamlit.io)** with zero manual configuration:

1. Sign in to **[share.streamlit.io](https://share.streamlit.io)** with your GitHub account (**aditya-2204**).
2. Click **"New app"**.
3. Select:
   - **Repository**: `aditya-2204/AI-Gym-Assistance`
   - **Branch**: `main`
   - **Main file path**: `main.py`
4. *(Optional — for Voice Coaching)*: In **Advanced Settings** → **Secrets**, add:
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key_here"
   ```
5. Click **"Deploy"**!

---

## 🚀 Local Installation & Setup

### Prerequisites

- Python 3.9 - 3.12
- A working webcam
- (Optional) [Groq API Key](https://console.groq.com) for real-time AI voice coaching

### 1. Clone the Repository

```bash
git clone https://github.com/aditya-2204/AI-Gym-Assistance.git
cd AI-Gym-Assistance
```

### 2. Set Up Virtual Environment

```bash
# Create venv
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables (Optional)

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the Application

```bash
streamlit run main.py
```

Open your browser at `http://localhost:8501`.

---

## 🛠️ Tech Stack

- **Computer Vision**: [Google MediaPipe](https://developers.google.com/mediapipe), [OpenCV](https://opencv.org/)
- **Frontend / Framework**: [Streamlit](https://streamlit.io/), [Streamlit-WebRTC](https://github.com/whitphx/streamlit-webrtc)
- **AI & Coaching**: [Groq](https://groq.com/), [gTTS](https://gtts.readthedocs.io/)
- **Storage**: SQLite3, Pandas
- **Typography**: Plus Jakarta Sans, Outfit, JetBrains Mono

---

## 👤 Author

**Aditya Saxena**  
- GitHub: [@aditya-2204](https://github.com/aditya-2204)  
- LinkedIn: [Aditya Saxena](https://www.linkedin.com/in/aditya-saxena-976511281)  
- Email: [aditya808166@gmail.com](mailto:aditya808166@gmail.com)

---

## 📄 License

This project is open-source under the MIT License.