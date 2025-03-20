# Import Streamlit library to create the web app interface
import streamlit as st

# Import random library for random selection of jokes and emojis
import random

# Function to store and return random jokes
def tell_joke():
    # List of jokes with various categories (science, wordplay, tech)
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything! 👨🔬",  # Science joke
        "I told my wife she was drawing her eyebrows too high. She looked surprised. 😲",  # Wordplay
        "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",  # Pun
        "Why don't skeletons fight each other? They don't have the guts! 💀",  # Halloween joke
        "What do you call fake spaghetti? An impasta! 🍝",  # Food pun
        "Why did the computer go to school? It wanted to improve its byte-size! 💻",  # Tech joke
        "What do you get when you cross a snowman and a vampire? Frostbite! ⛄",  # Seasonal joke
        "Why don't eggs tell jokes? They'd crack up! 🥚"  # Food pun
    ]
    return random.choice(jokes)  # Return random joke from list

# Set up the main page configuration
st.title("🤖 Joke Bot 3000")  # Title with robot emoji
st.write("Welcome to the Joke Bot! 😄 Let's laugh together!")  # Welcome message with smiley

# List of reaction emojis/stickers (using markdown emojis)
reactions = ["😂", "🤣", "😆", "🎉", "👏", "💡", "✨", "🎈"]

# Create a button with a laughing emoji
if st.button("Tell Me a Joke 😂"):
    # Get random joke from function
    joke = tell_joke()
    
    # Display joke in bold with random reaction emoji
    st.markdown(f"**{joke}** " + random.choice(reactions))
    
    # Add extra visual effects
    st.balloons()  # Animated balloons for celebration effect
    st.write("")  # Empty space for better spacing

# Optional: Add sidebar explanation (hidden feature)
with st.sidebar:
    st.write("*Psst... I'm using:*")
    st.code("Python 3.8\nStreamlit 1.11.0\nRandom module", language="bash")