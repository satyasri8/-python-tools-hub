if tool == "Home":
    # Hero Section
    st.markdown(
        """
        <h1 style='text-align: center;'>🧰 Python Tools Dashboard</h1>
        <p style='text-align: center; font-size:18px;'>
        A clean, interactive collection of Python mini‑tools built with Streamlit
        </p>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.divider()

    # Metrics Section (Very Attractive)
    col1, col2, col3 = st.columns(3)
    col1.metric("🛠️ Tools", "6")
    col2.metric("⚡ Built With", "Python + Streamlit")
    col3.metric("🎯 Focus", "Learning & Productivity")

    st.divider()
    st.subheader("✨ Available Tools")

    # Tool Cards - Row 1
    c1, c2, c3 = st.columns(3)

    with c1:
        st.container(border=True)
        st.markdown("### 🧮 Calculator")
        st.caption("Perform basic arithmetic operations quickly")

    with c2:
        st.container(border=True)
        st.markdown("### 🎯 Guessing Game")
        st.caption("Fun number guessing game with difficulty levels")

    with c3:
        st.container(border=True)
        st.markdown("### 📝 Word Counter")
        st.caption("Analyze text and download reports")

    # Tool Cards - Row 2
    c4, c5, c6 = st.columns(3)

    with c4:
        st.container(border=True)
        st.markdown("### 🔐 Password Checker")
        st.caption("Check password strength securely")

    with c5:
        st.container(border=True)
        st.markdown("### 🔄 Unit Converter")
        st.caption("Convert common units instantly")

    with c6:
        st.container(border=True)
        st.markdown("### 🔁 Palindrome Checker")
        st.caption("Validate strings and patterns")

    st.divider()

    # Footer / CTA
    st.markdown(
        """
        <p style='text-align:center; font-size:14px;'>
        👈 Select a tool from the sidebar to get started<br>
        Built with ❤️ using Python & Streamlit
        </p>
        """,
        unsafe_allow_html=True
    )
