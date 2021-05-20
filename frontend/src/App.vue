<template>
  <div id="app">
    <app-header />
    <div class="flex hidden" :class="{ 'is-loading': $store.state.isLoading }">
      <div class="spinner-border text-primary"></div>
    </div>
    <div class="container">
      <router-view></router-view>
    </div>
    <notifications-list />
  </div>
</template>

<script>
  import axios from 'axios'
  import AppHeader from "./components/AppHeader";
  import NotificationsList from "./components/NotificationsList";

  export default {
    name: "app",
    components: {
      AppHeader,
      NotificationsList
    },
    beforeCreate() {
      if (this.$store.state.token) {
        axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    }
  };
</script>

<style>
  .flex {
    display: flex;
    justify-content: center;
    margin-top: 10px;
  }
  .hidden {
    height: 0;
    overflow: hidden;
  }
  .is-loading {
    height: 80px;
  }
</style>