<template>
  <div>
    <div class="genre-section">
      <h2>Select Genre</h2>
      <select v-model="selectedGenre" @change="fetchGenreRanking">
        <option value="">-- Select Genre --</option>
        <option v-for="genre in genres" :key="genre" :value="genre">{{ genre }}</option>
      </select>
    </div>

    <h2>Recommendations</h2>
    <movie-list v-if="selectedGenre" :movie-list="movieList" />
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
      movieList: [],
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
          this.movieList = response.data;
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
