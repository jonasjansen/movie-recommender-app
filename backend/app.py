from flask import Flask, jsonify

app = Flask(__name__)

# Example data for illustration
movie_data = [
    {"title": "Movie 1", "genre": "action", "rating": 4.5},
    {"title": "Movie 2", "genre": "action", "rating": 3.8},
    # Add more movie data as needed
]

@app.route('/movies/genres')
def get_all_genres():
    # Logic to fetch and return all available genres
    genres = ["action", "comedy", "drama", "sci-fi", "horror"]
    return jsonify(genres)

@app.route('/movies/sample')
def get_random_movies():
    # Logic to fetch and return a random sample of movies
    # Replace this with your actual implementation
    return jsonify(movie_data)

@app.route('/recommendation/by_genre/<selected_genre>')
def get_recommendation_by_genre(selected_genre):
    # Logic to fetch and return a recommendation based on the given genre
    # Replace this with your actual implementation
    genre_recommendation = [movie for movie in movie_data if movie['genre'] == selected_genre]
    genre_recommendation = sorted(genre_recommendation, key=lambda x: x['rating'], reverse=True)[:10]
    return jsonify(genre_recommendation)

@app.route('/recommendation/by_rating', methods=['POST'])
def get_recommendation_by_rating():
    # Logic to fetch and return a recommendation based on the list of rated movies
    # Replace this with your actual implementation
    # Example: You might expect a JSON payload with a list of rated movies
    rated_movies = request.get_json().get('rated_movies', [])

    # Dummy logic to recommend movies based on ratings
    rated_movies_recommendation = sorted(movie_data, key=lambda x: x['rating'], reverse=True)[:10]
    return jsonify(rated_movies_recommendation)

if __name__ == '__main__':
    app.run(debug=True)
