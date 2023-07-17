import { defineStore } from 'pinia';
import axios from "axios";

export const usePathStore = defineStore('path', {
  state: () => ({
    job_id: '',
    job_status: '',
    job_poolinterval: '',
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
    profile_name: '',
    profile_url: axios.defaults.baseURL + '/profile_get/',
    changed: false,
  }),
  actions: {
    async get_job_status() {
      try {
        const response = await axios.get(`/profile_check/${this.job_id}`);
        this.job_status = response.data.job_status;
        this.changed = true;
        if (this.job_status === 'finished') {
          clearInterval(this.job_poolinterval);
          this.distance = response.data.distance;
          this.az_a_b = response.data.az_a_b;
          this.az_b_a = response.data.az_b_a;
          this.p_a_elevation = response.data.p_a_elevation;
          this.p_b_elevation = response.data.p_b_elevation;
          this.profile_name = response.data.profile_name;
        }
      }
      catch(error) {
        alert(error);
      };
    },
    async calculate() {
      this.distance = '';
      this.az_a_b = '';
      this.az_b_a = '';
      this.p_a_elevation = '';
      this.p_b_elevation = '';
      this.profile_name = '';
      const c = 1000000;
      const la_a = parseInt(this.la_a * c, 10);
      const lo_a = parseInt(this.lo_a * c, 10);
      const la_b = parseInt(this.la_b * c, 10);
      const lo_b = parseInt(this.lo_b * c, 10);
      try {
        const response = await axios.get(`/profile_add_task/${la_a}/${lo_a}/${la_b}/${lo_b}`);
        this.job_id = response.data.job_id;
        this.job_status = response.data.job_status;
        this.changed = true;
        if (this.job_status !== 'finished') {
          this.job_poolinterval = setInterval(() => {this.get_job_status()}, 1000);
          setTimeout(() => { clearInterval(this.job_poolinterval) }, 60000);
        }
        else {
          this.distance = response.data.distance;
          this.az_a_b = response.data.az_a_b;
          this.az_b_a = response.data.az_b_a;
          this.p_a_elevation = response.data.p_a_elevation;
          this.p_b_elevation = response.data.p_b_elevation;
          this.profile_name = response.data.profile_name;
        }
      }
      catch(error) {
        alert(error);
      };
    },
  },
})
