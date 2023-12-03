<template>
  <div>
    <!-- List of movies to rate -->
    <div class="container">

      <button @click="toggleExpansionRating" class="accordion">
        <span class="text">Rate Movies</span>
        <span class="toggle">{{ isExpandedRating ? '↑' : '↓' }}</span>
      </button>

      <div class="accordion-content" :class="{ 'expanded': isExpandedRating, 'collapsed': !isExpandedRating }">
        <movie-list v-if="isExpandedRating" :movies="moviesToRate" :showRating="true" @rating-updated="updateRating"/>
      </div>

    </div>

    <!-- Add a button to send the ratings to the API -->
    <button class="rating-action" @click="sendRatingsToApi">Send Ratings to API</button>

    <!-- List of recommended movies -->
    <div class="container">

      <button @click="toggleExpansionRecommendation" class="accordion">
        <span class="text">Your recommendations</span>
        <span class="toggle">{{ isExpandedRecommendation ? '↑' : '↓' }}</span>
      </button>

      <div class="accordion-content" :class="{ 'expanded': isExpandedRecommendation, 'collapsed': !isExpandedRecommendation }">
          <movie-list v-if="isExpandedRecommendation" :movies="moviesRecommended" :showRating="false" @rating-updated="updateRating"/>
      </div>
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
      isExpandedRating: true,
      isExpandedRecommendation: false,
    };
  },
  created() {
    this.fetchMovieSample();
  },
  methods: {
    toggleExpansionRating() {
      this.isExpandedRating = !this.isExpandedRating;
    },
    toggleExpansionRecommendation() {
      this.isExpandedRecommendation = !this.isExpandedRecommendation;
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
.container {
  background-color: #1c1b23;
  border-radius: 5px;
  border: 1px solid darkgray;
  padding: 10px;
}

.accordion {
  background-color: #1c1b23;
  color: #fff;
  cursor: pointer;
  padding: 10px 10px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.accordion .text {
  font-weight: 500;
  font-size: 1.3rem;
}

.accordion .toggle {
  font-size: 1.5rem;
  float: right;
  margin-left: 20px;
  margin-right: 10px
}

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

.accordion-content {
  overflow: hidden;
  transition: max-height 1s ease-out;
}

.collapsed{
  max-height: 0;
}
.expanded {
  max-height: 2000px;
}


</style>
