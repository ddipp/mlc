<template>
  <h3>Find next point by distance and bearing </h3>
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
      <label for="dis">
        Distance
        <input id="dis" v-model="dis" placeholder="Distance">
      </label>
      <label for="bea">
        Bearing (°)
        <input id="bea" v-model="bea" placeholder="Bearing (°)">
      </label>
    </div>
  </fieldset>
  <button @click="nextpoint.calculate()">Calculate</button>
  <div v-if="nextpoint.changed" class="answer">
    <fieldset>
      <legend>Point A</legend>
      <ul>
        <li>Altitude {{ nextpoint.p_a_elevation }} m</li>
      </ul>
    </fieldset>
    <fieldset>
      <legend>Point B</legend>
      <ul>
        <li>Latitude {{ nextpoint.la_b }}</li>
        <li>Longitude {{ nextpoint.lo_b }}</li>
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

const la_a = computed({
  get() {
    return nextpoint.la_a;
  },
  set(newValue) {
    nextpoint.la_a = newValue;
    nextpoint.changed = false;
  },
});

const lo_a = computed({
  get() {
    return nextpoint.lo_a;
  },
  set(newValue) {
    nextpoint.lo_a = newValue;
    nextpoint.changed = false;
  },
});

const dis = computed({
  get() {
    return nextpoint.dis;
  },
  set(newValue) {
    nextpoint.dis = newValue;
    nextpoint.changed = false;
  },
});

const bea = computed({
  get() {
    return nextpoint.bea;
  },
  set(newValue) {
    nextpoint.bea = newValue;
    nextpoint.changed = false;
  },
});

</script>
