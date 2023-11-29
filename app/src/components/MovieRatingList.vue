<template>
  <div class="movie-section">
    <h2>Top 10 Movies</h2>
    <div class="movie-card" v-for="(movie, index) in movieList" :key="index">
      <img :src="getMovieImage(index)" alt="Movie Image" />
      <div class="movie-details">
        <p class="movie-rank">Rank {{ index + 1 }}</p>
        <p class="movie-name">{{ movie.title }}</p>
        <div class="rating-stars">
          <span
              v-for="starIndex in 5"
              :key="starIndex"
              @click="rateMovie(index, starIndex)"
              :class="{ 'filled-star': starIndex <= movie.rating }"
          >
            ★
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    movieList: Array,
  },
  methods: {
    getMovieImage(index) {
      // Replace this with the actual image URL for each movie
      // Dummy data for illustration
      return `https://via.placeholder.com/150?text=Movie${index + 1}`;
    },
    rateMovie(movieIndex, rating) {
      // Update the rating of the clicked movie
      this.$emit('updateRating', movieIndex, rating);
    },
  },
};
</script>

<style>
/* Styles remain the same */
</style>
