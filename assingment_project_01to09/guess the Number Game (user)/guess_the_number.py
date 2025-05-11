import streamlit as st

# Initialize session state for the game
if 'low' not in st.session_state:
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    st.session_state.game_over = False
    st.session_state.attempts = 0

st.title("🤖 Computer Guesses Your Number!")
st.subheader("Think of a number between 1 and 100, and let the computer guess it!")

st.write(f"Is your number {st.session_state.guess}?")

col1, col2, col3 = st.columns(3)

if col1.button("Too Low"):
    st.session_state.low = st.session_state.guess + 1
    st.session_state.attempts += 1
    
if col2.button("Too High"):
    st.session_state.high = st.session_state.guess - 1
    st.session_state.attempts += 1
    
if col3.button("Correct!"):
    st.success(f"🎉 The computer guessed your number in {st.session_state.attempts + 1} attempts!")
    st.session_state.game_over = True

if not st.session_state.game_over:
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    st.rerun()

if st.session_state.game_over and st.button("Play Again"):
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess = 50
    st.session_state.game_over = False
    st.session_state.attempts = 0
    st.rerun()
