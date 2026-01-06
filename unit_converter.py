import streamlit as st

def unit_converter_app():
    st.header("🔄 Unit Converter")

    option = st.selectbox(
        "Choose conversion type",
        ("Kilometers to Meters", "Celsius to Fahrenheit", "Kilograms to Grams")
    )

    value = st.number_input("Enter value")

    if st.button("Convert"):
        if option == "Kilometers to Meters":
            st.success(f"{value} km = {value * 1000} meters")

        elif option == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
            st.success(f"{value}°C = {result}°F")

        elif option == "Kilograms to Grams":
            st.success(f"{value} kg = {value * 1000} grams")
