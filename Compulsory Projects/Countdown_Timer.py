# Streamlit aur time modules ko import karna
import streamlit as st
import time

# Countdown timer ki main function
def countdown_timer():
    # Session state ko shuru karna (timer ki settings kay liye)
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None  # Timer ka shuruati waqt
        st.session_state.remaining = 0      # Bacha hua time
        st.session_state.running = False    # Timer chal raha hai ya nahi

    # Time ko minutes aur seconds mein format karne ka function
    def format_time(seconds):
        mins, secs = divmod(seconds, 60)  # Seconds ko minutes aur seconds mein taqseem karna
        return f"⏳ {mins:02d}:{secs:02d}"  # Emoji ke saath formatted time

    # Application ka main interface
    st.title("Countdown Timer ⏱️")  # Title with emoji
    st.markdown("---")  # Horizontal line for design

    # User se time input lena
    input_seconds = st.number_input(
        "Enter seconds ⏲️:",  # Input ka label
        min_value=1,          # Kam se kam 1 second
        value=60,             # Default value
        help="Enter time in seconds"  # Help text
    )

    # Control buttons ka layout
    col1, col2, col3 = st.columns(3)  # 3 columns mein buttons
    
    # Start button
    with col1:
        if st.button("Start 🚀") and not st.session_state.running:
            st.session_state.start_time = time.time()  # Current time record karna
            st.session_state.remaining = input_seconds  # Total time set karna
            st.session_state.running = True  # Timer ko chalana
    
    # Stop button
    with col2:
        if st.button("Stop ⏹️") and st.session_state.running:
            st.session_state.running = False  # Timer ko rokna
    
    # Reset button
    with col3:
        if st.button("Reset 🔄"):
            st.session_state.running = False  # Timer band karna
            st.session_state.remaining = input_seconds  # Time ko reset karna
            st.rerun()  # Display ko update karna

    # Timer ka hisaab-kitaab
    if st.session_state.running:
        elapsed = time.time() - st.session_state.start_time  # Guzra hua time
        st.session_state.remaining = max(input_seconds - int(elapsed), 0)  # Bachi hui time update
    else:
        st.session_state.remaining = st.session_state.remaining  # Purani value rakna

    # Progress bar ka hisaab
    progress = 1 - (st.session_state.remaining / input_seconds) if input_seconds > 0 else 0
    st.progress(progress)  # Progress bar dikhana

    # Time display ka section
    time_display = st.empty()  # Khali container banana
    time_display.markdown(f"# {format_time(st.session_state.remaining)}")  # Formatted time dikhana

    # Khud-ba-khud update karne ka system
    if st.session_state.running:
        time.sleep(0.1)  # 0.1 second ka intezar
        st.rerun()  # Puri app ko dobara chalana

    # Timer khatam hone ka check
    if st.session_state.remaining <= 0 and st.session_state.running:
        st.session_state.running = False  # Timer band karna
        st.balloons()  # Celebration animation
        st.error("⏰ Time's up! 🎉")  # Alert message
        st.audio("https://assets.mixkit.co/active_storage/sfx/2572/2572-preview.mp3")  # Alarm sound

# Application ko chalana
if __name__ == "__main__":
    countdown_timer()  # Main function call