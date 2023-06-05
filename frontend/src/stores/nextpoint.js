import { defineStore } from 'pinia';
import axios from "axios";

export const useNextPointStore = defineStore('nextpoint', {
  state: () => ({
    latitude_a: '',
    longitude_a: '',
    latitude_b: '',
    longitude_b: '',
    distance: '',
    bearing: '',
    p_a_elevation: '',
    p_b_elevation: '',
    changed: false,
  }),
  actions: {
    async calculate() {
      const c = 1000000;
      const latitude_a = parseInt(this.latitude_a * c, 10);
      const longitude_a = parseInt(this.longitude_a * c, 10);
      const distance = parseInt(this.distance * c, 10);
      const bearing = parseInt(this.bearing * c, 10);
      try {
        const response = await axios.get(`/nextpoint/${latitude_a}/${longitude_a}/${distance}/${bearing}`);
        this.latitude_b = response.data.latitude_b;
        this.longitude_b = response.data.longitude_b;
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
