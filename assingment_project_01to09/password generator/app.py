import streamlit as st
import re
import random

# Constants
COMMON_PASSWORDS = {"password", "123456", "qwerty", "abc123", "password123", "admin", "letmein"}
SPECIAL_CHARACTERS = "!@#$%^&*"

# Initialize used passwords in session state
if "used_passwords" not in st.session_state:
    st.session_state.used_passwords = set()

if "applied_password" not in st.session_state:
    st.session_state.applied_password = None

# Function to check password strength
def check_password_strength(password):
    if password in st.session_state.used_passwords:
        return "❌ This password has already been used. Choose a new one.", []

    score = 0
    suggestions = []

    if password.lower() in COMMON_PASSWORDS:
        return "❌ Weak Password - Common password detected! Choose a unique password.", suggestions

    if len(password) >= 14:
        score += 2
    elif len(password) >= 10:
        score += 1
    else:
        suggestions.append("Increase password length to at least 14 characters.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")

    if re.search(rf"[{SPECIAL_CHARACTERS}]", password):
        score += 1
    else:
        suggestions.append(f"Include at least one special character ({SPECIAL_CHARACTERS}).")

    if score >= 4:
        return "✅ Strong Password! Your password is secure.", []
    elif score == 3:
        return "⚠️ Moderate Password - Consider improving it with the suggestions below.", suggestions
    else:
        return "❌ Weak Password - Improve it using the suggestions below.", suggestions

# Function to generate strong password
def generate_strong_password(length=16):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" + SPECIAL_CHARACTERS
    password = "".join(random.sample(characters, length))
    return password

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")

# Sidebar Design
with st.sidebar:
    st.markdown(
        """
        <div style="background-color:#1e1e1e; color: #ffffff; padding:15px; border-radius:10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);">
            <h3 style="color:#4A90E2; text-align:center;">🔒 Password Strength Tips</h3>
            <p style="font-size:14px;">
                👉 Use a mix of uppercase and lowercase letters.<br>
                👉 Include numbers and special characters.<br>
                👉 Make it at least 14 characters long.<br>
                👉 Avoid common words and phrases.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")
   

# Header
st.markdown("""
    <h2 style='text-align: center; color: #4A90E2;'>🔐 Password Strength Meter</h2>
    <p style='text-align: center;'>Check your password strength, get improvement suggestions, and apply a secure password.</p>
""", unsafe_allow_html=True)

# About Section
with st.expander("ℹ️ About This App"):
    st.markdown("""
        This app helps you check the strength of your passwords and gives recommendations for making them more secure.

        - **Enter a password** to check its strength.
        - **View suggestions** to improve weak or moderate passwords.
        - **Generate a strong password** if you need one.
        - **Apply a password** to save and prevent reuse in this session.

        🔒 Stay secure with strong passwords!
    """)

# Password Input
password = st.text_input("Enter Your Password", type="password", help="Enter your password and press Enter to check its strength.")

if password:
    strength_message, suggestions = check_password_strength(password)

    color = "#2ed573" if "✅" in strength_message else "#ffa502" if "⚠️" in strength_message else "#ff4757"

    st.markdown(f"<h4 style='color: {color};'>{strength_message}</h4>", unsafe_allow_html=True)

    if suggestions:
        st.markdown("<h5 style='color: #ff6b81;'>Suggestions to Improve:</h5>", unsafe_allow_html=True)
        for tip in suggestions:
            st.markdown(f"- ✅ {tip}")

    # Apply Password Option
    if "✅ Strong Password!" in strength_message:
        if st.button("Apply This Password ✅"):
            st.session_state.used_passwords.add(password)
            st.session_state.applied_password = password
            st.success("🔒 Password has been successfully applied and saved!")
    elif "❌" in strength_message:
        st.warning("⚠️ You need a strong password before applying!")

# Password Generator
st.markdown("---")
st.markdown("<h4 style='color: #2ed573;'>Need a Strong Password?</h4>", unsafe_allow_html=True)

if st.button("Generate Strong Password 🔄"):
    strong_password = generate_strong_password()
    st.code(strong_password, language="bash")

# Show Applied Password (If Any)
if st.session_state.applied_password:
    st.success(f"🔐 Currently applied password: `{st.session_state.applied_password}`")