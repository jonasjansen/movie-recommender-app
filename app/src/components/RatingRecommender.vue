<template>
  <div>
    <h2>Top 10 Rated Movies</h2>
    <star-rating :items="items" @rating-updated="updateRating" />
  </div>
</template>

<script>
import axios from 'axios';
import MovieRatingList from './MovieRatingList.vue';
import StarRating from './StarRating.vue';

export default {
  components: {
    StarRating,
  },
  data() {
    return {
      items: [
        { title: 'Item 1', image: 'https://placekitten.com/200/300', currentRating: 2 },
        { title: 'Item 2', image: 'https://placekitten.com/200/300', currentRating: 0 },
        { title: 'Item 3', image: 'https://placekitten.com/200/300', currentRating: 0 },
        { title: 'Item 4', image: 'https://placekitten.com/200/300', currentRating: 0 },
        { title: 'Item 5', image: 'https://placekitten.com/200/300', currentRating: 0 },
        { title: 'Item 6', image: 'https://placekitten.com/200/300', currentRating: 0 },
        { title: 'Item 7', image: 'https://placekitten.com/200/300', currentRating: 0 },
        { title: 'Item 8', image: 'https://placekitten.com/200/300', currentRating: 0 },
        { title: 'Item 9', image: 'https://placekitten.com/200/300', currentRating: 0 },
        { title: 'Item 10', image: 'https://placekitten.com/200/300', currentRating: 0 },
        // Add more items as needed, up to a maximum of 10
      ],
    };
  },
  methods: {
    updateRating({ index, stars }) {
      // Update the ratings in the parent component
      this.items[index].currentRating = stars;

      // Now, you can send the updated ratings to your API or perform any other desired actions
      this.sendRatingsToApi();
    },
    async sendRatingsToApi() {
      try {
        console.log("Sending ratings to the API:", this.items);

        // Extract only necessary data (movie ID and rating) to send to the API
        const ratingsData = this.items.map(({ title, currentRating }) => ({ title, currentRating }));


        // Implement your logic to send ratings to the API
        const response = await axios.post('/api/recommendation/by_rating', { rated_movies: ratingsData});

        console.log("Result from API:", response.data);

        // TODO: Show result as list.
      } catch (error) {
        //console.error('Error fetching movie ranking:', error);
        console.error('Error fetching movie ranking:');
      }


    },
  },
};
</script>

<style>
/* Styles remain the same */
</style>
