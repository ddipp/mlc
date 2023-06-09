import { defineStore } from 'pinia';
import axios from "axios";

export const usePathStore = defineStore('path', {
  state: () => ({
    la_a: '',
    lo_a: '',
    la_b: '',
    lo_b: '',
    distance: '',
    arc_distance: '',
    az_a_b: '',
    az_b_a: '',
    p_a_elevation: '',
    p_b_elevation: '',
    graph: '',
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
        const response = await axios.get(`/profile/${la_a}/${lo_a}/${la_b}/${lo_b}`);
        this.distance = response.data.distance;
        this.az_a_b = response.data.az_a_b;
        this.az_b_a = response.data.az_b_a;
        this.p_a_elevation = response.data.p_a_elevation;
        this.p_b_elevation = response.data.p_b_elevation;
        this.graph = response.data.graph;
        this.changed = true;
      }
      catch(error) {
        alert(error);
      };
    },
  },
})
