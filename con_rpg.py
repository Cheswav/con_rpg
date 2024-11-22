import streamlit as st
import random

# Setup game state
if "location" not in st.session_state:
    st.session_state["location"] = "village"
if "player_name" not in st.session_state:
    st.session_state["player_name"] = None
if "player_class" not in st.session_state:
    st.session_state["player_class"] = None
if "score" not in st.session_state:
    st.session_state["score"] = 0

# Introduction
st.title("🌍 Conditional Adventure RPG")
st.write("Welcome to the world of **Conditionalia**, where your journey is shaped by your choices and answers!")

# Player setup
if not st.session_state["player_name"]:
    st.session_state["player_name"] = st.text_input("Enter your name to begin your journey:")
if not st.session_state["player_class"] and st.session_state["player_name"]:
    st.session_state["player_class"] = st.radio("Choose your class:", ["Warrior", "Mage", "Explorer"])

if st.session_state["player_name"] and st.session_state["player_class"]:
    st.write(f"Welcome, {st.session_state['player_name']} the {st.session_state['player_class']}! Your adventure begins now.")
    st.markdown("---")

# Game locations and NPC interactions
locations = {
    "village": {
        "description": "You arrive in a bustling village. The market is lively, and an old merchant greets you.",
        "npc": "Merchant",
        "question": "If you sell all your wares today, what will you do with the money?",
    },
    "forest": {
        "description": "You wander into a dense forest. A mysterious ranger appears from the shadows.",
        "npc": "Ranger",
        "question": "If you were invisible, how would you explore the forest?",
    },
    "castle": {
        "description": "A grand castle looms ahead. Inside, the king sits on his throne, waiting for your answer.",
        "npc": "King",
        "question": "If you became ruler of this land, what would you change first?",
    },
}

# Display current location
current_location = st.session_state["location"]
location_data = locations[current_location]
st.subheader(f"📍 Location: {current_location.capitalize()}")
st.write(location_data["description"])
st.write(f"An NPC ({location_data['npc']}) approaches you with a question:")

# NPC asks a conditional question
st.write(f"**{location_data['npc']}**: {location_data['question']}")

# Player responds
answer = st.text_input("Your answer:")

# Respond and move to the next location
if answer:
    st.session_state["score"] += random.randint(10, 30)  # Reward points
    st.success(f"{location_data['npc']} nods in approval. You earned points!")
    st.write(f"🎉 Your current score: {st.session_state['score']}")

    # Travel to the next location
    next_location = st.radio(
        "Choose your next destination:",
        [loc for loc in locations.keys() if loc != current_location],
        key="next_location"
    )
    if st.button("Travel"):
        st.session_state["location"] = next_location
        st.experimental_rerun()  # Refresh to load the new location
