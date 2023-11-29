<template>
  <div class="rated-movie-list">
    <h2>Rate Movies</h2>
    <div v-for="(movie, index) in movieList" :key="index" class="rated-movie-card">
      <img :src="movie.image" alt="Movie Image" />
      <div class="movie-details">
        <p class="movie-name">{{ movie.title }}</p>
        <div class="rating-stars">
          <span
              v-for="star in 5"
              :key="star"
              class="star"
              @click="rateMovie(index, star)"
          >
            <i :class="getStarClass(star, movie.rating)"></i>
          </span>
        </div>
      </div>
    </div>

    <button @click="submitRatings">Submit Ratings</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    movieList: Array,
  },
  methods: {
    rateMovie(movieIndex, rating) {
      // Update the rating for the clicked movie
      this.movieList = this.movieList.map((movie, index) =>
          index === movieIndex ? { ...movie, rating } : movie
      );
    },
    async submitRatings() {
      try {
        // Extract only necessary data (movie ID and rating) to send to the API
        const ratingsData = this.movieList.map(({ id, rating }) => ({ id, rating }));

        // Make API call to /recommendation/by_rating with the updated ratings
        const response = await axios.post('/api/recommendation_by_rating', { rated_movies: ratingsData });

        // Update the movie list with the new recommendations
        this.$emit('update-movie-list', response.data);
      } catch (error) {
        console.error('Error submitting ratings:', error);
      }
    },
    getStarClass(star, rating) {
      return star <= rating ? 'fas fa-star' : 'far fa-star';
    },
  },
};
</script>

<style>
.rated-movie-list {
  margin-top: 20px;
}

.rated-movie-card {
  display: flex;
  border: 1px solid #ddd;
  padding: 10px;
  margin-bottom: 10px;
}

.rated-movie-card img {
  width: 100px;
  height: 150px;
  margin-right: 10px;
}

.movie-details {
  flex: 1;
}

.movie-name {
  font-weight: bold;
  margin-bottom: 5px;
}

.rating-stars {
  margin-top: 5px;
}

.star {
  font-size: 20px;
  cursor: pointer;
}
</style>
