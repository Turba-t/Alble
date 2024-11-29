import random
import streamlit as st
import pandas as pd
import altair as alt

# Expanded dataset with additional attributes
albums = [
    {"name": "Thriller", "year": 1982, "artist_gender": "male", "band_size": 1, "nationality": "American", "genres": ["Pop", "R&B"], "artist": "Michael Jackson"},
    {"name": "Rumours", "year": 1977, "artist_gender": "mixed", "band_size": 4, "nationality": "British-American", "genres": ["Rock"], "artist": "Fleetwood Mac"},
    {"name": "The Dark Side of the Moon", "year": 1973, "artist_gender": "male", "band_size": 4, "nationality": "British", "genres": ["Progressive Rock"], "artist": "Pink Floyd"},
    {"name": "Back in Black", "year": 1980, "artist_gender": "male", "band_size": 4, "nationality": "Australian", "genres": ["Hard Rock"], "artist": "AC/DC"},
    {"name": "21", "year": 2011, "artist_gender": "female", "band_size": 1, "nationality": "British", "genres": ["Soul", "Pop"], "artist": "Adele"},
    {"name": "Hybrid Theory", "year": 2000, "artist_gender": "male", "band_size": 6, "nationality": "American", "genres": ["Nu Metal", "Rock"], "artist": "Linkin Park"},
    {"name": "Graduation", "year": 2007, "artist_gender": "male", "band_size": 1, "nationality": "American", "genres": ["Hip Hop", "Pop"], "artist": "Kanye West"},
    {"name": "To Pimp a Butterfly", "year": 2015, "artist_gender": "male", "band_size": 1, "nationality": "American", "genres": ["Hip Hop", "Pop"], "artist": "Kendrick Lamar"},
    {"name": "Purple Rain", "year": 1984, "artist_gender": "male", "band_size": 1, "nationality": "American", "genres": ["Rock", "Pop"], "artist": "Prince"},
    {"name": "Abbey Road", "year": 1969, "artist_gender": "male", "band_size": 4, "nationality": "British", "genres": ["Rock", "Alternative"], "artist": "The Beatles"},
    {"name": "Enter the Wu-Tang", "year": 1993, "artist_gender": "male", "band_size": 9, "nationality": "American", "genres": ["Hip Hop"], "artist": "Wu-Tang Clan"},
    {"name": "Back to Black", "year": 2007, "artist_gender": "female", "band_size": 1, "nationality": "British", "genres": ["Pop", "Jazz"], "artist": "Amy Winehouse"},
]

# Initialize session state
if "current_album" not in st.session_state:
    st.session_state["current_album"] = random.choice(albums)
if "guesses" not in st.session_state:
    st.session_state["guesses"] = 0
if "clues_revealed" not in st.session_state:
    st.session_state["clues_revealed"] = 0
if "game_over" not in st.session_state:
    st.session_state["game_over"] = False
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Function to reset the game
def reset_game():
    st.session_state["current_album"] = random.choice(albums)
    st.session_state["guesses"] = 0
    st.session_state["clues_revealed"] = 0
    st.session_state["game_over"] = False
    st.session_state["chat_history"] = []

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Play", "Stats"])

# Play Page
if page == "Play":
    st.title("Alble: Chat Edition")

    # Display chat history
    for message in st.session_state["chat_history"]:
        if message["type"] == "user":
            st.markdown(f"**You:** {message['text']}")
        else:
            st.markdown(f"**System:** {message['text']}")

    # User input
    user_input = st.text_input("Type your guess or question:")

    if user_input and not st.session_state["game_over"]:
        st.session_state["chat_history"].append({"type": "user", "text": user_input})
        st.session_state["guesses"] += 1

        current_album = st.session_state["current_album"]
        response = ""

        if user_input.lower() == current_album["name"].lower():
            response = f"🎉 Correct! The album was '{current_album['name']}' by {current_album['artist']}."
            st.session_state["game_over"] = True
        elif st.session_state["guesses"] >= 10:
            response = f"❌ Out of guesses! The correct answer was '{current_album['name']}' by {current_album['artist']}."
            st.session_state["game_over"] = True
        else:
            response = f"❌ Incorrect! You have {10 - st.session_state['guesses']} guesses left."
            st.session_state["clues_revealed"] += 1
            # Add clues
            if st.session_state["clues_revealed"] == 1:
                response += f" Clue: Year Released - {current_album['year']}."
            elif st.session_state["clues_revealed"] == 2:
                response += f" Clue: Artist Gender - {current_album['artist_gender']}."
            elif st.session_state["clues_revealed"] == 3:
                response += f" Clue: Band Size - {current_album['band_size']}."
            elif st.session_state["clues_revealed"] == 4:
                response += f" Clue: Nationality - {current_album['nationality']}."
            elif st.session_state["clues_revealed"] == 5:
                response += f" Clue: Genres - {', '.join(current_album['genres'])}."
            elif st.session_state["clues_revealed"] >= 6:
                response += f" Final Clue: Artist - {current_album['artist']}."

        st.session_state["chat_history"].append({"type": "system", "text": response})

    # Restart option
    if st.session_state["game_over"]:
        if st.button("Play Again"):
            reset_game()


# Stats Page
elif page == "Stats":
    st.title("Game Statistics")

    # Basic Stats
    stats = st.session_state["stats"]
    st.subheader("Summary")
    st.write(f"Total Games Played: {stats['games_played']}")
    st.write(f"Total Wins: {stats['wins']}")
    st.write(f"Total Losses: {stats['losses']}")
    if stats["games_played"] > 0:
        avg_guesses = sum(stats["guesses_per_game"]) / stats["games_played"]
        st.write(f"Average Guesses Per Game: {avg_guesses:.2f}")

    # Visualization: Bar chart of guesses per game
    if stats["games_played"] > 0:
        st.subheader("Guesses Per Game")
        guesses_df = pd.DataFrame({
            "Game": list(range(1, len(stats["guesses_per_game"]) + 1)),
            "Guesses": stats["guesses_per_game"]
        })
        chart = alt.Chart(guesses_df).mark_bar().encode(
            x="Game:O",
            y="Guesses:Q"
        ).properties(title="Guesses Per Game")
        st.altair_chart(chart, use_container_width=True)
