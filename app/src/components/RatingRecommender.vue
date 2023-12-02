<template>
  <div>
    <!-- List of movies to rate -->
    <h2>Rate Movies</h2>
    <rating-list :movies="moviesToRate" @rating-updated="updateRating"/>

    <!-- Add a button to send the ratings to the API -->
    <button @click="sendRatingsToApi">Send Ratings to API</button>

    <!-- List of recommended movies -->
    <h2>Recommendations</h2>
    <movie-list :movies="moviesRecommended"/>
  </div>
</template>

<script>
import axios from 'axios';
import RatingList from './RatingList.vue';
import MovieList from "./MovieList.vue";

export default {
  components: {
    MovieList,
    RatingList,
  },
  data() {
    return {
      moviesToRate: [],
      moviesRecommended: [],
    };
  },
  created() {
    this.fetchMovieSample();
  },
  methods: {
    async fetchMovieSample() {
      try {
        console.log('Get sample movies from API.')
        const response = await axios.get('/api/movie/sample');

        console.log("Result from API:", response.data);
        this.moviesToRate = response.data;

      } catch (error) {
        console.error('Error fetching genres:', error);
      }
    },
    updateRating({ index, stars }) {
      console.log("UpdateRating", index, stars)
      this.moviesToRate[index].rating = stars;
    },
    async sendRatingsToApi() {
      try {
        console.log("Sending ratings to the API:", this.moviesToRate);

        const ratingsData = this.moviesToRate.map(({ id, rating }) => ({ id, rating }));
        const response = await axios.post('/api/recommendation/by_rating', { rated_movies: ratingsData});

        console.log("Result from API:", response.data);
        this.moviesRecommended = response.data;



      } catch (error) {
        console.error('Error fetching movie ranking:');
      }
    },
  },
};
</script>

<style>
/* Styles remain the same */
</style>
