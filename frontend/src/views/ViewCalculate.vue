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

document.title = 'Calculate points';
</script>
