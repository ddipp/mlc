import { defineStore } from 'pinia';
import axios from "axios";

export const useDistanceStore = defineStore('distance', {
  state: () => ({
    la_a: 0,
    lo_a: 0,
    la_b: 0,
    lo_b: 0,
    distance: '',
    arc_distance: '',
    az_a_b: '',
    az_b_a: '',
    changed: false,
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
        this.arc_distance = response.data.arc_distance;
        this.az_a_b = response.data.az_a_b;
        this.az_b_a = response.data.az_b_a;
        this.changed = true;
      }
      catch(arror) {
        alert(error);
      };
    },
  },
})
