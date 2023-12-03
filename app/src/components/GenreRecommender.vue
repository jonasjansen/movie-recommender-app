<template>
  <div>
    <div class="genre-section">
      <div class="label">Genre</div>

      <!-- Custom dropdown container -->
      <div class="custom-dropdown" @click="toggleDropdown">
        {{ selectedGenre || '-- Select --' }}
        <ul v-show="showDropdown">
          <li v-for="genre in genres" :key="genre" @click="selectGenre(genre)">
            {{ genre }}
          </li>
        </ul>
      </div>
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
      showDropdown: false,
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
    toggleDropdown() {
      console.log('Toggle dropdown')
      this.showDropdown = !this.showDropdown;
    },
    selectGenre(genre) {
      this.selectedGenre = genre;
      this.fetchGenreRanking(); // Call your fetchGenreRanking method here
    },
  },
};
</script>

<style scoped>

.accordion .header{
  pointer-events: none;
}
.label {
  margin-right: 15px;
}

.genre-section {
  display: flex;
  align-items: center;
  color: white;
  font-size: 1.3rem;
  padding: 6px 20px;
  background-color: #1c1b23;
  border: 1px solid darkgray;
  border-radius: 5px;
  margin-bottom: 20px;
}

.label {
  padding: 14px 25px 14px 0;
  border-right: 1px solid darkgray;
}

.custom-dropdown {
  margin-left: 10px;
  position: relative;
  cursor: pointer;
  padding: 14px 25px 14px 0;
  width: 100%;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  position: absolute;
  top: 42px;
  left: -26px;
  background-color: #000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border: 1px solid darkgray;
}

ul li {
  padding: 12px 26px;
  cursor: pointer;
}

ul li:hover {
  background-color: #5252a6;
}
</style>
