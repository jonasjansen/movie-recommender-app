<template>
  <div class="main">
    <div class="sidebar">
      <router-link to="/" class="logo-link">
        <div class="logo">
          <div>Movie</div>
          <div>Recommender</div>
        </div>
      </router-link>
      <router-link to="/genre" class="menu-item" :class="{ active: currentRoute === '/genre' }">By Genre</router-link>
      <router-link to="/rating" class="menu-item" :class="{ active: currentRoute === '/rating' }">By Rating</router-link>
      <div v-if="currentRoute === '/genre'" class="instructions">
        Please choose your preferred genre. Your new movie recommendations will be shown below.
      </div>
      <div v-if="currentRoute === '/rating'" class="instructions">
       Please rate as many movies as possible. Then click on the Link "Get Movie Recommendations". Your new movie recommendations will be shown below.
      </div>
    </div>
    <div class="main-content">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentRoute: "/genre", // Set the default route
    };
  },
  watch: {
    $route(to) {
      this.currentRoute = to.path;
    },
  },
};
</script>

<style>
@font-face {
  font-family: 'Forque';
  src: url('/fonts/forque.ttf') format('truetype');
}

.logo {
  font-family: 'Forque', sans-serif;
  font-size: 3rem;
  color: #fff;
  text-align: center;
  padding-bottom: 20px;
  border-bottom: 1px solid darkgray;
  margin-bottom: 30px;
  text-decoration: None;
}

.logo-link {
  text-decoration: None;
}

.instructions {
  margin-top: 40px;
  padding-top: 30px;
  border-top: 1px solid darkgray;
  color: #fff;
  font-size: 1rem;
  line-height: 1.5rem;
    text-align: justify;
}

body {
  margin: 0;
  padding: 0;
}

.main {
  display: flex;
  margin: 0;
  padding: 0;
  height: 100vh;
  background-color: #1c1b23;
  font-family: Noto Sans, Noto Sans HK, Noto Sans JP, Noto Sans KR, Noto Sans SC, Noto Sans TC, sans-serif;
}

.sidebar {
  width: 250px;
  padding: 25px;
  background-color: #0f000f;
  position: sticky;
  top: 0;
}

.main-content {
  flex: 1;
  padding: 25px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}


.menu-item {
  color: #fff;
  display: block;
  padding: 10px;
  margin-bottom: 30px;
  text-decoration: none;
  background-color: #1c1b23;
  border-radius: 5px;
  border: 1px solid darkgray;
  line-height: 2rem;
  font-size: 1.3rem;
  text-align: center;
}

.menu-item:hover,
.menu-item.active {
  background-color: #5252a6;
}


</style>
