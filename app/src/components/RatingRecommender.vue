<template>
  <div>
    <!-- List of movies to rate -->
    <div :class="['accordion']">
      <button class="header" @click="toggleShowRating">
        <span class="text">Rate Movies</span>
        <span class="toggle">{{ showRating ? '↑' : '↓' }}</span>
      </button>
      <transition name="accordion" @before-enter="beforeEnter" @enter="enter" @before-leave="beforeLeave" @leave="leave">
        <div class="content" v-show="showRating">
          <movie-list :movies="moviesToRate" :showRating="true" @rating-updated="updateRating"/>
        </div>
      </transition>
    </div>


    <!-- Add a button to send the ratings to the API -->
    <button class="rating-action" @click="sendRatingsToApi">Get Movie Recommendations</button>

    <!-- List of recommended movies -->
      <div :class="['accordion']">
      <button class="header" @click="toggleShowRecommendation">
        <span class="text">Your recommendations</span>
        <span class="toggle">{{ showRecommendation ? '↑' : '↓' }}</span>
      </button>
      <transition name="accordion" @before-enter="beforeEnter" @enter="enter" @before-leave="beforeLeave" @leave="leave">
        <div class="content" v-show="showRecommendation">
          <movie-list :movies="moviesRecommended" :showRating="true" @rating-updated="updateRating"/>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import MovieList from "./MovieList.vue";

export default {
  components: {
    MovieList,
  },
  data() {
    return {
      moviesToRate: [],
      moviesRecommended: [],
      showRating: true,
      showRecommendation: false,
    };
  },
  created() {
    this.fetchMovieSample();
  },
  methods: {
    beforeEnter(el) {
      el.style.height = '0';
    },
    enter(el) {
      el.style.height = el.scrollHeight + 'px';
    },
    beforeLeave(el) {
      el.style.height = el.scrollHeight + 'px';
    },
    leave(el) {
      el.style.height = '0';
    },
    toggleShowRating() {
      this.showRating = !this.showRating;
    },
    toggleShowRecommendation() {
      this.showRecommendation = !this.showRecommendation;
    },
    async fetchMovieSample() {
      try {
        console.log('Get sample movies from API.')
        const response = await axios.get('/api/movie/sample');

        console.log("Result from API:", response.data);
        this.moviesToRate = response.data;

      } catch (error) {
        console.error('Error fetching genres:', error);
      }
    },
    updateRating({index, stars}) {
      console.log("UpdateRating", index, stars)
      this.moviesToRate[index].rating = stars;
    },
    async sendRatingsToApi() {
      this.isExpandedRecommendation = true;

      try {
        console.log("Sending ratings to the API:", this.moviesToRate);

        const ratingsData = this.moviesToRate.map(({id, rating}) => ({id, rating}));
        const response = await axios.post('/api/recommendation/by_rating', {rated_movies: ratingsData});

        console.log("Result from API:", response.data);
        this.moviesRecommended = response.data;


      } catch (error) {
        console.error('Error fetching movie ranking:');
      }
    },
  },
};
</script>

<style>
.rating-action {
  color: #fff;
  display: block;
  padding: 18px 50px;
  margin: 20px auto;
  text-decoration: none;
  background-color: #5252a6;
  border-radius: 5px;
  border: 1px solid darkgray;
  line-height: 2rem;
  font-size: 1.3rem;
  text-align: center;
  cursor: pointer;
  width: 100%;
}

.accordion {
  background-color: #1c1b23;
  border-radius: 5px;
  border: 1px solid darkgray;
  padding: 10px;
}

.accordion .header {
  background-color: #1c1b23;
  color: #fff;
  cursor: pointer;
  padding: 10px 10px;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
  width: 100%;
}

.accordion .header .text {
  font-weight: 500;
  font-size: 1.3rem;
}

.accordion .header .toggle {
  font-size: 1.5rem;
  float: right;
  margin-left: 20px;
  margin-right: 10px
}

.accordion .content {
  overflow: hidden;
  border-top: 0;
  border-bottom-left-radius: 6px;
  border-bottom-right-radius: 6px;
  transition: 300ms ease-out;
}

</style>
