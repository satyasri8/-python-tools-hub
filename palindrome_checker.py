import streamlit as st

def palindrome_checker_app():
    st.header("🔁 Palindrome Checker")

    text = st.text_input("Enter a word or sentence")

    if st.button("Check"):
        cleaned = "".join(text.lower().split())

        if cleaned == "":
            st.warning("Please enter text")
        elif cleaned == cleaned[::-1]:
            st.success("✅ It is a Palindrome")
        else:
            st.error("❌ Not a Palindrome")
