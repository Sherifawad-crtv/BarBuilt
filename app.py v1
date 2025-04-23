
import streamlit as st
import random

st.set_page_config(page_title="Calisthenics Generator", layout="centered")

st.markdown("<h1 style='text-align: center;'>BarBuilt: Calisthenics Workout Generator</h1>", unsafe_allow_html=True)
st.markdown("Train anywhere. No excuses.")

goal = st.selectbox("Choose your goal", ["Fat Loss", "Muscle Gain", "Strength", "Mobility", "Skill Mastery"])
level = st.selectbox("Your level", ["Beginner", "Intermediate", "Advanced"])
time = st.selectbox("Workout time", ["15–30 min", "30–45 min", "45+ min"])

warmups = ["Pike Walks x10", "Bear Shoulder Taps 30s", "Jumping Jacks 1 min"]
push = ["Push-ups 3x15", "Incline Push-ups 3x10", "Dips 3x8"]
pull = ["Inverted Rows 3x10", "Pull-ups 3x5", "Band Face Pulls 3x12"]
legs = ["Bodyweight Squats 3x20", "Lunges 3x10/leg", "Wall Sit 3x30s"]
core = ["Plank 3x30s", "Deadbugs 3x10", "Leg Raises 3x12"]
skills = ["Wall Handstand Hold", "L-sit on Bars", "Tuck Planche Hold"]
cooldowns = ["Forward Fold", "Cobra Stretch", "Shoulder Stretch"]

if st.button("Generate My Workout"):
    st.subheader("Your Personalized Workout")
    st.markdown(f"**Warm-up:** {random.choice(warmups)}")
    st.markdown(f"**Push:** {random.choice(push)}")
    st.markdown(f"**Pull:** {random.choice(pull)}")
    st.markdown(f"**Legs:** {random.choice(legs)}")
    st.markdown(f"**Core:** {random.choice(core)}")
    st.markdown(f"**Skill:** {random.choice(skills)}")
    st.markdown(f"**Cool-down:** {random.choice(cooldowns)}")
