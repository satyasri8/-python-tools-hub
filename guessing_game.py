import streamlit as st
import random

def guessing_game_app():
    st.header("🎯 Number Guessing Game")

    # Select difficulty
    difficulty = st.selectbox(
        "Choose Difficulty",
        ("Easy", "Medium", "Hard")
    )

    max_attempts = {
        "Easy": 10,
        "Medium": 7,
        "Hard": 5
    }[difficulty]

    # Initialize session state
    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.wrong_attempts = 0
        st.session_state.game_over = False
        st.session_state.max_attempts = max_attempts

    # Reset if difficulty changes
    if st.session_state.max_attempts != max_attempts:
        st.session_state.number = random.randint(1, 100)
        st.session_state.wrong_attempts = 0
        st.session_state.game_over = False
        st.session_state.max_attempts = max_attempts

    attempts_left = max_attempts - st.session_state.wrong_attempts
    st.write(f"Wrong attempts left: **{attempts_left}**")

    guess = st.slider(
        "Guess a number",
        1,
        100,
        disabled=st.session_state.game_over
    )

    if st.button("Submit Guess", disabled=st.session_state.game_over):
        if guess < st.session_state.number:
            st.session_state.wrong_attempts += 1
            st.warning("📉 Too low!")

        elif guess > st.session_state.number:
            st.session_state.wrong_attempts += 1
            st.warning("📈 Too high!")

        else:
            st.success("🎉 Correct! You guessed the number!")
            st.session_state.game_over = True

        if st.session_state.wrong_attempts >= max_attempts and not st.session_state.game_over:
            st.error(f"❌ Game Over! The correct number was {st.session_state.number}")
            st.session_state.game_over = True

    if st.session_state.game_over:
        if st.button("Restart Game 🔄"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.wrong_attempts = 0
            st.session_state.game_over = False
            st.info("Game reset. Try again!")
