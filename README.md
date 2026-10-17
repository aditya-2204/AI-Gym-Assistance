# AI Gym Assistance 🏋️‍♂️🤖

An intelligent, real-time AI workout coach and exercise form analyzer powered by Computer Vision and Large Language Models. **AI Gym Assistance** tracks body posture via camera stream, counts repetitions accurately, evaluates exercise form, and provides real-time voice and audio coaching feedback.

---

## 🌟 Key Features

- **Real-Time Pose Estimation & Form Analysis**: Utilizes Google MediaPipe and OpenCV to track 33 body landmarks with high precision.
- **Accurate Repetition Counting & State Tracking**: Real-time geometric angle calculations and state machines for reliable repetition tracking.
- **AI Voice Coaching**: Powered by Groq LLMs and Google Text-to-Speech (gTTS) for conversational, motivating audio guidance during workouts.
- **Multiple Supported Exercises**:
  - 🦾 Biceps Curls
  - 🏋️‍♂️ Squats
  - 🧘 Lunges
  - 💪 Push-ups
  - 🏋️ Shoulder Press
- **Webcam Streaming via WebRTC**: Seamless low-latency video streaming in the browser via `streamlit-webrtc`.
- **User Authentication & Workout History**: SQLite-backed session persistence and historical exercise metrics.
- **Modern Landing Page**: Sleek, responsive landing page interface with custom typography and interactive sections.

---

## 🏗️ Project Architecture

```
AI-Gym-Assistance/
├── LandingPage/               # Web showcase & product landing page
│   ├── index.html             # Landing page structure
│   ├── style.css              # Custom styling & animations
│   ├── fonts/                 # Averta web fonts
│   ├── IMGs_add_your_own/     # Image assets folder
│   └── videos_add_your_own/   # Demo video assets folder
│
├── Main App/                  # Core Streamlit application
│   ├── main.py                # Application entry point
│   ├── requirements.txt       # Python dependencies
│   ├── packages.txt           # System-level dependencies
│   ├── core/                  # Base exercise interface & definitions
│   ├── detectors/             # Exercise detection & repetition logic
│   │   ├── biceps_curl.py
│   │   ├── lunges.py
│   │   ├── pushup.py
│   │   ├── shoulder_press.py
│   │   └── squat.py
│   ├── ml_models/             # MediaPipe pose landmarker models
│   ├── services/              # Modular backend services
│   │   ├── auth/              # User authentication wall
│   │   ├── coaching/          # LLM coach, TTS, and voice pipeline
│   │   ├── config/            # Workout configurations
│   │   ├── persistence/       # SQLite storage & database helpers
│   │   ├── state/             # Streamlit session state management
│   │   ├── tracking/          # Repetition & metrics synchronization
│   │   ├── ui/                # CSS and font styling loaders
│   │   └── vision/            # WebRTC video frame processor
│   └── static/                # Stylesheets and font assets
│
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 - 3.11
- A working webcam
- (Optional) [Groq API Key](https://console.groq.com) for real-time AI voice coaching

### 1. Clone the Repository

```bash
git clone https://github.com/aditya-2204/AI-Gym-Assistance.git
cd AI-Gym-Assistance
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
cd "Main App"
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file inside the `Main App` folder or set the environment variable:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the Application

```bash
streamlit run main.py
```

Open your browser at `http://localhost:8501`.

---

## 🌐 Running the Landing Page

To view the landing page:
1. Navigate to the `LandingPage` directory.
2. Open `index.html` in your web browser or use a live server (e.g., VS Code Live Server or `python -m http.server 3000`).

---

## 🛠️ Tech Stack

- **Computer Vision**: [MediaPipe](https://developers.google.com/mediapipe), [OpenCV](https://opencv.org/)
- **Frontend / Framework**: [Streamlit](https://streamlit.io/), [Streamlit-WebRTC](https://github.com/whitphx/streamlit-webrtc)
- **AI & Coaching**: [Groq](https://groq.com/), [gTTS](https://gtts.readthedocs.io/)
- **Storage**: SQLite3, Pandas
- **Web Design**: HTML5, CSS3, Modern Glassmorphism & Typography

---

## 👤 Author

**Aditya Saxena**  
- GitHub: [@aditya-2204](https://github.com/aditya-2204)
- LinkedIn: [Aditya Saxena](https://www.linkedin.com/in/aditya-saxena-976511281)
- Email: [aditya808166@gmail.com](mailto:aditya808166@gmail.com)

---

## 📄 License

This project is open-source under the MIT License.