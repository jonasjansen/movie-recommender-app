from flask import Flask, jsonify, request
import json
import pandas as pd
import numpy as np
import random
from calculation import recommend_by_genre, recommend_by_ratings
from movie_object_builder import convert_ids_to_objects

app = Flask(__name__)

similarity_matrix = np.load('data/similarity_matrix.npy')
rating_matrix = pd.read_csv('data/rating_matrix.csv', index_col=0)
rating_matrix.columns = rating_matrix.columns.map(int)
exploded_movies = pd.read_csv('data/exploded_movies.csv', index_col=0)
popular_movies_ids = exploded_movies[exploded_movies['hybrid_score']
                                     > 0.3]['movie_id'].unique().tolist()
genres = exploded_movies['genre'].unique().tolist()
genre_recommendations = {}


@app.route('/movie/genres')
def get_all_genres():
    return jsonify(genres)


@app.route('/movie/sample')
def get_random_movies():
    # We sample movies that have a hybrid score above a threshold because they have better chances that the user watched them
    movie_ids = random.sample(popular_movies_ids, 20)
    movie_list = convert_ids_to_objects(movie_ids, exploded_movies)
    return json.dumps(movie_list)


@app.route('/recommendation/by_genre/<selected_genre>')
def get_recommendation_by_genre(selected_genre):
    if selected_genre in genre_recommendations:
        recommendations = genre_recommendations[selected_genre]
    else:
        recommendations = recommend_by_genre(exploded_movies, selected_genre)
        genre_recommendations[selected_genre] = recommendations

    movie_ids = recommendations.tolist()
    movie_list = convert_ids_to_objects(movie_ids, exploded_movies)
    return json.dumps(movie_list)


@app.route('/recommendation/by_rating', methods=['POST'])
def get_recommendation_by_rating():
    user_ratings = request.get_json().get('rated_movies', [])

    new_ratings = pd.Series(index=rating_matrix.columns)
    for user_rating in user_ratings:
        if user_rating['rating'] > 0:
            new_ratings[user_rating['id']] = user_rating['rating']

    movie_ids = recommend_by_ratings(
        new_ratings.values, similarity_matrix, rating_matrix, exploded_movies)

    movie_list = convert_ids_to_objects(movie_ids, exploded_movies)
    return json.dumps(movie_list)


if __name__ == '__main__':
    app.run(debug=True)
