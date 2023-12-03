BASE_URL = 'https://liangfgithub.github.io/MovieImages/'


def convert_ids_to_objects(movie_ids, movie_data_source):
    movie_objects = []

    for movie_id in movie_ids:
        # Get line of movie data from the data source based on the movie_id
        movie_data = movie_data_source[movie_data_source['movie_id']
                                       == movie_id].iloc[0]

        image_url = ''.join([BASE_URL, str(movie_id), '.jpg'])
        movie_object = {
            'id': movie_id,
            'title': movie_data['title'],
            'image': image_url,
            'rating': 0
        }

        movie_objects.append(movie_object)

    return movie_objects
