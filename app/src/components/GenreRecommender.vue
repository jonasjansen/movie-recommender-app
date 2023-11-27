<template>
  <div>
    <div class="genre-section">
      <h2>Select Genre</h2>
      <select v-model="selectedGenre">
        <option value="">-- Select Genre --</option>
        <option v-for="genre in genres" :key="genre" :value="genre">{{ genre }}</option>
      </select>
    </div>

    <div class="movie-section" v-if="selectedGenre">
      <h2>Top 10 Movies</h2>
      <div class="movie-card" v-for="(movie, index) in movieList" :key="index">
        <img :src="getMovieImage(index)" alt="Movie Image" />
        <div class="movie-details">
          <p class="movie-rank">Rank {{ index + 1 }}</p>
          <p class="movie-name">{{ movie }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedGenre: '',
      genres: [], // To store the list of genres
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
          this.movieList = response.data;
        } catch (error) {
          console.error('Error fetching genre ranking:', error);
        }
      }
    },
    getMovieImage(index) {
      // Replace this with the actual image URL for each movie
      // Dummy data for illustration
      return `https://via.placeholder.com/150?text=Movie${index + 1}`;
    },
  },
};
</script>

<style>
.genre-section {
  margin-bottom: 20px;
}

.movie-section {
  margin-top: 20px;
  display: flex;
  flex-wrap: wrap;
}

.movie-card {
  flex: 1 1 calc(20% - 20px); /* Set each card to take up 20% of the container width with a margin */
  margin: 10px;
  display: flex;
  flex-direction: column;
  border: 1px solid #ddd;
  padding: 10px;
}

.movie-card img {
  width: 100%;
  height: auto;
  margin-bottom: 10px;
}

.movie-details {
  flex: 1;
}

.movie-rank {
  font-weight: bold;
}

.movie-name {
  margin-top: 5px;
}
</style>

