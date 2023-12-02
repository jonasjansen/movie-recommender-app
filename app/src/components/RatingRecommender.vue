<template>
  <div>
    <h2>Rate Movies</h2>
    <rating-list :movies="moviesToRate" @rating-updated="updateRating"/>
    <h2>Recommendations</h2>
    <movie-list :movie-list="moviesToRecommend"/>
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
      moviesToRecommend: [],
    };
  },
  created() {
    this.fetchMovieSample();
  },
  methods: {
    async fetchMovieSample() {
      try {
        const response = await axios.get('/api/movie/sample');
        console.log('Movie sample:', response.data)
        this.moviesToRate = response.data;
        this.moviesToRecommend = response.data;
      } catch (error) {
        console.error('Error fetching genres:', error);
      }
    },
    updateRating({ index, stars }) {
      console.log("DEBUG: updateRating", index, stars)
      // Update the ratings in the parent component
      this.moviesToRate[index].rating = stars;

      // Now, you can send the updated ratings to your API or perform any other desired actions
      //this.sendRatingsToApi();
    },
    async sendRatingsToApi() {
      try {
        console.log("Sending ratings to the API:", this.movies);

        // Extract only necessary data (movie ID and rating) to send to the API
        const ratingsData = this.items.map(({ title, currentRating }) => ({ title, currentRating }));


        // Implement your logic to send ratings to the API
        const response = await axios.post('/api/recommendation/by_rating', { rated_movies: ratingsData});

        console.log("Result from API:", response.data);
      } catch (error) {
        //console.error('Error fetching movie ranking:', error);
        console.error('Error fetching movie ranking:');
      }
    },
  },
};
</script>

<style>
/* Styles remain the same */
</style>
