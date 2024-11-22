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
        "
