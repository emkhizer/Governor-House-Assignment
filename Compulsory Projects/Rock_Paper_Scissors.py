# rock_paper_scissors.py
import streamlit as st
import random

def rock_paper_scissors():
    # Session state ko initialize karna (wins counter ke liye)
    if 'wins' not in st.session_state:
        st.session_state.wins = 0

    # Game options emojis ke saath 🪨📄✂️
    choices = ['Rock 🪨', 'Paper 📄', 'Scissors ✂️']
    
    # Player ka input (Hindi label ke saath)
    player_choice = st.selectbox(
        "Select your choice:",
        choices,
        help="Select 1 From Rock, Paper And Scissors  🤔"
    )
    
    # Computer ki random choice generate karna
    computer_choice = random.choice(choices)
    
    # Computer ki choice dikhana
    st.markdown(f"**Computer's Choice :** {computer_choice}")
    
    # Game ka logic (jeet/kaar ka faisla)
    if player_choice == computer_choice:
        st.warning("Draw! 😐 Both Have Same Choice!")
        st.image("https://emojicdn.elk.sh/🤝", width=100)
    elif (
        (player_choice == 'Rock 🪨' and computer_choice == 'Scissors ✂️') or
        (player_choice == 'Scissors ✂️' and computer_choice == 'Paper 📄') or
        (player_choice == 'Paper 📄' and computer_choice == 'Rock 🪨')
    ):
        st.session_state.wins += 1  # Wins counter barhana
        st.balloons()
        st.success("You Won! 🎉🏆 WoW! 👏")
        st.image("https://emojicdn.elk.sh/🏅", width=80)
    else:
        st.error("You Loose 😔 Computer won! 💻🎯")
        st.image("https://emojicdn.elk.sh/😢", width=80)

    # Total Win dikhana
    st.write(f"Total Win: {st.session_state.wins} 🏆")

# Main program execution
if __name__ == "__main__":
    st.title("Rock 🪨 Paper 📄 Scissors ✂️ Game")
    rock_paper_scissors()
    
    # Dobara khelne ka button
    if st.button("Play Again? 🔄"):
        st.rerun()  # Session ko refresh karna