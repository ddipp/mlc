import { defineStore } from 'pinia';
import axios from "axios";

export const useDistanceStore = defineStore('distance', {
  state: () => ({
    la_a: 0,
    lo_a: 0,
    la_b: 0,
    lo_b: 0,
    distance: '',
    changed: true,
  }),
  actions: {
    async calculate() {
      const c = 1000000;
      const la_a = parseInt(this.la_a * c, 10);
      const lo_a = parseInt(this.lo_a * c, 10);
      const la_b = parseInt(this.la_b * c, 10);
      const lo_b = parseInt(this.lo_b * c, 10);
      try {
        const response = await axios.get(`/distance/${la_a}/${lo_a}/${la_b}/${lo_b}`);
        this.distance = response.data.distance;
        this.changed = true;
      }
      catch(arror) {
        alert(error);
      };
    },
  },
})
