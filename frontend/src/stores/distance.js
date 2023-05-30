import { defineStore } from 'pinia'

export const useDistanceStore = defineStore('distance', {
  state: () => {
    return { 
      latitude_a: 0,
      longitude_a: 0,
      latitude_b: 0,
      longitude_b: 0,
    }
  },
  // could also be defined as
  // state: () => ({ count: 0 })
  actions: {
    increment() {
      this.count++
    },
  },
})
