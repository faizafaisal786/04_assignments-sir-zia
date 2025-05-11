import time
import streamlit as st

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        st.write(timer)
        time.sleep(1)
        seconds -= 1
    st.write("Time's up! ⏰")

st.title("Countdown Timer ⏳")

seconds = st.number_input("Enter time in seconds:", min_value=1, step=1)

if st.button("Start Timer"):
    countdown_timer(int(seconds))
