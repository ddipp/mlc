<template>
  <div class="row">
    <div class="column">
      <h3>Find distance and bearing between two coordinates</h3>
      <fieldset>
        <legend>Point A</legend>
        <div class="row">
          <div class="column">Latitude</div>
          <div class="column">
              <input placeholder="Latitude">
          </div>
        </div>
        <div class="row">
          <div class="column">Longitude</div>
          <div class="column">
              <input placeholder="Longitude">
          </div>
      </div>
    </fieldset>
    <fieldset>
        <legend>Point B</legend>
        <div class="row">
          <div class="column">Latitude</div>
          <div class="column">
              <input placeholder="Latitude">
          </div>
        </div>
        <div class="row">
          <div class="column">Longitude</div>
          <div class="column">
              <input placeholder="Longitude">
          </div>
      </div>
    </fieldset>
    </div>
    <div class="column">
      <h3>Find next point by distance and bearing </h3>
      <fieldset>
        <legend>Point A</legend>
        <div class="row">
          <div class="column">Latitude</div>
          <div class="column">
            <input placeholder="Latitude">
          </div>
        </div>
        <div class="row">
          <div class="column">Longitude</div>
          <div class="column">
            <input placeholder="Longitude">
          </div>
        </div>
        <div class="row">
          <div class="column">Distance (km)</div>
          <div class="column">
            <input placeholder="Distance">
          </div>
        </div>
        <div class="row">
          <div class="column">Bearing (°)</div>
          <div class="column">
            <input placeholder="Bearing">
          </div>
        </div>
      </fieldset>
    </div>
  </div>
</template>

<script setup>
document.title = 'Profile radio planner';
</script>
