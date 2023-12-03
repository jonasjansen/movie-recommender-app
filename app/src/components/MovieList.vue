<template>
  <div class="movie-list">
    <div v-for="(movie, index) in movies" :key="index" class="movie-card">
      <div class="movie-content">
        <img :src="movie.image" alt="Movie Image" class="movie-image"/>
        <p class="movie-title">{{ movie.title }}</p>
        <div v-if="showRating" class="rating">
        <span
            v-for="star in 5"
            :key="star"
            @click="rate(index, star)"
            @mouseover="hover(index, star)"
            @mouseout="clearHover"
            :class="{
              'gold': star <= movie.rating || (star <= hoverRating && hoverIndex === index),
              'black' : true
            }"
        >
          &#9733;
        </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    showRating: {
      type: Boolean,
      default: false
    },
    movies: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      hoverRating: 0,
      hoverIndex: -1,
    };
  },
  methods: {
    rate(index, stars) {
      this.$emit('rating-updated', {index, stars});
    },
    hover(index, stars) {
      this.hoverRating = stars;
      this.hoverIndex = index;
    },
    clearHover() {
      this.hoverRating = 0;
      this.hoverIndex = -1;
    },
  },
};
</script>

<style scoped>
.movie-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  //background-color: #1c1b23;
  padding: 20px 10px;
}

.movie-card {
  flex: 0 0 19%;
  margin-bottom: 20px; /* Adjust as needed */
}

.movie-content {
  width: 100%;
  max-width: 185px;
  text-align: center;
  margin: 0 auto;
}

.movie-image {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  border: 1px solid darkgray;
}

.movie-title {
  text-align: center;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
  font-size: 2rem;
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

.rating {
  font-size: 24px;
  margin-top: 10px;
}

.gold {
  color: gold !important;
}

.black {
  color: #ccc; /* Color for empty star */
}

/* Hover effect */
.gold:hover,
.black:hover {
  cursor: pointer;
}
</style>

