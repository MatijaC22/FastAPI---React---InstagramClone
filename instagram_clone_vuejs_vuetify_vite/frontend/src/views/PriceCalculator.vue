<template>
  <v-main>
  <v-container fluid class="pa-1 mt-3">
<v-card class="pa-1" elevation="2" style="background-image: linear-gradient(to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)), url('../src/assets/images/background3.jpg'); background-size: cover;">

    <v-card color="grey-lighten-5"
                    border
                    class="mb-2"
                    density="compact">
    <div>
  
  <v-card border density="compact" title="CURRENCY LIST" variant="text">
    <tr style="min-width:100%;">
      <div style="display:flex; align-items:center;">
        <div style="flex-grow: 1;">
          <v-text-field
              :loading="loading"
              density="compact"
              variant="solo-filled"
              label="Search"
              append-inner-icon="mdi-magnify"
              single-line
              hide-details
              style="min-width:230px; margin: 0 10px 0 15px;"
              v-model="search"
            >
          </v-text-field>
        </div>
        
        <v-btn
          color="primary"
          v-bind="props"
          style="margin-bottom:0px;"
          class="ml-2"
          height="42"
          @click="this.refreshList()"
        >
          REFRESH
        </v-btn>         
        
    </div>
  </tr>

  <!-- <br> -->
 

  <!-- height je sada 63.5vh ali treba viit kako to nastimati korektno -->
  <div style="margin-left:20px;"> {{ formattedTime }} </div>
  <v-table
    fixed-header
    height="63.5vh"
    density="compact"
    class="mt-2"
  >
  <thead>
    <tr>
      <th class="text-left"
        v-for="(title, index) in ['name','value']"
        :key="index"
      >
        <div>{{ title }}</div>
        <div>{{title=='name' ? 'USD' : '1'}}</div>
      </th> 
    </tr>
  </thead>
    <tbody v-if="filteredItems != null">
      <tr v-for="(rate, index) in filteredItems" :key="index">
        <td >{{ rate.name }}</td>
        <td >{{ rate.value }}</td>
      </tr>           
    </tbody>
  </v-table>


  </v-card>
  </div>
    <br>
    </v-card>
</v-card>
  </v-container>
</v-main>
</template>

<script>
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';
import { mapState } from 'pinia'
import { mapActions } from 'pinia'
export default {
  data() {
    return{
      props:null,
      loading:null,
      extractionTime:null,
      currencies:null,
      formattedTime: '',
      filteredList:[],
      search:'',
    }
  },
  methods:{
    ...mapActions(useCounterStore, ['logout']),

    async getCurrencylist(){
      await axios.get(this.BASE_URL + 'sideFunctionalities/currencyRate')
      .then(response => {
        console.log('this is currencyRate.', response);
        
        const parsedData = response.data;
        const ratesObject = parsedData.rates;
        const rateArray = [];

        for (const [name, value] of Object.entries(ratesObject)) {
          rateArray.push({ name, value });
        }
        this.extractionTime = parsedData.timestamp
        this.currencies =  rateArray
        this.filteredList = this.currencies,
        console.log(this.currencies)
        console.log(this.filteredList)
      })
      .catch(error => {
        console.error('There was an error:', error.response.data);
        if(error.response.data.detail == 'Could not validate credentials'){
          this.logout()          
        }
      });
      this.timestamp(this.extractionTime);
    },
    timestamp(extractionTime){
      const date = new Date(extractionTime);
      const options = { 
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric',
        timeZone: 'UTC'
      };
      this.formattedTime = date.toLocaleString('nl-BE', options);
    },
    refreshList(){
      this.getCurrencylist();
      
    }
  },
  computed:{
    ...mapState(useCounterStore, ['BASE_URL']),

    filteredItems(){
      console.log(this.search)
      // console.log(this.filteredList)
      return this.filteredList.filter((data) => {
        const values = Object.values(data)
        return values.some((value) => {
          return String(value).toLowerCase().includes(this.search.toLowerCase())
        })
      })
    }
  },
  created(){
    this.refreshList()
  }
}
</script>