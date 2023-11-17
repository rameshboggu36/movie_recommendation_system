import pandas as pd
import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=6ca8c426cad94bc566892fee5465a380&language=en-US'.format(
            movie_id))
    return 'https://image.tmdb.org/t/p/w500/{}'.format(response.json()['poster_path'])


def recommend(movie):
    recommended_movies = recommendations[movie]
    recommended_poster = []
    out_movies = []
    for i in recommended_movies:
        movie_id = movies.iloc[i[0]].movie_id
        movie_title = movies[movies['movie_id'] == movie_id]['title'].to_list()
        out_movies.append(movie_title[0])
        recommended_poster.append(fetch_poster(movie_id))
    return out_movies, recommended_poster


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
recommendations = pickle.load(open('recommendations.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
st.title("Movie Recommendation System by Ramesh")

selected_movie = st.selectbox(
    'Which movie you like?', movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    st.text('Ramesh recommends these movies for you:')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
