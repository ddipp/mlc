import { defineStore } from 'pinia';
import axios from "axios";

export const useNextPointStore = defineStore('nextpoint', {
  state: () => ({
    la_a: '',
    lo_a: '',
    la_b: '',
    lo_b: '',
    dis: '',
    bea: '',
    p_a_elevation: '',
    p_b_elevation: '',
    changed: false,
  }),
  actions: {
    async calculate() {
      const c = 1000000;
      const la_a = parseInt(this.la_a * c, 10);
      const lo_a = parseInt(this.lo_a * c, 10);
      const dis = parseInt(this.dis * c, 10);
      const bea = parseInt(this.bea * c, 10);
      try {
        const response = await axios.get(`/nextpoint/${la_a}/${lo_a}/${dis}/${bea}`);
        this.la_b = response.data.latitude_b;
        this.lo_b = response.data.longitude_b;
        this.p_a_elevation = response.data.p_a_elevation;
        this.p_b_elevation = response.data.p_b_elevation;
        this.changed = true;
      }
      catch(error) {
        alert(error);
      };
    },
  },
})
