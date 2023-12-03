<template>
  <div>
    <div class="genre-section">
      <h2>Select Genre</h2>
      <select v-model="selectedGenre" @change="fetchGenreRanking">
        <option value="">-- Select Genre --</option>
        <option v-for="genre in genres" :key="genre" :value="genre">{{ genre }}</option>
      </select>
    </div>

    <!-- List of recommended movies -->
    <div :class="['accordion']">
      <button class="header">
        <span class="text">Your recommendations</span>
      </button>
      <transition name="accordion" >
        <div class="content" >
          <movie-list v-if="movies.length > 0" :movies="movies" :show-rank="false"/>
          <div class="message" v-else>
            No recommended movies available. Please rate movies and click on "Get Movie Recommendations" again.
          </div>
        </div>
      </transition>
    </div>
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
      selectedGenre: '',
      genres: [],
      movies: [],
    };
  },
  created() {
    // Fetch the list of genres when the component is created
    this.fetchGenres();
  },
  watch: {
    selectedGenre() {
      // Fetch the genre ranking when the selected genre changes
      this.fetchGenreRanking();
    },
  },
  methods: {
    async fetchGenres() {
      try {
        const response = await axios.get('/api/movie/genres');
        this.genres = response.data;
      } catch (error) {
        console.error('Error fetching genres:', error);
      }
    },
    async fetchGenreRanking() {
      // Fetch the genre ranking based on the selected genre
      if (this.selectedGenre) {
        try {
          const response = await axios.get(`/api/recommendation/by_genre/${this.selectedGenre}`);
          console.log('Genre ranking:', response.data)
          this.movies = response.data;
        } catch (error) {
          console.error('Error fetching genre ranking:', error);
        }
      }
    },
  },
};
</script>

<style>
.genre-section {
  margin-bottom: 20px;
}
</style>
