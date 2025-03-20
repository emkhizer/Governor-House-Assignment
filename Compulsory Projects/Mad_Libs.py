# madlibs.py
# Streamlit library ko import karta hai web applications banane ke liye 🚀
import streamlit as st

# Mad Libs game ke liye main function define karta hai 📖
def mad_libs():
    # User se noun (sangya) input lene ke liye text box show karta hai 📦
    noun = st.text_input("Enter a noun 📦: ")
    # User se verb (kriya) input lene ke liye text box show karta hai 🏃
    verb = st.text_input("Enter a verb 🏃: ")
    # User se adjective (visheshan) input lene ke liye text box show karta hai 🌈
    adjective = st.text_input("Enter an adjective 🌈: ")
    
    # "Generate Story" button ka check karta hai 🎮. Agar click kiya gaya hai toh:
    if st.button("Generate Story ✨"):
        # User ke inputs ko mila kar story banata hai 🧩
        story = f"The {adjective} {noun} {verb} over the lazy dog 🐶. Wow! 😄"
        # Banayi hui story ko webpage par display karta hai 🖥️
        st.success("Here's your story! 🎉")
        st.write(story)
        # Celebration sticker ke liye emojis add karta hai 🎊
        st.write("🎈✨🎇🎆🥳")

# Script ko directly run kiya gaya hai ya nahi check karta hai 🔍
if __name__ == "__main__":
    # Webpage ka title set karta hai "Mad Libs" ke saath emoji 📌
    st.title("Mad Libs 🎮📝")
    # Mad Libs function ko call karta hai game start karne ke liye 🕹️
    mad_libs()