import streamlit as st
from calculator import calculator_app
from guessing_game import guessing_game_app
from word_counter import word_counter_app
from password_checker import password_checker_app
from unit_converter import unit_converter_app
from palindrome_checker import palindrome_checker_app

st.set_page_config(page_title="Python Tools Dashboard", page_icon="🧰", layout="wide")

st.title("🧰 Python Tools Dashboard")


tool = st.sidebar.radio(
    "Select Tool",
    (
        "Home",
        "Calculator",
        "Number Guessing Game",
        "Word Counter",
        "Password Strength Checker",
        "Unit Converter",
        "Palindrome Checker"
    )
)

if tool == "Home":
    st.subheader("✨ Available Tools")
    st.write("""
    🧮 Calculator  
    🎯 Number Guessing Game  
    📝 Word Counter  
    🔐 Password Strength Checker  
    🔄 Unit Converter  
    🔁 Palindrome Checker  
    """)

elif tool == "Calculator":
    calculator_app()

elif tool == "Number Guessing Game":
    guessing_game_app()

elif tool == "Word Counter":
    word_counter_app()

elif tool == "Password Strength Checker":
    password_checker_app()

elif tool == "Unit Converter":
    unit_converter_app()

elif tool == "Palindrome Checker":
    palindrome_checker_app()
