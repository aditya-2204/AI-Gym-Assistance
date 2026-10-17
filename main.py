import streamlit as st
import os
import time
import pandas as pd
from services.auth.login_wall import render_login_wall
from services.state.session_defaults import initial_session_defaults
from services.config.workout_config import EXERCISE_OPTIONS
from services.ui.style_loader import load_css, inject_local_font, inject_webrtc_styles
from services.persistence.exercise_repository import init_db, get_users_exercises
from streamlit_webrtc import webrtc_streamer, WebRtcMode
from services.vision.exercise_video_processor import VideoProcessorClass
from services.tracking.metrics import sync_metrics_update
from groq import Groq
from services.coaching.llm import LLMCoach
from services.coaching.tts import TextToSpeech
from services.coaching.voice_pipeline import VoicePipeline, autoplay_audio
from services.ui.landing_view import render_landing_view


def main():
    st.set_page_config(
        page_icon="🏋️‍♂️",
        page_title="AI Gym Assistance — Real-time AI Workout Coach",
        initial_sidebar_state="expanded",
        layout="wide"
    )

    # Resilient path resolution for styles and fonts
    possible_css = [
        os.path.join(os.getcwd(), "static", "style.css"),
        os.path.join(os.getcwd(), "Main App", "static", "style.css"),
        os.path.join(os.path.dirname(__file__), "static", "style.css"),
    ]
    css_path = next((p for p in possible_css if os.path.exists(p)), possible_css[0])
    load_css(css_path)

    possible_font = [
        os.path.join(os.getcwd(), "static", "AdobeClean.otf"),
        os.path.join(os.getcwd(), "Main App", "static", "AdobeClean.otf"),
        os.path.join(os.path.dirname(__file__), "static", "AdobeClean.otf"),
    ]
    font_path = next((p for p in possible_font if os.path.exists(p)), possible_font[0])
    inject_local_font(font_path, "AdobeClean")

    init_db()
    initial_session_defaults()

    if "voice_pipeline" not in st.session_state:
        try:
            api_key = os.environ.get("GROQ_API_KEY", "")

            if not api_key and hasattr(st, "secrets") and "GROQ_API_KEY" in st.secrets:
                api_key = st.secrets["GROQ_API_KEY"]

            groq_client = Groq(api_key=api_key)
            llm_coach = LLMCoach(groq_client)
            tts = TextToSpeech()
            st.session_state.voice_pipeline = VoicePipeline(llm_coach, tts)
        except Exception:
            st.session_state.voice_pipeline = None

    # Sidebar Navigation
    with st.sidebar:
        st.title("🏋️‍♂️ AI Gym Assistance")
        st.caption("Computer Vision & AI Workout Coach")

        if st.session_state.get("username"):
            st.success(f"👤 Logged in as **{st.session_state.username}**")
        else:
            st.caption("Guest Mode")

        st.divider()

        nav_options = ["🏠 Home & Biomechanics", "⚡ Workout Studio", "📊 Workout History"]
        if "app_nav" not in st.session_state:
            st.session_state["app_nav"] = "🏠 Home & Biomechanics"

        st.radio(
            "Navigation Menu",
            nav_options,
            key="app_nav"
        )

    # Route 1: Home & Biomechanics Landing View
    if st.session_state.app_nav == "🏠 Home & Biomechanics":
        render_landing_view()
        return

    # Route 2: Workout History
    elif st.session_state.app_nav == "📊 Workout History":
        st.title("📊 Personal Workout History")
        st.caption("All your completed exercise sets and repetition volume saved in database.")

        user_id = st.session_state.get("user_id")
        if not user_id:
            st.info("Please log in via the **Workout Studio** to access and record your personal workout history.")
            if st.button("Go to Workout Studio"):
                st.session_state.app_nav = "⚡ Workout Studio"
                st.rerun()
            return

        history_rows = get_users_exercises(user_id)
        arr = [
            {
                "Exercise": row["exercise_name"],
                "Reps": row["reps"],
                "Sets": row["sets"],
                "Duration (s)": row["time"],
                "Date": row["created_at"],
            }
            for row in history_rows
        ]

        df = pd.DataFrame(arr)
        if not df.empty:
            df["Date"] = pd.to_datetime(df["Date"]).dt.date
            agg_df = df.groupby(["Exercise", "Date"]).agg({
                "Reps": "sum",
                "Sets": "sum",
                "Duration (s)": "sum",
            }).reset_index()
            agg_df.index += 1

            st.dataframe(agg_df, use_container_width=True)
        else:
            st.info("No workouts recorded yet. Start your first session in the **Workout Studio**!")

        return

    # Route 3: Live Workout Studio
    elif st.session_state.app_nav == "⚡ Workout Studio":
        # Check login wall
        if not render_login_wall():
            return

        workout_started = st.session_state.get("workout_started", False)

        # Sidebar workout controls
        with st.sidebar:
            st.divider()
            st.subheader("Workout Controls")

            if not workout_started:
                plan_exercise = st.selectbox("Exercise", options=EXERCISE_OPTIONS, key="plan_exercise")
                plan_sets = st.number_input("Target Sets", min_value=1, max_value=50, value=3, key="plan_sets", step=1)
                plan_reps = st.number_input("Reps per Set", min_value=1, max_value=50, value=10, key="plan_reps", step=1)

                start_session_button = st.button("▶ Start Workout", type="primary", use_container_width=True, key="start_session_button")

                if start_session_button:
                    st.session_state.exercise_type = plan_exercise
                    st.session_state.target_sets = int(plan_sets)
                    st.session_state.reps_per_set = int(plan_reps)
                    st.session_state.reps = 0
                    st.session_state.workout_started = True
                    st.session_state.set_cycle_started_at = time.time()
                    st.session_state.last_saved_sets_completed = 0

                    if st.session_state.voice_pipeline:
                        result = st.session_state.voice_pipeline.process_event(
                            event="workout_started",
                            exercise=plan_exercise,
                            metrics={},
                        )
                        if result:
                            st.session_state.audio_to_play, st.session_state.coach_feedback = result

                    st.session_state.last_notified_sets_completed = 0
                    st.session_state.last_notified_workout_complete = False
                    st.rerun()
            else:
                exercise = st.session_state.get("exercise_type")
                sets = st.session_state.get("target_sets")
                reps = st.session_state.get("reps_per_set")

                st.info(f"**{exercise}** — {sets} Sets / {reps} Reps")

                end_session_button = st.button("⏹ End Workout", use_container_width=True, key="end_session_button")
                if end_session_button:
                    st.session_state.workout_started = False
                    if st.session_state.voice_pipeline:
                        result = st.session_state.voice_pipeline.process_event(
                            event="workout_completed",
                            exercise=exercise,
                            metrics={},
                        )
                        if result:
                            st.session_state.audio_to_play, st.session_state.coach_feedback = result
                    st.rerun()

            if workout_started:
                st.divider()
                st.subheader("Live Progress")
                total_reps = st.session_state.get("reps", 0)
                current_set_reps = st.session_state.get("current_set_reps", 0)
                reps_per_set = st.session_state.get("reps_per_set", 10)
                sets_completed = st.session_state.get("sets_completed", 0)
                target_sets = st.session_state.get("target_sets", 3)

                st.metric("Total Reps", f"{total_reps}")
                st.metric("Current Set", f"{current_set_reps} / {reps_per_set}")
                st.metric("Sets Completed", f"{sets_completed} / {target_sets}")

        # Main Studio View
        st.title("🏋️‍♂️ Live Workout Studio")
        st.caption("Position yourself in full view of the camera to activate 33-point pose landmark estimation.")

        if st.session_state.get("audio_to_play"):
            autoplay_audio(st.session_state.audio_to_play)

        if st.session_state.get("coach_feedback"):
            st.success(f"🤖 **AI Coach:** {st.session_state.coach_feedback}")

        if not workout_started:
            st.markdown(
                """
                <div style="
                    background: linear-gradient(145deg, #161b22 0%, #0e131b 100%);
                    border: 1px solid rgba(0, 240, 255, 0.25);
                    border-radius: 14px;
                    padding: 36px 28px;
                    text-align: center;
                    margin-top: 20px;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
                ">
                    <span style="
                        display: inline-block;
                        background: rgba(0, 240, 255, 0.12);
                        color: #00f0ff;
                        border: 1px solid rgba(0, 240, 255, 0.3);
                        border-radius: 20px;
                        padding: 4px 14px;
                        font-size: 0.8rem;
                        font-weight: 700;
                        letter-spacing: 0.05em;
                        margin-bottom: 14px;
                    ">
                        ⚡ CAMERA READY
                    </span>
                    <h2 style="color: #f0f6fc; margin: 0 0 10px 0; font-size: 1.6rem; font-weight: 800;">
                        Configure Your Routine in the Sidebar
                    </h2>
                    <p style="color: #8b949e; font-size: 0.95rem; max-width: 520px; margin: 0 auto 24px auto; line-height: 1.5;">
                        Select your exercise, configure target sets and reps, then click 
                        <strong style="color: #00f0ff;">Start Workout</strong> to turn on the camera.
                    </p>
                    <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
                        <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 10px; padding: 12px 18px; text-align: left; min-width: 140px;">
                            <div style="color: #00f0ff; font-weight: 700; font-size: 0.8rem;">STEP 1</div>
                            <div style="color: #e6edf3; font-weight: 600; font-size: 0.9rem;">Select Move</div>
                        </div>
                        <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 10px; padding: 12px 18px; text-align: left; min-width: 140px;">
                            <div style="color: #00f0ff; font-weight: 700; font-size: 0.8rem;">STEP 2</div>
                            <div style="color: #e6edf3; font-weight: 600; font-size: 0.9rem;">Set Targets</div>
                        </div>
                        <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 10px; padding: 12px 18px; text-align: left; min-width: 140px;">
                            <div style="color: #10b981; font-weight: 700; font-size: 0.8rem;">STEP 3</div>
                            <div style="color: #e6edf3; font-weight: 600; font-size: 0.9rem;">Start Workout</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            context = webrtc_streamer(
                key="exercise-analysis",
                mode=WebRtcMode.SENDRECV,
                video_processor_factory=VideoProcessorClass,
                rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
                media_stream_constraints={
                    "video": True,
                    "audio": False,
                },
                async_processing=True,
            )

            sync_metrics_update(context)

            if context.state.playing:
                time.sleep(0.25)
                st.rerun()

            inject_webrtc_styles()

            # Dynamic exercise-specific metrics
            exercise = st.session_state.get("exercise_type")
            st.divider()
            mcol1, mcol2, mcol3 = st.columns(3)

            if exercise == "Squats":
                with mcol1:
                    st.metric("Knee Angle", f"{st.session_state.get('knee_angle', 0)}°")
                with mcol2:
                    st.metric("Back Angle", f"{st.session_state.get('back_angle', 0)}°")
                with mcol3:
                    st.metric("Depth Status", st.session_state.get("depth_status", "Waiting"))
            elif exercise == "Push-ups":
                with mcol1:
                    st.metric("Elbow Angle", f"{st.session_state.get('elbow_angle', 0)}°")
                with mcol2:
                    st.metric("Body Alignment", st.session_state.get("body_alignment", "Waiting"))
                with mcol3:
                    st.metric("Hip Position", st.session_state.get("hip_status", "Waiting"))
            elif exercise == "Biceps Curls (Dumbbell)":
                with mcol1:
                    st.metric("Elbow Angle", f"{st.session_state.get('elbow_angle', 0)}°")
                with mcol2:
                    st.metric("Shoulder Stability", st.session_state.get("shoulder_status", "Waiting"))
                with mcol3:
                    st.metric("Swing Status", st.session_state.get("swing_status", "Waiting"))
            elif exercise == "Shoulder Press":
                with mcol1:
                    st.metric("Elbow Angle", f"{st.session_state.get('elbow_angle', 0)}°")
                with mcol2:
                    st.metric("Arm Extension", st.session_state.get("extension_status", "Waiting"))
                with mcol3:
                    st.metric("Back Arch", st.session_state.get("back_arch_status", "Waiting"))
            elif exercise == "Lunges":
                with mcol1:
                    st.metric("Front Knee Angle", f"{st.session_state.get('front_knee_angle', 0)}°")
                with mcol2:
                    st.metric("Torso Angle", f"{st.session_state.get('torso_angle', 0)}°")
                with mcol3:
                    st.metric("Balance Status", st.session_state.get("balance_status", "Waiting"))


if __name__ == "__main__":
    main()