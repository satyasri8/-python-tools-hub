import streamlit as st
import random

def guessing_game_app():
    st.header("🎯 Number Guessing Game")

    # Initialize session state
    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False

    # Show attempts left
    attempts_left = 5 - st.session_state.attempts
    st.write(f"Attempts left: **{attempts_left}**")

    # Guess input (disabled if game over)
    guess = st.slider(
        "Guess a number",
        1,
        100,
        disabled=st.session_state.game_over
    )

    # Submit guess
    if st.button("Submit Guess", disabled=st.session_state.game_over):
        st.session_state.attempts += 1

        if guess < st.session_state.number:
            st.warning("📉 Too low!")
        elif guess > st.session_state.number:
            st.warning("📈 Too high!")
        else:
            st.success(f"🎉 Correct! Attempts used: {st.session_state.attempts}")
            st.session_state.game_over = True

        # Check if attempts exceeded
        if st.session_state.attempts >= 5 and not st.session_state.game_over:
            st.error(f"❌ Game Over! The correct number was {st.session_state.number}")
            st.session_state.game_over = True

    # Restart button (enabled only when game is over)
    if st.session_state.game_over:
        if st.button("Restart Game 🔄"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.game_over = False
            st.info("Game reset. Try again!")
