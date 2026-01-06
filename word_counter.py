import streamlit as st

def word_counter_app():
    st.header("📝 Word Counter")

    text = st.text_area("Enter your text below", height=200)

    if st.button("Analyze Text 🔍"):
        if text.strip() == "":
            st.warning("Please enter some text")
        else:
            words = len(text.split())
            characters = len(text)
            sentences = text.count(".") + text.count("!") + text.count("?")

            col1, col2, col3 = st.columns(3)
            col1.metric("Words", words)
            col2.metric("Characters", characters)
            col3.metric("Sentences", sentences)

            # ---------- REPORT ----------
            report = f"""
WORD COUNTER REPORT
-------------------
Words      : {words}
Characters : {characters}
Sentences  : {sentences}
"""

            st.download_button(
                label="📥 Download Report",
                data=report,
                file_name="word_counter_report.txt",
                mime="text/plain"
            )
