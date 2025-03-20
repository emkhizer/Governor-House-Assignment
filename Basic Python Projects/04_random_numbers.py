import streamlit as st
import random

# Function to generate random numbers
def generate_random_numbers(count, min_value=1, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(count)]

# Streamlit app
st.title("🎲 Random Numbers Generator")
st.write("Generate a list of random numbers with custom options! 🔢")

# User inputs
col1, col2 = st.columns(2)
with col1:
    user_input = st.number_input("How many random numbers do you want to generate?", 
                                min_value=1, value=5, key="count")
with col2:
    min_value = st.number_input("Minimum value", min_value=1, value=1, key="min")
    max_value = st.number_input("Maximum value", min_value=min_value + 1, value=100, key="max")

# Generate numbers button
if st.button("✨ Generate Numbers"):
    if min_value >= max_value:
        st.error("❌ The minimum value must be less than the maximum value!")
    else:
        random_numbers = generate_random_numbers(user_input, min_value, max_value)
        st.success("✅ Successfully generated random numbers!")
        st.write("🔢 Generated random numbers:", random_numbers)
        st.write("📊 Summary:")
        st.write(f"- Total numbers: {len(random_numbers)}")
        st.write(f"- Smallest number: {min(random_numbers)}")
        st.write(f"- Largest number: {max(random_numbers)}")
        st.write(f"- Sum of numbers: {sum(random_numbers)}")