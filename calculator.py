import streamlit as st

def calculator_app():
    st.header("🧮 Simple Calculator")

    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number")
    with col2:
        num2 = st.number_input("Enter second number")

    operation = st.selectbox(
        "Choose operation",
        ["Add ➕", "Subtract ➖", "Multiply ✖️", "Divide ➗"]
    )

    if st.button("Calculate"):
        if operation.startswith("Add"):
            st.success(f"Result: {num1 + num2}")
        elif operation.startswith("Subtract"):
            st.success(f"Result: {num1 - num2}")
        elif operation.startswith("Multiply"):
            st.success(f"Result: {num1 * num2}")
        elif operation.startswith("Divide"):
            if num2 == 0:
                st.error("Cannot divide by zero")
            else:
                st.success(f"Result: {num1 / num2}")
