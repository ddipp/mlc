<template>
  <h3>Find all points and their elevations between the given ones every 10 meters</h3>
  <fieldset>
    <legend>Point A</legend>
    <div class="grid">
      <label for="la_a">
        Latitude
        <input id="la_a" v-model="la_a" placeholder="Latitude">
      </label>
      <label for="lo_a">
        Longitude
        <input id="lo_a" v-model="lo_a" placeholder="Longitude">
      </label>
    </div>
  </fieldset>

  <fieldset>
    <legend>Point B</legend>
    <div class="grid">
      <label for="la_b">
        Latitude
        <input id="la_b" v-model="la_b" placeholder="Latitude">
      </label>
      <label for="lo_b">
        Longitude
        <input id="lo_b" v-model="lo_b" placeholder="Longitude">
      </label>
    </div>
  </fieldset>
  <button @click="path.calculate()">Calculate</button>

  <div v-if="path.changed" class="answer">
    <fieldset>
      <ul>
        <li>Distance between two points in kilometers in a straight line {{ path.distance }}</li>
        <li>Cource from Point A to Point B {{ path.az_a_b }}°</li>
        <li>Cource from Point B to Point A {{ path.az_b_a }}°</li>
        <li>Point A. Altitude {{ path.p_a_elevation }} m</li>
        <li>Point B. Altitude {{ path.p_b_elevation }} m</li>
      </ul>
    </fieldset>
    <img alt="Profile PointA to PointB" v-bind:src="path.graph"/>
  </div>
</template>

<script setup>
// TODO: rename variable
import { computed } from 'vue';
import { usePathStore } from '@/stores/path';

const path = usePathStore();

const la_a = computed({
  get() {
    return path.la_a;
  },
  set(newValue) {
    path.la_a = newValue;
    path.changed = false;
  },
});

const la_b = computed({
  get() {
    return path.la_b;
  },
  set(newValue) {
    path.la_b = newValue;
    path.changed = false;
  },
});

const lo_a = computed({
  get() {
    return path.lo_a;
  },
  set(newValue) {
    path.lo_a = newValue;
    path.changed = false;
  },
});

const lo_b = computed({
  get() {
    return path.lo_b;
  },
  set(newValue) {
    path.lo_b = newValue;
    path.changed = false;
  },
});

</script>
