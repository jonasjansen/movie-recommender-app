<template>
  <div>
    <h1>Recommender by Rating</h1>

    <button @click="getMovieData">Get API Data</button>

    <div v-if="movieData">
      <p>{{ movieData }}</p>
    </div>

    <div v-if="error">
      <p>Error fetching movie data: {{ error }}</p>
    </div>

  </div>

</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      movieData: null,
      error: null
    };
  },
  methods: {
    getMovieData() {
      // Make a GET request to the /movie endpoint
      axios.get('/api')
          .then(response => {
            // Handle successful response
            this.movieData = response.data;
            this.error = null;
          })
          .catch(error => {
            // Handle error
            this.error = error.message;
            this.movieData = null;
          });
    }
  }
}

</script>

<style scoped>

</style>