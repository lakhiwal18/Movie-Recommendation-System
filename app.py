import pickle

import pandas as pd
import streamlit as st
import requests
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Welcome To My Movie Recommendation System',
    movies['title'].values)



if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0],width=120)
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1],width=120)

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2],width=120)
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3],width=120)
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4],width=120)



