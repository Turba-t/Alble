import random
import streamlit as st
import pandas as pd
import altair as alt
import streamlit as st

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
import random
import time


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! Guess the album in 10 atteampts!",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Expanded dataset with additional attributes
albums = [
    {"name": "Thriller", "year": 1982, "artist_gender": "male", "band_size": 1, "nationality": "American", "genres": ["Pop", "R&B"], "artist": "Micheal Jackson"},
    {"name": "Rumours", "year": 1977, "artist_gender": "mixed", "band_size": 4, "nationality": "British-American", "genres": ["Rock"], "artist": "Fleetwood Mac"},
    {"name": "The Dark Side of the Moon", "year": 1973, "artist_gender": "male", "band_size": 4, "nationality": "British", "genres": ["Progressive Rock"], "artist": "Pink Floyd"},
    {"name": "Back in Black", "year": 1980, "artist_gender": "male", "band_size": 4, "nationality": "Australian", "genres": ["Hard Rock"], "artist": "ACDC"},
    {"name": "21", "year": 2011, "artist_gender": "female", "band_size": 1, "nationality": "British", "genres": ["Soul", "Pop"], "artist": "Adelle"},
    {"name": "Hybrid Theory", "year": 2000, "artist_gender": "male", "band_size": 6, "nationality": "American", "genres": ["Nu Metal", "Rock"], "artist": "Linkin Park"},
    {"name": "Bad", "year": 1987, "artist_gender": "male", "band_size": 1, "nationality": "American", "genres": ["Pop", "Funk"], "artist": "Micheal Jackson"},
    {"name": "Graduation", "year": 2007, "artist_gender": "male", "band_size": 1, "nationality": "American", "genres": ["Hip Hop", "Pop"], "artist": "Kanye West"},
    {"name": "My beautiful dark twisted fantasy", "year": 2010, "artist_gender": "male", "band_size": 1, "nationality": "American", "genres": ["Hip Hop", "Pop"], "artist": "Kanye West"},
    {"name": "To pimp a butterfly", "year": 2015, "artist_gender": "male", "band_size": 1, "nationality": "American", "genres": ["Hip Hop", "Pop"], "artist": "Kendrick Lamar"},
    {"name": "Kid A", "year": 2000, "artist_gender": "male", "band_size": 5, "nationality": "British", "genres": ["Rock", "Alternative"], "artist": "Radiohead"},
    {"name": "Ok Computer", "year": 1997, "artist_gender": "male", "band_size": 5, "nationality": "British", "genres": ["Rock", "Alternative"], "artist": "Radiohead"},
    {"name": "Discovery", "year": 2001, "artist_gender": "male", "band_size": 2, "nationality": "French", "genres": ["Electronic"], "artist": "Daft Punk"},
    {"name": "Purple Rain", "year": 1984, "artist_gender": "male", "band_size": 1, "nationality": "American", "genres": ["Rock", "Pop"], "artist": "Prince"},
    {"name": "Abbey Road", "year": 1969, "artist_gender": "male", "band_size": 4, "nationality": "British", "genres": ["Rock", "Alternative"], "artist": "The Beatles"},
    {"name": "Wish you were here", "year": 1975, "artist_gender": "male", "band_size": 4, "nationality": "British", "genres": ["Progressive Rock"], "artist": "Pink Floyd"},
    {"name": "Enter the Wu-Tang", "year": 1993, "artist_gender": "male", "band_size": 9, "nationality": "American", "genres": ["Hip Hop"], "artist": "Wu-Tang Clan"},
    {"name": "Back To Black", "year": 2007, "artist_gender": "female", "band_size": 1, "nationality": "British", "genres": ["Pop", "Jazz"], "artist": "Amy Whinehouse"},
    {"name": "Sour", "year": 2021, "artist_gender": "female", "band_size": 1, "nationality": "American", "genres": ["Pop"], "artist": "Olivia Rodrigo"},
    {"name": "Brat", "year": 2024, "artist_gender": "female", "band_size": 1, "nationality": "British", "genres": ["Electronic"], "artist": "Charli XCX"},
    {"name": "When We All Fall Asleep Where Do We Go?", "year": 2019, "artist_gender": "female", "band_size": 1, "nationality": "American", "genres": ["Pop"], "artist": "Billie Eilish"},
    {"name": "Damn", "year": 2017, "artist_gender": "male", "band_size": 1, "nationality": "American", "genres": ["Hip Hop"], "artist": "Kendrick Lamar"},
    {"name": "Nectar", "year": 2020, "artist_gender": "male", "band_size": 1, "nationality": "Japanese/American", "genres": ["Pop"], "artist": "Joji"},
    {"name": "The Miseducation of Lauryn Hill", "year": 1998, "artist_gender": "female", "band_size": 1, "nationality": "American", "genres": ["Hip Hop"], "artist": "Lauryn Hill"},
    {"name": "Brat", "year": 2024, "artist_gender": "female", "band_size": 1, "nationality": "British", "genres": ["Electronic"], "artist": "Charli XCX"},
    {"name": "Demon Days", "year": 2005, "artist_gender": "mixed", "band_size": 4, "nationality": "British", "genres": ["Pop", "Progressive Rock"], "artist": "Gorillaz"},
    
    
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
if "stats" not in st.session_state:
    st.session_state["stats"] = {
        "games_played": 0,
        "wins": 0,
        "losses": 0,
        "guesses_per_game": []
    }

# Function to update stats
def update_stats(won, guesses):
    st.session_state["stats"]["games_played"] += 1
    if won:
        st.session_state["stats"]["wins"] += 1
    else:
        st.session_state["stats"]["losses"] += 1
    st.session_state["stats"]["guesses_per_game"].append(guesses)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Play", "Stats"])

# Play Page
if page == "Play":
    st.title("Alble")
    st.write("Guess the album within 10 attempts!")

    current_album = st.session_state["current_album"]
    user_guess = st.text_input("Your Guess:")

    if user_guess and not st.session_state["game_over"]:
        st.session_state["guesses"] += 1
        if user_guess.lower() == current_album["name"].lower():
            st.success(f"Correct! The album was '{current_album['name']}' by {current_album['artist']} 🎉")
            update_stats(won=True, guesses=st.session_state["guesses"])
            st.session_state["game_over"] = True
        elif st.session_state["guesses"] >= 10:
            st.error(f"Out of guesses! The correct answer was '{current_album['name']}' by {current_album['artist']}.")
            update_stats(won=False, guesses=st.session_state["guesses"])
            st.session_state["game_over"] = True
        else:
            st.warning(f"Incorrect! You have {10 - st.session_state['guesses']} guesses left.")
            st.session_state["clues_revealed"] += 1

    # Display clues if not game over
    if not st.session_state["game_over"]:
        if st.session_state["guesses"] > 0:  # Show clues after the first guess
            st.subheader("Clues:")
            if st.session_state["clues_revealed"] >= 1:
                st.write(f"Year Released: {current_album['year']}")
            if st.session_state["clues_revealed"] >= 2:
                st.write(f"Artist Gender: {current_album['artist_gender']}")
            if st.session_state["clues_revealed"] >= 3:
                st.write(f"Band Size: {current_album['band_size']}")
            if st.session_state["clues_revealed"] >= 4:
                st.write(f"Nationality: {current_album['nationality']}")
            if st.session_state["clues_revealed"] >= 5:
                st.write(f"Genres: {', '.join(current_album['genres'])}")
            if st.session_state["clues_revealed"] >= 6:
                st.write(f"Artist: {current_album['artist']}")


    # Option to play again
    if st.session_state["game_over"]:
        if st.button("Play Again"):
            st.session_state["current_album"] = random.choice(albums)
            st.session_state["guesses"] = 0
            st.session_state["clues_revealed"] = 0
            st.session_state["game_over"] = False

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
