
import streamlit as st
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(page_title="Gen AI Snakes & Ladders", layout="centered")

st.title("🎲 Gen AI Snakes & Ladders: Political Reality Check")
st.write("Use Gen AI wisely to climb the ladders. Make mistakes, and you'll slide down a snake. Your agency is your superpower.")

# Game setup
board_size = 5
ladders = {2: 10, 6: 15, 9: 19, 14: 21, 18: 24}
ladder_msgs = {
    2: "Used Gen AI to reframe a Facebook post—sounded professional.",
    6: "Turned oversight notes into a punchy Substack article.",
    9: "Asked AI to simplify a complex concept—constituents loved it.",
    14: "Used Gen AI to draft 3 speech options—chose the best.",
    18: "Prompted AI to moderate tone—hit the right message."
}

snakes = {8: 3, 12: 5, 17: 7, 20: 11, 23: 13}
snake_msgs = {
    8: "Published AI content without tone-check—sounded arrogant.",
    12: "Let AI write a crisis post—public backlash hit hard.",
    17: "Blamed ChatGPT for an error—credibility took a knock.",
    20: "Used AI in a speech without context—audience confused.",
    23: "Asked AI to write about a sensitive ward issue—no empathy."
}

# Session state
if "position" not in st.session_state:
    st.session_state.position = 1
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Draw the board
def draw_board(position):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(0, board_size)
    ax.set_ylim(0, board_size)
    ax.axis("off")

    for i in range(board_size):
        for j in range(board_size):
            square = i * board_size + j + 1
            row = board_size - 1 - i
            col = j if i % 2 == 0 else board_size - 1 - j
            ax.add_patch(patches.Rectangle((col, row), 1, 1, fill=True, edgecolor='black', facecolor='white'))
            ax.text(col + 0.5, row + 0.5, str(square), va='center', ha='center')

            if square == position:
                ax.plot(col + 0.5, row + 0.5, marker='o', markersize=20, color='orange')

    st.pyplot(fig)

# Roll dice
if st.button("🎲 Roll the Dice"):
    if not st.session_state.game_over:
        roll = random.randint(1, 6)
        st.write(f"You rolled a {roll}!")

        new_pos = st.session_state.position + roll
        if new_pos > 25:
            st.write("You need the exact number to land on 25.")
        else:
            st.session_state.position = new_pos
            st.write(f"You move to square {new_pos}.")

            if new_pos in ladders:
                st.session_state.position = ladders[new_pos]
                st.success(f"Ladder! {ladder_msgs[new_pos]} You climb to {ladders[new_pos]}.")
            elif new_pos in snakes:
                st.session_state.position = snakes[new_pos]
                st.error(f"Snake! {snake_msgs[new_pos]} You slide to {snakes[new_pos]}.")

        if st.session_state.position == 25:
            st.success("🏁 You reached square 25! Gen AI mastered!")
            st.balloons()
            st.session_state.game_over = True

# Show board + position
draw_board(st.session_state.position)
st.info(f"📍 You are currently on square {st.session_state.position}")

if st.button("🔄 Restart Game"):
    st.session_state.position = 1
    st.session_state.game_over = False
                
