import streamlit as st
import random

# Initialize game state variables
if "location" not in st.session_state:
    st.session_state["location"] = "village"
if "player_name" not in st.session_state:
    st.session_state["player_name"] = None
if "player_class" not in st.session_state:
    st.session_state["player_class"] = None
if "score" not in st.session_state:
    st.session_state["score"] = 0
if "next_location" not in st.session_state:
    st.session_state["next_location"] = None

# Introduction
st.title("🌍 Conditional Adventure RPG")
st.write("Welcome to the world of **Conditionalia**, where your journey is shaped by your choices and answers!")

# Player setup
if not st.session_state["player_name"]:
    st.session_state["player_name"] = st.text_input("Enter your name to begin your journey:")
if st.session_state["player_name"] and not st.session_state["player_class"]:
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

# Current location and NPC interaction
current_location = st.session_state["location"]
location_data = locations[current_location]

# Display location details
st.subheader(f"📍 Location: {current_location.capitalize()}")
st.write(location_data["description"])
st.write(f"An NPC ({location_data['npc']}) approaches you with a question:")

# NPC asks a conditional question
st.write(f"**{location_data['npc']}**: {location_data['question']}")

# Player response
answer = st.text_input("Your answer:")

if answer:
    st.session_state["score"] += random.randint(10, 30)  # Reward points
    st.success(f"{location_data['npc']} nods in approval. You earned points!")
    st.write(f"🎉 Your current score: {st.session_state['score']}")

    # Travel options
    available_locations = [loc for loc in locations.keys() if loc != current_location]
    st.session_state["next_location"] = st.radio(
        "Choose your next destination:",
        available_locations,
        key="next_location"
    )

if st.session_state["next_location"]:
    if st.button("Travel"):
        st.session_state["location"] = st.session_state["next_location"]
        st.session_state["next_location"] = None  # Reset travel choice
