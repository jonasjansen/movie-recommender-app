from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
import random
from math import recommend_by_genre, recommend_by_ratings


app = Flask(__name__)

similarity_matrix = np.load('similarity_matrix.npy')
rating_matrix = pd.read_csv('rating_matrix.csv')
exploded_movies = pd.read_csv('exploded_movies.csv')
popular_movies_ids = exploded_movies[exploded_movies['hybrid_score']
                                     > 0.3]['movie_id'].unique().tolist()
genres = exploded_movies['genre'].unique().tolist()
genre_recommendations = {}

# Example data for illustration
movie_data = [
    {"title": "Movie 1", "genre": "action", "rating": 4.5},
    {"title": "Movie 2", "genre": "action", "rating": 3.8},
    # Add more movie data as needed
]


@app.route('/movie/genres')
def get_all_genres():
    return jsonify(genres)


@app.route('/movie/sample')
def get_random_movies():
    # We sample movies that have a hybrid score above a threshold because they have better chances that the user watched them
    return jsonify(random.sample(popular_movies_ids, 20))


@app.route('/recommendation/by_genre/<selected_genre>')
def get_recommendation_by_genre(selected_genre):
    if selected_genre in genre_recommendations:
        recommendations = genre_recommendations[selected_genre]
    else:
        recommendations = recommend_by_genre(exploded_movies, selected_genre)
        genre_recommendations[selected_genre] = recommendations

    return jsonify(recommendations)


@app.route('/recommendation/by_rating', methods=['POST'])
def get_recommendation_by_rating():
    # TODO: Proper process the post data.
    # TODO: Find out how to debug this.

    # new_ratings = request.json['new_ratings']
    new_ratings = request.get_json().get('rated_movies', [])
    return jsonify(recommend_by_ratings(new_ratings, similarity_matrix, rating_matrix, exploded_movies))


if __name__ == '__main__':
    app.run(debug=True)
