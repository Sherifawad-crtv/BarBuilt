import streamlit as st
import random

st.set_page_config(page_title="BarBuilt", layout="centered")

# Inject Urbanist font and custom styles
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Urbanist', sans-serif;
        background-color: #ffffff;
        color: #000000;
    }

    .stButton>button {
        background-color: #3533CD;
        color: white;
        border-radius: 6px;
        padding: 0.6rem 1.2rem;
        border: none;
        transition: all 0.3s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #2e2cb5;
        transform: scale(1.03);
    }

    .stSelectbox, .stTextInput, .stTextArea, .stDateInput {
        background-color: #f5f6f7;
        border-radius: 6px;
    }

    .questionnaire {
        padding: 1rem;
        border: 1px solid #eee;
        border-radius: 8px;
        background: #f9f9fc;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>BarBuilt</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Personalized Calisthenics Generator</p>", unsafe_allow_html=True)

st.markdown("### Letâs get to know you first")

with st.form("questionnaire"):
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", 16, 80)
            fitness_level = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
            goal = st.selectbox("Fitness Goal", ["Fat Loss", "Muscle Gain", "Strength", "Mobility", "Skill Mastery"])
        with col2:
            gender = st.radio("Gender", ["Male", "Female", "Other"])
            time_available = st.selectbox("Time Per Session", ["15â30 min", "30â45 min", "45+ min"])
            equipment = st.multiselect("Available Equipment", ["None", "Pull-up bar", "Rings", "Resistance bands"])

        focus = st.multiselect("Target Areas", ["Push", "Pull", "Legs", "Core", "Mobility"])
        injury = st.text_area("Do you have any injuries or limitations?", "")

        submitted = st.form_submit_button("Generate My Workout")

warmups = ["Pike Walks x10", "Bear Shoulder Taps 30s", "Jumping Jacks 1 min"]
push = ["Push-ups 3x15", "Incline Push-ups 3x10", "Dips 3x8"]
pull = ["Inverted Rows 3x10", "Pull-ups 3x5", "Band Face Pulls 3x12"]
legs = ["Bodyweight Squats 3x20", "Lunges 3x10/leg", "Wall Sit 3x30s"]
core = ["Plank 3x30s", "Deadbugs 3x10", "Leg Raises 3x12"]
skills = ["Wall Handstand Hold", "L-sit on Bars", "Tuck Planche Hold"]
cooldowns = ["Forward Fold", "Cobra Stretch", "Shoulder Stretch"]

if submitted:
    st.markdown("### Your Personalized Workout")
    st.success(f"**Warm-up:** {random.choice(warmups)}")
    st.info(f"**Push:** {random.choice(push)}")
    st.info(f"**Pull:** {random.choice(pull)}")
    st.info(f"**Legs:** {random.choice(legs)}")
    st.info(f"**Core:** {random.choice(core)}")
    st.warning(f"**Skill:** {random.choice(skills)}")
    st.success(f"**Cool-down:** {random.choice(cooldowns)}")
