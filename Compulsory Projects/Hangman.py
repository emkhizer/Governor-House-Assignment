# hangman.py
import streamlit as st
import random

def hangman():
    # Game ki basic settings initialize karna 🎮
    if 'word' not in st.session_state:
        st.session_state.word = random.choice(['🐍python', '🚶hangman', '🏆challenge', '💻programming'])
        st.session_state.guessed_letters = set()
        st.session_state.remaining_attempts = 6
        st.session_state.game_over = False

    # Hangman ki stages ko define karna with emojis 🎨
    HANGMAN_STAGES = [
        """
          -----
          |   |
          😊  |
              |
              |
              |
        -------
        """,
        """
          -----
          |   |
          😟  |
          |   |
              |
              |
        -------
        """,
        """
          -----
          |   |
          😖  |
         /|   |
              |
              |
        -------
        """,
        """
          -----
          |   |
          😫  |
         /|\\  |
              |
              |
        -------
        """,
        """
          -----
          |   |
          😭  |
         /|\\  |
         /    |
              |
        -------
        """,
        """
          -----
          |   |
          💀  |
         /|\\  |
         / \\  |
              |
        -------
        """
    ]
    
    # Game interface setup 🖼️
    st.title("Hangman Game 🎯")
    st.markdown("---")
    
    # Current game state display 📊
    masked_word = ' '.join(
        [f"🎉{char}" if char in st.session_state.guessed_letters else "🌿_" 
         for char in st.session_state.word if char != ' ']
    )
    st.markdown(f"### **Word:** {masked_word}")
    st.markdown(f"### **Attempts Left:** {'❤️' * st.session_state.remaining_attempts}")
    
    # Display current hangman state 🖼️
    current_stage = 5 - st.session_state.remaining_attempts
    st.code(HANGMAN_STAGES[current_stage], language="ascii-art")
    
    # Game logic aur user input handling 🕹️
    if not st.session_state.game_over:
        user_guess = st.text_input("Enter a letter 🔤:", max_chars=1).lower()
        
        if st.button("Submit ✅"):
            # Input validation check ✅
            if not user_guess.isalpha():
                st.error("❌ Invalid! Please enter only alphabets!")
            
            # Repeat guess check 🔄
            elif user_guess in st.session_state.guessed_letters:
                st.warning("⚠️ You already tried this letter!")
            
            # New guess processing 🆕
            else:
                st.session_state.guessed_letters.add(user_guess)
                
                # Incorrect guess handling ❌
                if user_guess not in st.session_state.word:
                    st.session_state.remaining_attempts -= 1
                    st.markdown("### ❌ Incorrect guess!")
                
                # Correct guess handling ✅
                else:
                    st.markdown("### ✅ Correct guess!")
                
                # Win/lose conditions check 🏁
                if all(char in st.session_state.guessed_letters for char in st.session_state.word):
                    st.session_state.game_over = True
                    st.balloons()
                    st.success("🎉🏆 Congratulations! You won!")
                
                elif st.session_state.remaining_attempts <= 0:
                    st.session_state.game_over = True
                    st.error(f"💀 Game Over! Correct word was: {st.session_state.word}")

    # Game restart mechanism 🔄
    if st.session_state.game_over:
        if st.button("🔄 Play Again?"):
            # Session state clear karna
            for key in ['word', 'guessed_letters', 'remaining_attempts', 'game_over']:
                if key in st.session_state:
                    del st.session_state[key]

if __name__ == "__main__":
    hangman()


# Game ki basic settings initialize karna - Game shuru karte waqt basic settings tayar karna

# Hangman ki stages ko define karna - Har attempt ke badalne par dikhne wali tasweer

# Game interface setup - Game ka khoobsurat dikhav banana

# Current game state display - Khiladi ko game ki latest halat dikhana

# Display current hangman state - Hangman ki maujooda soorat-e-haal dikhana

# Game logic aur user input handling - Khiladi ke inputs ka intezam aur game ka faisla

# Input validation check - Sahi tarah ka input ya na hone ki tasdeeq

# Repeat guess check - Pehle try kiye gaye harf ki dobara koshish

# New guess processing - Naye guess ka tajzia aur asar

# Win/lose conditions check - Jeet ya haar ki sharton ki tasdeeq

# Game restart mechanism - Dobara khelne ka intezam