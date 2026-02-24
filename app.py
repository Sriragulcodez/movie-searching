import streamlit as st
import random
from omdb_service import fetch_movies
from quicksort import quicksort

movie_cache = {}

st.set_page_config(page_title="Smart Movie Assistant", layout="centered")
st.title("🎬 Smart Movie Decision Assistant")

tab1, tab2, tab3 = st.tabs(["🔍 Search", "🎭 Mood", "🎲 Surprise"])

# ---------------- SEARCH TAB ----------------
with tab1:
    st.header("Search Movies")

    search_query = st.text_input("Enter movie name")
    sort_option = st.selectbox("Sort by", ["year", "title"])

    if st.button("Search"):
        if search_query:
            movies = fetch_movies(search_query)

            if not movies:
                st.warning("No movies found.")
            else:
                detailed_movies = []

                for movie in movies:
                    imdb_id = movie["imdbID"]
                    if imdb_id in movie_cache:
                        detailed_movies.append(movie_cache[imdb_id])
                    else:
                        movie_cache[imdb_id] = movie
                        detailed_movies.append(movie)

                sorted_movies = quicksort(detailed_movies, sort_option)

                for movie in sorted_movies:
                    st.subheader(f"{movie['Title']} ({movie['Year']})")

                    imdb_url = f"https://www.imdb.com/title/{movie['imdbID']}/"
                    watch_url = f"https://www.google.com/search?q=watch+{movie['Title'].replace(' ', '+')}+online"

                    st.markdown(f"[🎬 View on IMDb]({imdb_url})")
                    st.markdown(f"[📺 Where to Watch]({watch_url})")
                    st.markdown("---")

# ---------------- MOOD TAB ----------------
with tab2:
    st.header("Pick Your Mood")

    mood = st.selectbox("Select Mood", [
        "Feel Good",
        "Action Packed",
        "Emotional",
        "Mind Bending",
        "Family Night"
    ])

    mood_map = {
        "Feel Good": "comedy",
        "Action Packed": "action",
        "Emotional": "drama",
        "Mind Bending": "thriller",
        "Family Night": "family"
    }

    if st.button("Find Movies"):
        keyword = mood_map[mood]
        movies = fetch_movies(keyword)

        for movie in movies[:5]:
            st.subheader(f"{movie['Title']} ({movie['Year']})")
            imdb_url = f"https://www.imdb.com/title/{movie['imdbID']}/"
            st.markdown(f"[🎬 View on IMDb]({imdb_url})")
            st.markdown("---")

# ---------------- SURPRISE TAB ----------------
with tab3:
    st.header("Surprise Me 🎲")

    if st.button("Give Me a Movie"):
        movies = fetch_movies("movie")

        if movies:
            random_movie = random.choice(movies)
            st.subheader(f"{random_movie['Title']} ({random_movie['Year']})")

            imdb_url = f"https://www.imdb.com/title/{random_movie['imdbID']}/"
            watch_url = f"https://www.google.com/search?q=watch+{random_movie['Title'].replace(' ', '+')}+online"

            st.markdown(f"[🎬 View on IMDb]({imdb_url})")
            st.markdown(f"[📺 Where to Watch]({watch_url})")