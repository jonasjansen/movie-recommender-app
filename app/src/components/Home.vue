<!-- Home.vue -->
<template>
  <div class="content">
    <div class="container">
      <h1 class="header">Welcome to the Movie Recommender App!</h1>

      <div class="text">

        <p>
          This app will help you find movies to watch based on your preferences.
          The app gives your recommendations based either on your preferred genre
          or you can rate movies you've seen and the app will recommend movies based on your ratings.
        </p>

        <p>
          To get started, click on one of the links in the sidebar on the left.
        </p>

        <p>
          Have fun!
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  // Add any component-specific logic here
};
</script>

<style scoped>
.content {
  color: white;
}

.container {
  border: 1px solid darkgray;
  border-radius: 5px;
  background-color: #0f000f;
  margin: 0 auto;
  max-width: 800px;
  padding: 20px;
}

.header {
  font-size: 2rem;
  text-align: center;
  margin-bottom: 36px;
}

.text {
  border-top: 1px solid darkgray;
  padding-top: 20px;
  margin-top: 20px;
  padding-right: 10px;
  padding-left: 10px;
  font-size: 1.3rem;
  line-height: 2rem;
  text-align: justify;

}
</style>
