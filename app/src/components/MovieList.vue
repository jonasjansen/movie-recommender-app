<template>
  <div class="movie-list">
    <div v-for="(movie, index) in movies" :key="index" class="movie-card">
      <div class="movie-content">

        <!-- rank -->
        <div v-if="showRank" class="rank">
          <span class="rank-number">{{ index + 1 }}</span>
        </div>

        <!-- image -->
        <img :src="movie.image" alt="Movie Image" class="movie-image"/>

        <!-- rating -->
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

        <!-- title -->
        <p class="movie-title">{{ movie.title }}</p>

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
    showRank: {
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
  padding: 20px 10px 10px 10px;
  margin-top: 10px;
  border-top: 1px solid darkgray;
}

.movie-card {
  flex: 0 0 19%;
  margin-bottom: 10px;
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
  font-size: 1rem;
  margin-top: 10px;
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

.rank {
  margin-bottom: 10px;
}
.rank-number {
  color: #fff;
  font-weight: 500;
  background-color: #5252a6;
  border-radius: 50%;
  padding: 5px 10px;
  margin-top: 10px;
  display: inline-block;
}
</style>

