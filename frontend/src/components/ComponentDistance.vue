<template>
  <h3>Find distance and bearing between two coordinates</h3>
  <fieldset>
    <legend>Point A</legend>
    <div class="row">
      <div class="column">Latitude</div>
      <div class="column">
        <input v-model="distance.latitude_a" placeholder="Latitude">
      </div>
    </div>
    <div class="row">
      <div class="column">Longitude</div>
      <div class="column">
        <input v-model="distance.longitude_a" placeholder="Longitude">
      </div>
    </div>
  </fieldset>
  <fieldset>
    <legend>Point B</legend>
    <div class="row">
      <div class="column">Latitude</div>
      <div class="column">
        <input v-model="distance.latitude_b" placeholder="Latitude">
      </div>
    </div>
    <div class="row">
      <div class="column">Longitude</div>
      <div class="column">
        <input v-model="distance.longitude_b" placeholder="Longitude">
      </div>
    </div>
  </fieldset>
</template>

<script setup>
import axios from 'axios';

import { useDistanceStore } from '@/stores/distance';

const distance = useDistanceStore();

</script>
