import random
import streamlit as st

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

st.title("Rock, Paper, Scissors Game")

choices = ["rock", "paper", "scissors"]
user_choice = st.selectbox("Choose Rock, Paper, or Scissors", choices)

if st.button("Play"):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    st.write(f"You chose: {user_choice}")
    st.write(f"Computer chose: {computer_choice}")
    st.write(f"Result: {result}")
