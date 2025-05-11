import streamlit as st
import random

# Initialize session state for storing the random number and attempts
if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.title("🎯 Guess the Number Game")
st.subheader("Try to guess the number between 1 and 100!")

# Input from user
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Check the guess
if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1
    
    if guess < st.session_state.target_number:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.target_number:
        st.warning("Too high! Try again.")
    else:
        st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts!")
        st.session_state.game_over = True

# Reset Game
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
