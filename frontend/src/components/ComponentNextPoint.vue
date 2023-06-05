<template>
  <h3>Find next point by distance and bearing </h3>
  <fieldset>
    <legend>Point A</legend>
    <div class="row">
      <div class="column">Latitude</div>
      <div class="column">
        <input v-model="latitude_a" placeholder="Latitude">
      </div>
    </div>
    <div class="row">
      <div class="column">Longitude</div>
      <div class="column">
        <input v-model="longitude_a" placeholder="Longitude">
      </div>
    </div>
    <div class="row">
      <div class="column">Distance (km)</div>
      <div class="column">
        <input v-model="distance" placeholder="Distance">
      </div>
    </div>
    <div class="row">
      <div class="column">Bearing (°)</div>
      <div class="column">
        <input v-model="bearing" placeholder="Bearing">
      </div>
    </div>
  </fieldset>
  <button @click="nextpoint.calculate()">Calculate</button>
  <div v-if="nextpoint.changed" class="answer">
    <fieldset>
      <legend>Point B</legend>
      <ul>
        <li>Latitude {{ nextpoint.latitude_b }}</li>
        <li>Longitude {{ nextpoint.longitude_b }}</li>
        <li>Altitude {{ nextpoint.p_b_elevation }} m</li>
      </ul>
    </fieldset>
  </div>
</template>

<script setup>
// TODO: rename variable
import { computed } from 'vue';
import { useNextPointStore } from '@/stores/nextpoint';

const nextpoint = useNextPointStore();

const latitude_a = computed({
  get() {
    return nextpoint.latitude_a;
  },
  set(newValue) {
    nextpoint.latitude_a = newValue;
    nextpoint.changed = false;
  },
});

const longitude_a = computed({
  get() {
    return nextpoint.longitude_a;
  },
  set(newValue) {
    nextpoint.longitude_a = newValue;
    nextpoint.changed = false;
  },
});

const distance = computed({
  get() {
    return nextpoint.distance;
  },
  set(newValue) {
    nextpoint.distance = newValue;
    nextpoint.changed = false;
  },
});

const bearing = computed({
  get() {
    return nextpoint.bearing;
  },
  set(newValue) {
    nextpoint.bearing = newValue;
    nextpoint.changed = false;
  },
});

</script>
