import { defineStore } from 'pinia';
import axios from "axios";

export const useTestStore = defineStore('test', {
  state: () => ({
    x: '',
    y: '',
    job_id: '',
    sum: '',
    graph: '',
    changed: false,
  }),
  actions: {
    async calculate() {
      const c = 1;
      const x = parseInt(this.x * c, 10);
      const y = parseInt(this.y * c, 10);

      try {
        const response = await axios.get(`/xy/${x}/${y}`);
        this.job_id = response.data.job_id;
        this.sum = response.data.sum;
        this.changed = true;
      }
      catch(error) {
        alert(error);
      };
    },
  },
})
