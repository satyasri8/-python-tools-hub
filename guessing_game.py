import streamlit as st
import random

def guessing_game_app():
    st.header("🎯 Number Guessing Game")

    # Difficulty selection
    difficulty = st.selectbox(
        "Choose Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    max_attempts_map = {
        "Easy": 10,
        "Medium": 7,
        "Hard": 5
    }

    max_attempts = max_attempts_map[difficulty]

    # ---- SAFE SESSION STATE INITIALIZATION ----
    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 100)

    if "wrong_attempts" not in st.session_state:
        st.session_state.wrong_attempts = 0

    if "game_over" not in st.session_state:
        st.session_state.game_over = False

    if "difficulty" not in st.session_state:
        st.session_state.difficulty = difficulty

    # Reset game if difficulty changes
    if st.session_state.difficulty != difficulty:
        st.session_state.number = random.randint(1, 100)
        st.session_state.wrong_attempts = 0
        st.session_state.game_over = False
        st.session_state.difficulty = difficulty

    attempts_left = max_attempts - st.session_state.wrong_attempts
    st.write(f"❌ Wrong attempts left: **{attempts_left}**")

    guess = st.slider(
        "Guess a number between 1 and 100",
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
            st.error(f"❌ Game Over! The number was {st.session_state.number}")
            st.session_state.game_over = True

    if st.session_state.game_over:
        if st.button("Restart Game 🔄"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.wrong_attempts = 0
            st.session_state.game_over = False
            st.info("Game restarted. Try again!")
