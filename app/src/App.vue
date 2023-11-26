<!-- App.vue -->
<template>
  <div id="app">
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
};
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
