import streamlit as st
import random

def guessing_game_app():
    st.header("🎯 Number Guessing Game")

    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0

    guess = st.slider("Guess a number", 1, 100)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1

        if guess < st.session_state.number:
            st.warning("📉 Too low!")
        elif guess > st.session_state.number:
            st.warning("📈 Too high!")
        else:
            st.success(f"🎉 Correct! Attempts: {st.session_state.attempts}")

    if st.button("Restart Game 🔄"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.info("Game reset. Try again!")
