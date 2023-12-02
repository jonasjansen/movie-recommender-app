<template>
  <div class="movie-list">
    <div v-for="(movie, index) in movies" :key="index" class="movie-card">
      <div class="movie-content">
        <img :src="movie.image" alt="Movie Image" class="movie-image" />
        <h2 class="movie-title">{{ movie.title }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    movies: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style>
.movie-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.movie-card {
  flex: 0 0 19%;
  margin-bottom: 20px; /* Adjust as needed */
}

.movie-content {
  width: 100%;
  text-align: center;
}

.movie-image {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  border: 1px solid darkgray;
}

.movie-title {
  color: rgba(255, 255, 255, 0.8);
  font-size: 1rem;
}

@media screen and (max-width: 1200px) {
  .movie-card {
    flex: 0 0 24%;
  }
}

@media screen and (max-width: 992px) {
  .movie-card {
    flex: 0 0 32%;
  }
}

@media screen and (max-width: 768px) {
  .movie-card {
    flex: 0 0 48%;
  }
}

@media screen and (max-width: 576px) {
  .movie-card {
    flex: 0 0 100%;
  }
}
</style>
