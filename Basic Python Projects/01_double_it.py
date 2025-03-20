import streamlit as st

def double_number(num):
    return num * 2

st.title("Double It")
st.write("Enter a number to get its double.")

user_input = st.number_input("Enter a number:", min_value=0.0, step=0.1)
if st.button("Double It"):
    result = double_number(user_input)
    st.write(f"The double of {user_input} is {result}")