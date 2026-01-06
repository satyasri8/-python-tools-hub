import streamlit as st
from calculator import calculator_app
from guessing_game import guessing_game_app
from word_counter import word_counter_app

st.set_page_config(
    page_title="Python Basic Tools",
    page_icon="🧰",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #f8f9fa;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    text-align: center;
}
.card:hover {
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🧰 Python Basic Tools")
st.write("One app. Multiple tools. Choose what you need 👇")

# ---------- SIDEBAR ----------
st.sidebar.title("🔧 Select Tool")
tool = st.sidebar.radio(
    "",
    ("Home", "Calculator", "Number Guessing Game", "Word Counter")
)

# ---------- HOME ----------
if tool == "Home":
    st.subheader("✨ Available Tools")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h2>🧮 Calculator</h2>
            <p>Perform basic arithmetic operations quickly.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h2>🎯 Guessing Game</h2>
            <p>Interactive number guessing game with feedback.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h2>📝 Word Counter</h2>
            <p>Analyze text for words, characters & sentences.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("👈 Select a tool from the sidebar to begin")

elif tool == "Calculator":
    calculator_app()

elif tool == "Number Guessing Game":
    guessing_game_app()

elif tool == "Word Counter":
    word_counter_app()
