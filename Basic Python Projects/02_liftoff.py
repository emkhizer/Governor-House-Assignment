import streamlit as st
import time

def countdown():
    for i in range(5, 0, -1):
        st.write(i)
        time.sleep(1)
    st.write("Liftoff!")

st.title("Liftoff Countdown")
st.write("Click the button to start the countdown.")

if st.button("Start Countdown"):
    countdown()