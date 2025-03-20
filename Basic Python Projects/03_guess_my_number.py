import streamlit as st
import random

# Initialize session state variables
if 'game_active' not in st.session_state:
    st.session_state.game_active = False
if 'target_number' not in st.session_state:
    st.session_state.target_number = None
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

def new_game():
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_active = True

st.title("🎮 Guess My Number Game")
st.write("Can you guess the secret number between 1 and 100? 🔢")

if not st.session_state.game_active:
    st.write("Click the button below to start a new game!")
    if st.button("🎯 Start New Game"):
        new_game()
else:
    st.write(f"Attempts: {st.session_state.attempts} 💡")
    user_guess = st.number_input("Enter your guess:", 
                                min_value=1, 
                                max_value=100,
                                key="guess_input")
    
    if st.button("🚀 Submit Guess"):
        st.session_state.attempts += 1
        if user_guess < st.session_state.target_number:
            st.error("📉 Too low! Try a higher number!")
        elif user_guess > st.session_state.target_number:
            st.error("📈 Too high! Try a lower number!")
        else:
            st.success(f"""
            🎉 Congratulations! You won!
            The secret number was {st.session_state.target_number}
            Guessed in {st.session_state.attempts} attempts!
            """)
            st.balloons()
            st.session_state.game_active = False

    if st.button("😞 Give Up"):
        st.warning(f"""
        The secret number was {st.session_state.target_number}
        Better luck next time! 🤞
        """)
        st.session_state.game_active = False