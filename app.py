import streamlit as st
import random

# --------------------------------------------------
# PAGE CONFIG (must be FIRST Streamlit command)
# --------------------------------------------------
st.set_page_config(
    page_title="Python Tools Hub",
    page_icon="🧰",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS (UI / UX Upgrade)
# --------------------------------------------------
st.markdown("""
<style>
.main-title {
    font-size: 48px;
    font-weight: 800;
    text-align: center;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #6c757d;
}
.card {
    padding: 25px;
    border-radius: 15px;
    background: #f8f9fa;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    height: 100%;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Choose a tool",
    ["🏠 Home", "🧮 Calculator", "🎯 Guessing Game", "📝 Word Counter"]
)

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
if page == "🏠 Home":
    st.markdown('<div class="main-title">🧰 Python Basic Tools Hub</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Simple • Interactive • Beginner Friendly</div>', unsafe_allow_html=True)
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>🧮 Calculator</h3>
        <p>Perform basic arithmetic operations with error handling.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🎯 Guessing Game</h3>
        <p>Guess the number with a maximum of 5 wrong attempts.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>📝 Word Counter</h3>
        <p>Count words, characters, and sentences from text input.</p>
        </div>
        """, unsafe_allow_html=True)

    st.success("👈 Select a tool from the sidebar to get started!")

# --------------------------------------------------
# CALCULATOR
# --------------------------------------------------
elif page == "🧮 Calculator":
    st.header("🧮 Simple Calculator")

    col1, col2 = st.columns(2)
    num1 = col1.number_input("Enter first number")
    num2 = col2.number_input("Enter second number")

    operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        try:
            if operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            elif operation == "Multiply":
                result = num1 * num2
            elif operation == "Divide":
                result = num1 / num2

            st.success(f"✅ Result: {result}")

        except ZeroDivisionError:
            st.error("❌ Cannot divide by zero")

# --------------------------------------------------
# GUESSING GAME (5 WRONG ATTEMPTS ONLY)
# --------------------------------------------------
elif page == "🎯 Guessing Game":
    st.header("🎯 Number Guessing Game")

    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False

    guess = st.slider("Guess a number between 1 and 100", 1, 100)

    if st.button("Submit Guess") and not st.session_state.game_over:
        if guess != st.session_state.number:
            st.session_state.attempts += 1

            if st.session_state.attempts >= 5:
                st.error(f"❌ Game Over! The number was {st.session_state.number}")
                st.session_state.game_over = True
            elif guess < st.session_state.number:
                st.warning("📉 Too low!")
            else:
                st.warning("📈 Too high!")
        else:
            st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts + 1} attempts")
            st.session_state.game_over = True

    st.info(f"Attempts used: {st.session_state.attempts} / 5")

    if st.button("Restart Game 🔄"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.success("🔁 Game restarted!")

# --------------------------------------------------
# WORD COUNTER
# --------------------------------------------------
elif page == "📝 Word Counter":
    st.header("📝 Word Counter")

    text = st.text_area("Enter text here")

    if st.button("Analyze Text"):
        if text.strip() == "":
            st.warning("⚠️ Please enter some text")
        else:
            words = text.split()
            characters = len(text)
            sentences = text.count(".") + text.count("!") + text.count("?")

            st.success("✅ Analysis Completed")
            st.write(f"**Total Words:** {len(words)}")
            st.write(f"**Total Characters:** {characters}")
            st.write(f"**Total Sentences:** {sentences}")
