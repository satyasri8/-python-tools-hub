# 🧰 Python Basic Tools – Streamlit App

A multi-tool web application built using **Python** and **Streamlit** that combines multiple basic Python projects into a single, interactive user interface.  
Users can choose tools based on their requirements through a clean and intuitive UI.

---

## 🚀 Features

### 🧮 Simple Calculator
- Perform basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Handles division-by-zero errors gracefully

---

### 🎯 Number Guessing Game
- Interactive number guessing game (range: 1–100)
- Instant feedback for each guess (Too High / Too Low)
- Tracks number of attempts
- Restart functionality using Streamlit session state

---

### 📝 Word Counter
- Analyze text entered by the user
- Counts:
  - Total words
  - Total characters
  - Total sentences
- Allows users to **download the analysis report** as a text file

---

### 🔐 Password Strength Checker
- Evaluates password strength based on:
  - Minimum length
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Displays password strength as:
  - Weak
  - Medium
  - Strong
- Encourages secure password practices

---

### 🔄 Unit Converter
- Converts commonly used units:
  - Kilometers → Meters
  - Celsius → Fahrenheit
  - Kilograms → Grams
- Simple and user-friendly input system
- Instant conversion results

---

### 🔁 Palindrome Checker
- Checks whether a word or sentence is a palindrome
- Ignores spaces and letter casing
- Demonstrates string manipulation concepts

---

## 🎨 UI / UX Highlights
- Sidebar-based navigation for easy tool selection
- Card-style layout on the Home page
- Icons and emojis for better readability
- Responsive layout using Streamlit columns
- Clean spacing and minimal design
- Download feature for enhanced user experience

---

## 🛠️ Technologies Used
- **Python**
- **Streamlit**
- Modular programming
- Session state management
- Basic UI/UX design principles

---

## 📂 Project Structure

python-basic-tools-streamlit/
│
├── app.py
├── calculator.py
├── guessing_game.py
├── word_counter.py
├── password_checker.py
├── unit_converter.py
├── palindrome_checker.py
├── requirements.txt
└── README.md


---

## ▶️ How to Run the Application

### 1️⃣ Install dependencies

pip install streamlit
