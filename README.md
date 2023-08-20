<div id="header" align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2k4bTM0Z3pnN3ZwaHk5dmxsd2kwbjZ2anJicmQ4ejF0aGd4N3lsMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qE3DniPVVNCiDaUltX/giphy.gif" width="700" height="300"/>
</div>

# Movie Recommendation System:-
This is a Movie Recommendation System that utilizes the TMDB dataset to provide personalized movie recommendations. The system is built using Python and deployed using the Streamlit library. Users can input their preferences and receive movie recommendations based on their selections.

##  Introduction:-
The Movie Recommendation System is designed to assist users in discovering new movies that align with their interests. By analyzing the TMDB dataset, the system generates recommendations using Content-Based  Filtering techniques. The Streamlit library is used to create an interactive user interface, making it easy for users to input their preferences and receive relevant movie suggestions.The Movie Recommendation System is a Python-based project that offers personalized movie recommendations to users using machine learning techniques. This system analyzes movie features such as genres, cast, and keywords to suggest movies that are similar to the user's preferences.The Movie Recommendation System leverages movie metadata, including genres, cast, and keywords, to provide users with movie recommendations that align with their interests. The system utilizes the concept of cosine similarity to measure the similarity between movies based on their features and suggests similar movies to users.

## 🔡 Dataset:-
The system utilizes two datasets, tmdb_5000_movies.csv and tmdb_5000_credits.csv, containing information about movies, cast, crew, genres, keywords, and more. The data is cleaned and processed to create a consolidated dataset that forms the basis for recommendation.

## 🎰 Model Building:-
* Data Merging: The two datasets are merged to create a comprehensive dataset containing relevant movie information.

* Feature Extraction: Key features such as genres, cast, keywords, and crew are extracted from the dataset and preprocessed for further analysis.

* Vectorization: Features are transformed into a numerical representation using the CountVectorizer technique, creating a vector space that represents each movie.

* Cosine Similarity: Cosine similarity is calculated between movies' vector representations to measure their similarity, forming the basis for recommendation.

## Usage:-
* Data Setup: Ensure you have the tmdb_5000_movies.csv and tmdb_5000_credits.csv datasets.

* Data Processing: The provided Jupyter Notebook demonstrates data processing steps, including feature extraction and vectorization.

* Model Building: Follow the notebook to build the recommendation model using cosine similarity.

* Recommendation: Utilize the built model to recommend movies. Input a movie title, and the system will suggest similar movies based on the movie's features.

## File Descriptions:-
* tmdb_5000_movies.csv: Movie dataset containing information about movies.
* tmdb_5000_credits.csv: Movie dataset containing cast and crew information.
* Movie_Recommendation_System.ipynb: Jupyter Notebook showcasing the entire workflow of building the recommendation system.
* movie_list.pkl: Pickle file containing preprocessed movie data for recommendation.
* movie_dict.pkl: Pickle file containing a dictionary representation of the movie data.
*similarity.pkl: Pickle file containing the cosine similarity matrix between movies.


Feel free to contact us at sk7733844929@gmail.com for any questions or feedback! We hope you enjoy using the Movie Recommendation System.
