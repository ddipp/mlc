<template>
  <div class="row">
    <div class="column">
      <ComponentDistance />
    </div>
    <div class="column">
      <ComponentNextPoint />
    </div>
  </div>
</template>

<script setup>
import ComponentDistance from '@/components/ComponentDistance.vue';
import ComponentNextPoint from '@/components/ComponentNextPoint.vue';

document.title = 'Profile radio planner';
</script>
