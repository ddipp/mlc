<template>
  <h3>Find distance and bearing between two coordinates</h3>
  <fieldset>
    <legend>Point A</legend>
    <div class="row">
      <div class="column">Latitude</div>
      <div class="column">
        <input v-model="la_a" placeholder="Latitude">
      </div>
    </div>
    <div class="row">
      <div class="column">Longitude</div>
      <div class="column">
        <input v-model="distance.lo_a" placeholder="Longitude">
      </div>
    </div>
  </fieldset>
  <fieldset>
    <legend>Point B</legend>
    <div class="row">
      <div class="column">Latitude</div>
      <div class="column">
        <input v-model="distance.la_b" placeholder="Latitude">
      </div>
    </div>
    <div class="row">
      <div class="column">Longitude</div>
      <div class="column">
        <input v-model="distance.lo_b" placeholder="Longitude">
      </div>
    </div>
  </fieldset>
  <button @click="distance.calculate()">Calculate</button>

  <h1 v-if="distance.changed">{{ distance.distance }}</h1>
</template>

<script setup>
import axios from 'axios';
import { computed } from 'vue';
import { useDistanceStore } from '@/stores/distance';

const distance = useDistanceStore();

const la_a = computed({
  get() {
    return distance.la_a;
  },
  set(newValue) {
    distance.la_a = newValue;
    distance.changed = false;
  },
});

const la_b = computed({
  get() {
    return distance.la_b;
  },
  set(newValue) {
    distance.la_b = newValue;
    distance.changed = false;
  },
});

const lo_a = computed({
  get() {
    return distance.lo_a;
  },
  set(newValue) {
    distance.lo_a = newValue;
    distance.changed = false;
  },
});

const lo_b = computed({
  get() {
    return distance.lo_b;
  },
  set(newValue) {
    distance.lo_b = newValue;
    distance.changed = false;
  },
});

</script>
