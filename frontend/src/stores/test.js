import { defineStore } from 'pinia';
import axios from "axios";

export const useTestStore = defineStore('test', {
  state: () => ({
    x: '',
    y: '',
    job_id: '',
    job_status: '',
    job_result: '',
    job_poolinterval: '',
    sum: '',
    graph: '',
    changed: false,
  }),
  actions: {
    async get_job_status() {
      try {
        const response = await axios.get(`/xy_check/${this.job_id}`);
        this.job_status = response.data.job_status;
        this.job_result = response.data.job_result;
        this.changed = true;
        console.log('pooling...');
        if (this.job_status === 'finished') {
          clearInterval(this.job_poolinterval);
        }
      }
      catch(error) {
        alert(error);
      };
    },

    async calculate() {
      const c = 1;
      const x = parseInt(this.x * c, 10);
      const y = parseInt(this.y * c, 10);

      try {
        const response = await axios.get(`/xy/${x}/${y}`);
        this.job_id = response.data.job_id;
        this.job_status = response.data.job_status;
        this.job_result = response.data.job_result;
        this.changed = true;
        if (this.job_status !== 'finished') {
          this.job_poolinterval = setInterval(() => {this.get_job_status()}, 1000);
          console.log(this.job_poolinterval);
        }
        else {
          console.log('Finish!');
        }
      }
      catch(error) {
        alert(error);
      };
    },
  },
})
