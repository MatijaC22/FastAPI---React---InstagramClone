import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import axios from 'axios'
import qs from 'qs';


interface LoginValues {
  email: string;
  password: string;
}

export const useCounterStore = defineStore({
  id: 'auth',
  state: () => ({
    isLoading: false,
    authModalShow: true,
    userLoggedIn: false,
    setAuthToken:null,
    setAuthTokenType:null,
    setUserId:null,
    setUsername:null,
    tab:null,
    BASE_URL: 'http://localhost:8000/',
    // BASE_URL: 'https://f09e-2402-4000-10c4-5e38-51f0-2970-8169-bc6c.ngrok-free.app/api/',
    userData:null
  }),
  getters: {
    // setIsLoading: (state:any, status:any) => {
    //   return state.isLoading = status
    // },
    // doubleCount: (state) => state.counter * 2
  },
  actions: {
    async login(values:LoginValues) {

      const data = qs.stringify({
        grant_type: '',
        username: values.email,
        password: values.password,
        scope: '',
        client_id: '',
        client_secret: ''
      });
      
      await axios.post(this.BASE_URL + 'login', data, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Accept': 'application/json'
        }
      })
        .then(response => {
          console.log('Data was successfully submitted.', response);
          this.setAuthToken = (<any>response).data.access_token
          this.setAuthTokenType = (<any>response).data.token_type
          this.setUserId = (<any>response).data.user_id
          this.setUsername = (<any>response).data.username
          localStorage.setItem('access_token', response.data.access_token);
          localStorage.setItem('username', response.data.username);
          return 'Success'

          
        })
        .catch(error => {
          console.error('There was an error submitting the data:', error.response.data);
          return error.response.data.detail
        });
      

    },
    async registerUser(login:any, password:any) {
      // try {
      //   this.userData = await api.post({ login, password })
      //   showTooltip(`Welcome back ${this.userData.name}!`)
      // } catch (error) {
      //   showTooltip(error)
      //   // let the form component display the error
      //   return error
      // }
    },
    // increment() {
    //   this.counter++
    // }
  }
})
// export const useStore = defineStore({
//   id: 'myStore',
//   state: () => ({
//     isLoading: false,
//     authModalShow: true,
//     userLoggedIn: false,
//     BASE_URL: 'http://localhost:8000/'
//   }),
//   getters: {
//     // Define your getters here
//   },
//   actions: {
//     async login(payload) {
//       // Define your actions here
//     },
//   },
//   mutations: {
//     setIsLoading(status) {
//       this.isLoading = status
//     },
//     // Define your mutations here
//   },
//   // Define your modules here
// })
