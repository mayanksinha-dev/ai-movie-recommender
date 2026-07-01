import pickle
import streamlit as st
import requests
import pandas as pd

st.markdown("""
<style>
.movie-title {
    text-align: center;
    font-weight: bold;
    font-size: 18px;
    height: 55px;      /* Same space for every title */
    overflow: hidden;  /* Extra text hide */
    word-wrap: break-word;
    white-space: normal;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0d856699ca92b63b2fd87eeb7e73564d&language=en-US"

    response = requests.get(url)
    data = response.json()

    poster_path = data.get("poster_path")

    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pd.DataFrame(pickle.load(open('movie_dic.pkl','rb')))
similarity = pickle.load(open('sm.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    (movie_list),
)

if st.button("Show Recommendation"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(
            f'<div class="movie-title" title="{recommended_movie_names[0]}">{recommended_movie_names[0]}</div>',
            unsafe_allow_html=True
        )
        st.image(recommended_movie_posters[0], use_container_width=True)

    with col2:
        st.markdown(
            f'<div class="movie-title" title="{recommended_movie_names[1]}">{recommended_movie_names[1]}</div>',
            unsafe_allow_html=True
        )
        st.image(recommended_movie_posters[1], use_container_width=True)

    with col3:
        st.markdown(
            f'<div class="movie-title" title="{recommended_movie_names[2]}">{recommended_movie_names[2]}</div>',
            unsafe_allow_html=True
        )
        st.image(recommended_movie_posters[2], use_container_width=True)

    with col4:
        st.markdown(
            f'<div class="movie-title" title="{recommended_movie_names[3]}">{recommended_movie_names[3]}</div>',
            unsafe_allow_html=True
        )
        st.image(recommended_movie_posters[3], use_container_width=True)

    with col5:
        st.markdown(
            f'<div class="movie-title" title="{recommended_movie_names[4]}">{recommended_movie_names[4]}</div>',
            unsafe_allow_html=True
        )
        st.image(recommended_movie_posters[4], use_container_width=True)