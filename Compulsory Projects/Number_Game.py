# guess_the_number_computer.py
# Streamlit aur random modules ko import karta hai 🐍📦
import streamlit as st
import random

def guess_the_number_computer():
    # 1 se 100 ke beech ek random number generate karta hai 🎲
    number = random.randint(1, 100)
    # Attempts counter ko 0 se initialize karta hai 🚦
    attempts = 0
    
    # User se guess lene ke liye number input field 📥
    guess = st.number_input(
        "Guess a number between 1 and 100 🔢:",
        min_value=1,
        max_value=100,
        help="Apna guess yahan daalein 🤔"
    )
    
    # Submit button ke saath check karta hai ✅
    if st.button("Submit Guess 🚀"):
        attempts += 1  # Har attempt par counter badhata hai ➕
        
        # Guess ko check karne ka logic 🔍
        if guess < number:
            st.error("Too low! 📉😞 Neeche se try karein")
            st.image("https://emojicdn.elk.sh/🔻", width=30)
        elif guess > number:
            st.warning("Too high! 📈😮 Upar se try karein")
            st.image("https://emojicdn.elk.sh/🔺", width=30)
        else:
            # Correct guess par celebration 🎉
            st.balloons()
            st.success(f"Correct! 🎯👏 Aapne sirf {attempts} attempts mein guess kar liya!")
            st.write("🏆✨🎊🎇 Congratulations! 🥳")

if __name__ == "__main__":
    # Game ka title set karta hai computer emoji ke saath 💻
    st.title("Guess the Number (Computer) 🖥️🎮")
    # Game function ko start karta hai 🕹️
    guess_the_number_computer()