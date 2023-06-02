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
        <input v-model="lo_a" placeholder="Longitude">
      </div>
    </div>
  </fieldset>
  <fieldset>
    <legend>Point B</legend>
    <div class="row">
      <div class="column">Latitude</div>
      <div class="column">
        <input v-model="la_b" placeholder="Latitude">
      </div>
    </div>
    <div class="row">
      <div class="column">Longitude</div>
      <div class="column">
        <input v-model="lo_b" placeholder="Longitude">
      </div>
    </div>
  </fieldset>
  <button @click="distance.calculate()">Calculate</button>

  <div v-if="distance.changed" class="answer">
    <fieldset>
      <ul>
        <li>Distance between two points in kilometers in a straight line {{ distance.distance }}</li>
        <li>Distance between two points in kilometers on the surface of the planet {{ distance.arc_distance }}</li>
        <li>Cource from Point A to Point B {{ distance.az_a_b }}°</li>
        <li>Cource from Point B to Point A {{ distance.az_b_a }}°</li>
        <li>Point A. Altitude {{ distance.p_a_elevation }} m</li>
        <li>Point B. Altitude {{ distance.p_b_elevation }} m</li>
      </ul>
    </fieldset>
  </div>
</template>

<script setup>
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
