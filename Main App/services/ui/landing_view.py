import streamlit as st


def render_landing_view():
    st.markdown(
        """
        <style>
        .hero-banner-box {
            background: radial-gradient(circle at 50% 0%, #17253d 0%, #0c121e 70%);
            border: 1px solid rgba(0, 240, 255, 0.25);
            border-radius: 16px;
            padding: 40px 28px;
            text-align: center;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4), 0 0 25px rgba(0, 240, 255, 0.08);
            margin-bottom: 30px;
        }
        .hero-tag-badge {
            display: inline-block;
            background: rgba(0, 240, 255, 0.1);
            color: #00f0ff;
            border: 1px solid rgba(0, 240, 255, 0.3);
            border-radius: 20px;
            padding: 5px 16px;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.06em;
            margin-bottom: 16px;
        }
        .hero-headline {
            color: #ffffff;
            font-size: 2.2rem;
            font-weight: 800;
            line-height: 1.15;
            margin: 0 0 14px 0;
            letter-spacing: -0.02em;
        }
        .hero-headline span {
            background: linear-gradient(135deg, #ffffff 40%, #00f0ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-desc {
            color: #94a3b8;
            font-size: 1.05rem;
            max-width: 620px;
            margin: 0 auto 10px auto;
            line-height: 1.5;
        }
        .stat-strip-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            background: #111827;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            margin: 28px 0;
            overflow: hidden;
        }
        .stat-strip-col {
            padding: 16px 12px;
            text-align: center;
            border-right: 1px solid rgba(255, 255, 255, 0.06);
        }
        .stat-strip-col:last-child {
            border-right: none;
        }
        .stat-strip-val {
            font-size: 1.55rem;
            font-weight: 800;
            color: #fff;
            line-height: 1.1;
        }
        .stat-strip-val span {
            color: #00f0ff;
        }
        .stat-strip-label {
            font-size: 0.75rem;
            color: #64748b;
            text-transform: uppercase;
            font-weight: 600;
            letter-spacing: 0.05em;
            margin-top: 4px;
        }
        .bio-card {
            background: #111827;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 22px;
            margin-bottom: 16px;
            transition: all 0.2s ease;
        }
        .bio-card:hover {
            border-color: rgba(0, 240, 255, 0.35);
            background: #162032;
        }
        .bio-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
        }
        .bio-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: #fff;
        }
        .bio-chip {
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.4);
            color: #10b981;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 12px;
            font-family: monospace;
        }
        .bio-desc {
            font-size: 0.9rem;
            color: #94a3b8;
            margin-bottom: 14px;
            line-height: 1.45;
        }
        .bio-list {
            margin: 0 0 12px 18px;
            padding: 0;
            font-size: 0.85rem;
            color: #cbd5e1;
            line-height: 1.6;
        }
        .hud-sim-container {
            background: #090e18;
            border: 1px solid rgba(0, 240, 255, 0.3);
            border-radius: 14px;
            padding: 24px;
            margin: 28px 0;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
        }
        .hud-tag {
            font-size: 0.75rem;
            font-family: monospace;
            font-weight: bold;
            color: #00f0ff;
            background: rgba(0, 240, 255, 0.12);
            padding: 3px 10px;
            border-radius: 6px;
            display: inline-block;
            margin-bottom: 14px;
        }
        .creator-box {
            background: #111827;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            padding: 28px;
            text-align: center;
            margin-top: 36px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Hero Banner
    st.markdown(
        """
        <div class="hero-banner-box">
            <span class="hero-tag-badge">⚡ VISION BIOMECHANICS & LLM COACHING</span>
            <h1 class="hero-headline">
                Train with Perfect Form.<br>
                <span>Real-Time AI Workout Coaching.</span>
            </h1>
            <p class="hero-desc">
                High-precision 33-point skeletal pose tracking, automated rep counting, 
                and live audio guidance streamed directly through your camera feed.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Primary Action CTA Button
    col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
    with col_c2:
        if st.button("🚀 Launch Workout Studio & Camera", type="primary", use_container_width=True, key="hero_cta_btn"):
            st.session_state.app_nav = "⚡ Workout Studio"
            st.rerun()

    # Telemetry Strip
    st.markdown(
        """
        <div class="stat-strip-row">
            <div class="stat-strip-col">
                <div class="stat-strip-val">&lt;100<span>ms</span></div>
                <div class="stat-strip-label">Frame Latency</div>
            </div>
            <div class="stat-strip-col">
                <div class="stat-strip-val">5<span> Moves</span></div>
                <div class="stat-strip-label">Form Detectors</div>
            </div>
            <div class="stat-strip-col">
                <div class="stat-strip-val">33<span> Pts</span></div>
                <div class="stat-strip-label">MediaPipe Landmarks</div>
            </div>
            <div class="stat-strip-col">
                <div class="stat-strip-val">100<span>%</span></div>
                <div class="stat-strip-label">On-Device Privacy</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Section 1: Biomechanics Guide
    st.markdown("### 🧬 Exercise Form Detection & Target Biomechanics")
    st.caption("Automated joint angle math tracks limb trajectories and counts valid repetitions.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="bio-card">
                <div class="bio-header">
                    <span class="bio-title">🏋️‍♂️ Squats</span>
                    <span class="bio-chip">DEPTH &lt; 90°</span>
                </div>
                <p class="bio-desc">
                    Calculates hip-to-knee-to-ankle angles to ensure thighs break parallel without rounding the spine.
                </p>
                <ul class="bio-list">
                    <li>Knee flexion angle tracking (&lt; 90° for full depth)</li>
                    <li>Torso angle check to prevent forward collapse</li>
                    <li>Automatic bottom-out repetition counter</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="bio-card">
                <div class="bio-header">
                    <span class="bio-title">💪 Push-ups</span>
                    <span class="bio-chip">DEPTH 90°</span>
                </div>
                <p class="bio-desc">
                    Checks 180° body plank alignment from shoulder to heel while measuring chest-to-elbow flexion.
                </p>
                <ul class="bio-list">
                    <li>Elbow depth angle verification</li>
                    <li>Straight spine & hip alignment tracking</li>
                    <li>Hip sag and pike fault warnings</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="bio-card">
                <div class="bio-header">
                    <span class="bio-title">🧘 Lunges</span>
                    <span class="bio-chip">KNEE 90°</span>
                </div>
                <p class="bio-desc">
                    Monitors unilateral leg loading, knee-over-ankle positioning, and dynamic balance stability.
                </p>
                <ul class="bio-list">
                    <li>Front knee 90° angle measurement</li>
                    <li>Torso upright stability index</li>
                    <li>Independent single-leg repetition counter</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="bio-card">
                <div class="bio-header">
                    <span class="bio-title">🦾 Biceps Curls</span>
                    <span class="bio-chip">FLEXION &lt; 45°</span>
                </div>
                <p class="bio-desc">
                    Tracks elbow hinge motion and torso stability to eliminate momentum swinging for strict isolation.
                </p>
                <ul class="bio-list">
                    <li>Elbow isolation & body pin check</li>
                    <li>Torso swing & momentum detection</li>
                    <li>Full extension reset threshold (&gt; 160°)</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="bio-card">
                <div class="bio-header">
                    <span class="bio-title">🏋️ Shoulder Press</span>
                    <span class="bio-chip">LOCKOUT &gt; 165°</span>
                </div>
                <p class="bio-desc">
                    Evaluates vertical arm drive symmetry and complete overhead extension without lumbar arching.
                </p>
                <ul class="bio-list">
                    <li>Left vs. right arm drive symmetry</li>
                    <li>Full overhead vertical lockout</li>
                    <li>Lower back hyperextension alert</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Quick CTA in right column
        st.info("💡 **Ready to test?** Click **Launch Workout Studio** in the sidebar to activate your camera and begin training.")

    # Section 2: Real-Time HUD Preview
    st.markdown("### 🖥️ Live Telemetry & Camera HUD")
    st.markdown(
        """
        <div class="hud-sim-container">
            <span class="hud-tag">● WEBRTC VISION HUD PREVIEW</span>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; align-items: center;">
                <div style="background: #141c2c; border: 1px dashed rgba(0, 240, 255, 0.3); border-radius: 10px; padding: 24px; text-align: center;">
                    <div style="font-size: 56px; margin-bottom: 10px;">🧍‍♂️</div>
                    <div style="font-family: monospace; font-size: 11px; color: #00f0ff; font-weight: bold;">
                        ✓ 33/33 SKELETAL LANDMARKS LOCKED
                    </div>
                    <div style="font-size: 12px; color: #94a3b8; margin-top: 6px;">
                        Knee Angle: 86° · Hip Angle: 78° · Back Angle: 84°
                    </div>
                </div>
                <div>
                    <div style="background: #111827; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 12px 16px; margin-bottom: 12px;">
                        <div style="font-size: 10px; color: #64748b; font-family: monospace; text-transform: uppercase;">EXERCISE & SET</div>
                        <div style="font-size: 16px; font-weight: bold; color: #fff;">Squats — Set 2 / 3</div>
                    </div>
                    <div style="background: #111827; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 12px 16px; margin-bottom: 12px;">
                        <div style="font-size: 10px; color: #64748b; font-family: monospace; text-transform: uppercase;">REPETITIONS COUNTED</div>
                        <div style="font-size: 16px; font-weight: bold; color: #00f0ff;">8 of 12 Reps Completed</div>
                    </div>
                    <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 12px 14px;">
                        <div style="font-size: 11px; font-family: monospace; font-weight: bold; color: #10b981;">🤖 AI VOICE COACH</div>
                        <div style="font-size: 12px; color: #e2e8f0; margin-top: 2px;">
                            "Great depth on rep 8! Keep your chest upright and drive through your heels."
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Section 3: Author & Socials
    st.markdown(
        """
        <div class="creator-box">
            <h4 style="color: #fff; margin: 0 0 6px 0;">Built by Aditya Saxena</h4>
            <p style="color: #94a3b8; font-size: 0.9rem; margin-bottom: 16px;">
                AI & Machine Learning Engineer specializing in computer vision, deep learning, and generative AI.
            </p>
            <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
                <a href="https://www.linkedin.com/in/aditya-saxena-976511281" target="_blank" style="background: #1e293b; color: #fff; padding: 8px 18px; border-radius: 8px; font-size: 0.85rem; font-weight: 600; text-decoration: none; border: 1px solid rgba(255,255,255,0.1);">
                    LinkedIn
                </a>
                <a href="https://github.com/aditya-2204" target="_blank" style="background: #1e293b; color: #fff; padding: 8px 18px; border-radius: 8px; font-size: 0.85rem; font-weight: 600; text-decoration: none; border: 1px solid rgba(255,255,255,0.1);">
                    GitHub
                </a>
                <a href="mailto:aditya808166@gmail.com" style="background: #1e293b; color: #fff; padding: 8px 18px; border-radius: 8px; font-size: 0.85rem; font-weight: 600; text-decoration: none; border: 1px solid rgba(255,255,255,0.1);">
                    Email
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
