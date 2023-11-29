<template>
  <div class="star-ratings">
    <div v-for="(item, index) in items" :key="index" class="star-rating">
      <img :src="item.image" alt="Item Image" class="item-image" />
      <h2>{{ item.title }}</h2>
      <div class="rating">
        <span
            v-for="star in 5"
            :key="star"
            @click="rate(index, star)"
            @mouseover="hover(index, star)"
            @mouseout="clearHover"
            :class="{
              'gold': star <= item.currentRating || (star <= hoverRating && hoverIndex === index),
              'black' : true
            }"
        >
          &#9733;
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    items: {
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
      this.$emit('rating-updated', { index, stars });
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
.star-ratings {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.star-rating {
  text-align: center;
  margin: 20px;
  flex-basis: calc(20% - 40px); /* 5 items per row with margin */
}

.item-image {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
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

