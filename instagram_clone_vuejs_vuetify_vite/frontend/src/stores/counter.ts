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

    searchQuery: null,

    userLoggedIn: false,
    setAuthToken:null,
    setAuthTokenType:null,
    setUserId:null,
    setUsername:null,
    tab:null,
    // BASE_URL: 'http://localhost:8000/',
    BASE_URL: 'https://d7b2-219-92-69-253.ngrok-free.app/api/',
    userData:null,
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
          // this.setAuthToken = (<any>response).data.access_token
          // this.setAuthTokenType = (<any>response).data.token_type
          // this.setUserId = (<any>response).data.user_id
          // this.setUsername = (<any>response).data.username
          localStorage.setItem('access_token', response.data.access_token);
          localStorage.setItem('email', response.data.user.email);
          this.userData = (<any>response).data.user
          localStorage.setItem('userData', JSON.stringify(this.userData));
          return 'Success'

          
        })
        .catch(error => {
          console.error('There was an error submitting the data:', error.response.data);
          return error.response.data.detail
        });
      

    },
    logout(){
      // KADA CREDENTIALS EXPIRED THROW USER OUT FORM WEBSITE
      this.userLoggedIn = false
      this.setAuthToken = null
      this.setAuthTokenType = null
      this.setUserId = null
      this.setUsername = null
      localStorage.removeItem('access_token');
      localStorage.removeItem('email');
      localStorage.removeItem('userData');
    },
  }
})

