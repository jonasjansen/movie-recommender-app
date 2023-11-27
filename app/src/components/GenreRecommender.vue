<template>
  <div>
    <div class="genre-section">
      <h2>Select Genre</h2>
      <select v-model="selectedGenre">
        <option value="">-- Select Genre --</option>
        <option value="action">Action</option>
        <option value="comedy">Comedy</option>
        <!-- Add more genres as needed -->
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
export default {
  data() {
    return {
      selectedGenre: '',
      movieList: [], // Placeholder for movie list
    };
  },
  watch: {
    selectedGenre() {
      // Replace this with an API call to fetch movies based on the selected genre
      // For now, using dummy data
      this.fetchMovies();
    },
  },
  methods: {
    fetchMovies() {
      // Replace this with an API call to fetch movies based on the selected genre
      // Dummy data for illustration
      const dummyMovies = ['Movie 1', 'Movie 2', 'Movie 3', 'Movie 4', 'Movie 5', 'Movie 6', 'Movie 7', 'Movie 8', 'Movie 9', 'Movie 10'];
      this.movieList = dummyMovies;
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

