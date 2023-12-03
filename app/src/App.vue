<template>
  <div id="app">
    <div class="sidebar">
      <router-link to="/genre" class="menu-item" :class="{ active: currentRoute === '/genre' }">Recommender by Genre</router-link>
      <router-link to="/rating" class="menu-item" :class="{ active: currentRoute === '/rating' }">Recommender by Rating</router-link>
    </div>
    <div class="main-content">
      <router-view />
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
#app {
  display: flex;
  background-color: #0f000f;
  font-family: Noto Sans, Noto Sans HK, Noto Sans JP, Noto Sans KR, Noto Sans SC, Noto Sans TC, sans-serif;
}

body {
  margin: 0;
}

.sidebar {
  flex: 0 0 250px; /* Adjust the width of the sidebar as needed */
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  overflow-y: auto;
  min-width: 200px;
  padding: 25px;
  background-color: #1c1b23;
}

.menu-item {
  color: #fff;
  display: block;
  padding: 10px;
  margin-bottom: 20px;
  text-decoration: none;
  background-color: #1c1b23;
  border-radius: 5px;
  border: 1px solid darkgray;
  line-height: 2rem;
}

.menu-item:hover,
.menu-item.active {
  background-color: #5252a6;
}
.main-content {
  flex: 1;
  padding: 20px;
  margin-left: 250px;
  overflow-y: auto;
}
</style>
