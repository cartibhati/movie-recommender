import pickle
import streamlit as st
import requests
import os

# ------------------------------------
# Page config
# ------------------------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# ------------------------------------
# Load TMDB API key SAFELY
# ------------------------------------
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# ------------------------------------
# Fetch poster safely
# ------------------------------------
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    if not TMDB_API_KEY:
        return None

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": TMDB_API_KEY, "language": "en-US"}
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=5
        )

        if response.status_code != 200:
            return None

        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path

    except requests.exceptions.RequestException:
        return None

    return None

# ------------------------------------
# Load data
# ------------------------------------
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# ------------------------------------
# Recommendation logic (UNCHANGED)
# ------------------------------------
def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters

# ------------------------------------
# UI
# ------------------------------------
st.header("🎬 Movie Recommender System")

if not TMDB_API_KEY:
    st.warning("TMDB API key not detected. Posters may not load.")

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button("Show Recommendation"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            if posters[i]:
                st.image(posters[i])
            else:
                st.write("Poster not available")
