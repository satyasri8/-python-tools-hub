import streamlit as st
import re

def password_checker_app():
    st.header("🔐 Password Strength Checker")

    password = st.text_input("Enter your password", type="password")

    if st.button("Check Strength"):
        if password == "":
            st.warning("Please enter a password")
            return

        length = len(password) >= 8
        upper = re.search(r"[A-Z]", password)
        lower = re.search(r"[a-z]", password)
        digit = re.search(r"\d", password)
        special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

        score = sum([length, bool(upper), bool(lower), bool(digit), bool(special)])

        if score <= 2:
            st.error("❌ Weak Password")
        elif score <= 4:
            st.warning("⚠️ Medium Password")
        else:
            st.success("✅ Strong Password")

        st.write("### Criteria")
        st.write("✔ Minimum 8 characters")
        st.write("✔ Uppercase letter")
        st.write("✔ Lowercase letter")
        st.write("✔ Number")
        st.write("✔ Special character")
