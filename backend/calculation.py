import numpy as np


def recommend_by_genre(exploded_movies, genre):
    """
    Recommends movies based on genre.
    :param exploded_movies: DataFrame containing movie data
    :param genre: Genre to filter movies
    :return: List of recommended movie IDs
    """
    return exploded_movies[exploded_movies['genre'] == genre].nlargest(
        10, 'hybrid_score')['movie_id'].values


def recommend_by_ratings(new_ratings, similarity_matrix, rating_matrix, exploded_movies):
    """
    Recommends movies based on user ratings.
    :param new_ratings: New user ratings
    :param similarity_matrix: Matrix containing similarity values between movies
    :param rating_matrix: Matrix containing movie ratings
    :param exploded_movies: DataFrame containing movie data
    :return: List of recommended movie names
    """
    unrated_indices = np.where(np.isnan(new_ratings))[0]
    rated_indices = np.where(~np.isnan(new_ratings))[0]

    predictions = []
    for l in unrated_indices:
        neighborhood = np.intersect1d(
            np.where(~np.isnan(similarity_matrix[l, :])), rated_indices)
        numerator = np.dot(
            similarity_matrix[l, neighborhood], new_ratings[neighborhood])
        denominator = np.sum(similarity_matrix[l, neighborhood])

        if denominator != 0:
            prediction = numerator / denominator
            predictions.append((l, prediction))

    predictions.sort(key=lambda x: x[1], reverse=True)
    top_10_recommendations = [
        movie for movie, prediction in predictions[:10] if not np.isnan(prediction)]
    top_10_recommendations = rating_matrix.columns[top_10_recommendations].values.tolist(
    )

    if len(top_10_recommendations) < 10:
        genre_recommendations = complete_recommend_by_ratings(
            new_ratings, exploded_movies, rating_matrix)
        genre_recommendations = list(
            set(genre_recommendations) - set(top_10_recommendations))
        top_10_recommendations += genre_recommendations[:10 - len(
            top_10_recommendations)]

    return top_10_recommendations


def complete_recommend_by_ratings(new_ratings, exploded_movies, rating_matrix):
    """
    Completes recommendations based on ratings.
    :param new_ratings: New user ratings
    :param exploded_movies: DataFrame containing movie data
    :param rating_matrix: Matrix containing movie ratings
    :return: List of recommended movie IDs
    """
    exploded_movies = exploded_movies.drop_duplicates(
        subset='movie_id', keep='last')
    try:
        highest_rated_movie_id = rating_matrix.columns[np.nanargmax(
            new_ratings)]
        genre_of_highest_rated_movie = exploded_movies.loc[exploded_movies['movie_id']
                                                           == highest_rated_movie_id, 'genre'].values[0]
        movies_same_genre = exploded_movies[exploded_movies['genre']
                                            == genre_of_highest_rated_movie]
        rated_indices = np.where(~np.isnan(new_ratings))[0]
        rated_movie_ids = rating_matrix.columns[rated_indices].values
        movies_same_genre = movies_same_genre[~movies_same_genre['movie_id'].isin(
            rated_movie_ids)]
        return movies_same_genre.nlargest(10, 'hybrid_score')['movie_id'].tolist()

    except (ValueError, IndexError):
        return exploded_movies.nlargest(10, 'hybrid_score')['movie_id'].tolist()
