# guess_the_number_user.py
# Streamlit aur random modules ko import karta hai 🐍📦
import streamlit as st
import random

def guess_the_number_user():
    # User ko instructions deta hai number sochne ke liye 🧠💡
    st.write("Think of a number between 1 and 100. I will try to guess it! 🤔🔢")
    
    # Number range aur attempts counter set karta hai 🎯
    low, high = 1, 100
    attempts = 0
    
    # Binary search strategy use karta hai 🔍
    while low <= high:
        # Computer apna guess banata hai midpoint se ➗
        guess = (low + high) // 2
        attempts += 1
        
        # User se feedback leta hai dropdown se 📝
        feedback = st.selectbox(
            f"Mera guess #{attempts}: Kya aapka number {guess} hai? 🤖",
            ["Haan! ✅", "Mera number bada hai 📈", "Mera number chota hai 📉"],
            key=f"attempt_{attempts}"  # Har attempt ka unique key
        )
        
        # Feedback ke hisab se action leta hai ⚙️
        if feedback == "Haan! ✅":
            st.balloons()  # Celebration animation 🎉
            st.success(f"Yehi toh tha! 🎯 Mainne sirf {attempts} attempts mein guess kar liya! 🥳")
            st.write("🏆✨ Computer Wins! 🎮👑")
            break
        elif feedback == "Mera number bada hai 📈":
            low = guess + 1  # Lower bound update karta hai ⬆️
            st.write(f"Okay, main {guess+1} se 100 ke beech dhoondta hoon... 🔄")
        elif feedback == "Mera number chota hai 📉":
            high = guess - 1  # Upper bound update karta hai ⬇️
            st.write(f"Chalo main 1 se {guess-1} tak check karta hoon... 🔄")
    else:
        # Agar loop complete ho gaya toh defeat message 😞
        st.error("Oops! 🤯 Main aapka number nahi dhoond paaya. Kya aapne rules follow kiye the? 😅")

# Main program execution
if __name__ == "__main__":
    # Game ka title set karta hai with emojis 📌
    st.title("Guess the Number (User vs Computer) 🧠🆚🤖")
    # Game function ko start karta hai 🕹️
    guess_the_number_user()