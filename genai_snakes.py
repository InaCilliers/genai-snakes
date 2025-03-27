import streamlit as st
import random

st.set_page_config(page_title="Gen AI Snakes & Ladders", layout="centered")

st.title("🎲 Gen AI Snakes & Ladders: Political Reality Check")
st.write("Use Gen AI wisely to climb the ladders. Make mistakes, and you'll slide down a snake. Your agency is your superpower.")

# Board configuration
ladders = {2: 10, 6: 15, 9: 19, 14: 21, 18: 24}
snakes = {8: 3, 12: 5, 17: 7, 20: 11, 23: 13}

# Session state to track position
if "position" not in st.session_state:
    st.session_state.position = 1
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Roll the die
if st.button("🎲 Roll the Dice"):
    if not st.session_state.game_over:
        roll = random.randint(1, 6)
        st.write(f"You rolled a {roll}!")

        new_position = st.session_state.position + roll
        if new_position > 25:
            st.write("You need the exact number to land on 25.")
        else:
            st.session_state.position = new_position
            st.write(f"You move to square {new_position}.")

            # Check for ladders
            if new_position in ladders:
                st.session_state.position = ladders[new_position]
                st.success(f"Ladder! You climb to square {ladders[new_position]}.")
            # Check for snakes
            elif new_position in snakes:
                st.session_state.position = snakes[new_position]
                st.error(f"Oops! Snake! You slide down to square {snakes[new_position]}.")

        if st.session_state.position == 25:
            st.balloons()
            st.success("🏁 You reached the end! Gen AI used wisely!")
            st.session_state.game_over = True

# Display board position
st.info(f"📍 You are currently on square {st.session_state.position}")

# Reset game
if st.button("🔄 Restart Game"):
    st.session_state.position = 1
    st.session_state.game_over = False
