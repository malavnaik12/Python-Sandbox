<template>
  <div id="app">
    <UserGreeting />
  </div>
</template>

<script>
// import UserGreeting from './components/UserGreeting.vue';
import UserGreeting from './components/UserGreetingFastapi.vue';

export default {
  name: 'App',
  components: {
    UserGreeting
  }
};
</script>
