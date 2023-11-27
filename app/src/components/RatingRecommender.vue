<template>
  <div>
    <h2>Top 10 Rated Movies</h2>

    <movie-list :movie-list="ratedMovieList" />
  </div>
</template>

<script>
import axios from 'axios';
import MovieList from './MovieList.vue';

export default {
  components: {
    MovieList,
  },
  data() {
    return {
      // Assuming you have some mechanism to fetch rated movies
      ratedMovieList: [], // Update this with actual data
    };
  },
  created() {
    // Fetch the list of top-rated movies
    this.fetchTopRatedMovies();
  },
  methods: {
    async fetchTopRatedMovies() {
      try {
        const response = await axios.post('/api/recommendation_by_rating', {
          // Pass your list of rated movies or any other necessary data
        });
        this.ratedMovieList = response.data;
      } catch (error) {
        console.error('Error fetching top-rated movies:', error);
      }
    },
  },
};
</script>

<style>
/* Styles remain the same */
</style>
