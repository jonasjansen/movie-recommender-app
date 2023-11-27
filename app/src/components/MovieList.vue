<template>
  <div class="movie-section">
    <h2>Top 10 Movies</h2>
    <div class="movie-card" v-for="(movie, index) in movieList" :key="index">
      <img :src="getMovieImage(index)" alt="Movie Image" />
      <div class="movie-details">
        <p class="movie-rank">Rank {{ index + 1 }}</p>
        <p class="movie-name">{{ movie }}</p>
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
  },
};
</script>

<style>
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
