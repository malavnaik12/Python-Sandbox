<template>
  <div>
    <h1>Enter your name:</h1>
    <input v-model="name" placeholder="Your name">
    <button @click="submitName">Submit</button>
    <h2>{{ greeting }}</h2>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UserGreeting',
  data() {
    return {
      name: '',
      greeting: ''
    };
  },
  methods: {
    async submitName() {
      try {
        const response = await axios.post('http://localhost:8000/api/greet', { name: this.name });
        this.greeting = response.data.greeting;
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>
