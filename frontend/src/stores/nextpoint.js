import { defineStore } from 'pinia';
import axios from "axios";

export const useNextPointStore = defineStore('nextpoint', {
  state: () => ({
    job_id: '',
    job_status: '',
    job_poolinterval: '',
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
    async get_job_status() {
      try {
        const response = await axios.get(`/nextpoint_check/${this.job_id}`);
        this.job_status = response.data.job_status;
        this.changed = true;
        if (this.job_status === 'finished') {
          clearInterval(this.job_poolinterval);
          this.la_b = response.data.latitude_b;
          this.lo_b = response.data.longitude_b;
          this.p_a_elevation = response.data.p_a_elevation;
          this.p_b_elevation = response.data.p_b_elevation;
        }
      }
      catch(error) {
        alert(error);
      };
    },

    async calculate() {
      this.la_b = '';
      this.lo_b = '';
      this.p_a_elevation = '';
      this.p_b_elevation = '';
      const la_a = parseFloat(this.la_a);
      const lo_a = parseFloat(this.lo_a);
      const dis = parseFloat(this.dis);
      const bea = parseFloat(this.bea);
      try {
        const response = await axios.get(`/nextpoint_add_task/${la_a}/${lo_a}/${dis}/${bea}`);
        this.job_id = response.data.job_id;
        this.job_status = response.data.job_status;
        this.changed = true;
        if (this.job_status !== 'finished') {
          this.job_poolinterval = setInterval(() => {this.get_job_status()}, 1000);
          setTimeout(() => { clearInterval(this.job_poolinterval) }, 60000);
        }
        else {
          this.la_b = response.data.latitude_b;
          this.lo_b = response.data.longitude_b;
          this.p_a_elevation = response.data.p_a_elevation;
          this.p_b_elevation = response.data.p_b_elevation;
        }
      }
      catch(error) {
        alert(error);
      };
    },
  },
})
