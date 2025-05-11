import random
import streamlit as st

def get_random_word():
    words = ['python', 'streamlit', 'developer', 'hangman', 'challenge', 'programming']
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

st.title("Hangman Game")

if 'word' not in st.session_state:
    st.session_state.word = get_random_word()
    st.session_state.guessed_letters = set()
    st.session_state.attempts = 6

guessed_letters = st.session_state.guessed_letters
word = st.session_state.word
attempts = st.session_state.attempts

st.write(f"Attempts remaining: {attempts}")
st.write("Word: " + display_word(word, guessed_letters))

guess = st.text_input("Enter a letter:", max_chars=1).lower()

if st.button("Guess") and guess:
    if guess in guessed_letters:
        st.warning("You've already guessed this letter.")
    elif guess in word:
        guessed_letters.add(guess)
        st.success("Correct Guess!")
    else:
        guessed_letters.add(guess)
        st.session_state.attempts -= 1
        st.error("Wrong Guess!")

    if set(word).issubset(guessed_letters):
        st.balloons()
        st.success(f"Congratulations! You guessed the word: {word}")
        st.session_state.word = get_random_word()
        st.session_state.guessed_letters = set()
        st.session_state.attempts = 6
    elif st.session_state.attempts == 0:
        st.error(f"Game Over! The word was: {word}")
        st.session_state.word = get_random_word()
        st.session_state.guessed_letters = set()
        st.session_state.attempts = 6
