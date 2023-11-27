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
}

.sidebar {
  width: 200px;
  background-color: #f0f0f0;
  padding: 20px;
}

.menu-item {
  display: block;
  padding: 10px;
  margin-bottom: 10px;
  text-decoration: none;
  color: #333;
}

.menu-item:hover,
.menu-item.active {
  background-color: #ddd;
}

.main-content {
  flex: 1;
  padding: 20px;
}
</style>
