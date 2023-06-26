<template>
  <h3>Find all points and their elevations between the given ones every 10 meters</h3>
  <fieldset>
    <legend>Point A</legend>
    <div class="grid">
      <label for="x">
        X
        <input id="x" v-model="x" placeholder="X">
      </label>
      <label for="y">
        Y
        <input id="y" v-model="y" placeholder="Y">
      </label>
    </div>
  </fieldset>

  <button @click="test.calculate()">Calculate</button>

  <div v-if="test.changed" class="answer">
    <fieldset>
      <ul>
        <li>Job ID {{ test.job_id }}</li>
        <li>SUM {{ test.sum }}</li>
      </ul>
    </fieldset>
    <img alt="Profile PointA to PointB" v-bind:src="test.graph"/>
  </div>
</template>

<script setup>
// TODO: rename variable
import { computed } from 'vue';
import { useTestStore } from '@/stores/test';

const test = useTestStore();

const x = computed({
  get() {
    return test.x;
  },
  set(newValue) {
    test.x = newValue;
    test.changed = false;
  },
});

const y = computed({
  get() {
    return test.y;
  },
  set(newValue) {
    test.y = newValue;
    test.changed = false;
  },
});

</script>
