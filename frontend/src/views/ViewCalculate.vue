<template>
  <div class="grid">
    <div>
      <ComponentDistance />
    </div>
    <div>
      <ComponentNextPoint />
    </div>
  </div>
</template>

<script setup>
import ComponentDistance from '@/components/ComponentDistance.vue';
import ComponentNextPoint from '@/components/ComponentNextPoint.vue';

document.title = 'Profile radio planner';
</script>

<style>
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  grid-gap: 1rem;
}
.grid > div {
  background: #EDE7F6;
  padding: 1.5rem;
  border-radius: 1rem;
}
input {
  width: 50%;
}
</style>
