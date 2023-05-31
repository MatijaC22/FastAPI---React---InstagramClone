<template>
<v-main>
  <v-container fluid class="pa-1">
    <v-card class="pa-1" elevation="2" style="background-image: linear-gradient(to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)), url('../src/assets/images/background3.jpg'); background-size: cover;">
      <v-card color="grey-lighten-5" border density="compact">
        <div v-if="isLoading">Loading...</div>
        <DataTable v-else :dataItems="list" :dataItemsHeaders="headers" :name="this.$route.fullPath.split('database/')[1].toUpperCase()"/>
        <br>
      </v-card>
    </v-card>
  </v-container>
</v-main>
</template>


<script>
import axios from 'axios'
import DataTable from '@/components/DataTable.vue'

import { useCounterStore } from '@/stores/counter';
import { mapWritableState } from 'pinia'
import { mapState } from 'pinia'

export default {
  components:{
    DataTable
  },
  data() {
    return{
      list:[],
      headers:[],
      // containersListHeaders:['Reference','lastModify','Location','Country','ResponsableName','ClientName','TransportType','ProductType','View','Action'],
    //   containersListHeaders:[],
    // containersList: [
    //   {
    //     Reference:'3224301',
    //     lastModify:'15/10/2023',
    //     Location:'San Sebastion',
    //     Country:'Guatemala',
    //     ResponsableName:'Ivan Sen',
    //     ClientName:'Sin Xaio Hel',
    //     TransportType:'Sea',
    //     ProductType:'Oil',
    //   },
    //   {
    //     Reference:'3224302',
    //     lastModify:'15/10/2021',
    //     Location:'San Sebastion',
    //     Country:'Guatemala',
    //     ResponsableName:'Ivan Sen',
    //     ClientName:'Sin Xaio Hel',
    //     TransportType:'Sea',
    //     ProductType:'Oil',
    //   },
    //   {
    //     Reference:'3224303',
    //     lastModify:'15/10/2021',
    //     Location:'San Sebastion',
    //     Country:'Guatemala',
    //     ResponsableName:'Ivan Sen',
    //     ClientName:'Sin Xaio Hel',
    //     TransportType:'Sea',
    //     ProductType:'Oil',
    //   },
    //   {
    //     Reference:'3224304',
    //     lastModify:'15/10/2021',
    //     Location:'San Sebastion',
    //     Country:'Guatemala',
    //     ResponsableName:'Ivan Sen',
    //     ClientName:'Sin Xaio Hel',
    //     TransportType:'Sea',
    //     ProductType:'Oil',
    //   },
    //   {
    //     Reference:'3224305',
    //     lastModify:'15/10/2021',
    //     Location:'San Sebastion',
    //     Country:'Guatemala',
    //     ResponsableName:'Ivan Sen',
    //     ClientName:'Sin Xaio Hel',
    //     TransportType:'Sea',
    //     ProductType:'Oil',
    //   },
    //   {
    //     Reference:'3224306',
    //     lastModify:'15/10/2021',
    //     Location:'San Sebastion',
    //     Country:'Guatemala',
    //     ResponsableName:'Ivan Sen',
    //     ClientName:'Sin Xaio Hel',
    //     TransportType:'Sea',
    //     ProductType:'Oil',
    //   },
    //   {
    //     Reference:'3224307',
    //     lastModify:'15/10/2021',
    //     Location:'San Sebastion',
    //     Country:'Guatemala',
    //     ResponsableName:'Ivan Sen',
    //     ClientName:'Sin Xaio Hel',
    //     TransportType:'Sea',
    //     ProductType:'Oil',
    //   },
    //   {
    //     Reference:'3224308',
    //     lastModify:'15/10/2021',
    //     Location:'San Sebastion',
    //     Country:'Guatemala',
    //     ResponsableName:'Ivan Sen',
    //     ClientName:'Sin Xaio Hel',
    //     TransportType:'Sea',
    //     ProductType:'Oil',
    //   },
    //   {
    //     Reference:'3224309',
    //     lastModify:'15/10/2021',
    //     Location:'San Sebastion',
    //     Country:'Guatemala',
    //     ResponsableName:'Ivan Sen',
    //     ClientName:'Sin Xaio Hel',
    //     TransportType:'Sea',
    //     ProductType:'Oil',
    //   },
    //   {
    //     Reference:'3224310',
    //     lastModify:'15/10/2021',
    //     Location:'San Sebastion',
    //     Country:'Guatemala',
    //     ResponsableName:'Ivan Sen',
    //     ClientName:'Sin Xaio Hel',
    //     TransportType:'Sea',
    //     ProductType:'Oil',
    //   },
    //   {
    //     Reference:'3224311',
    //     lastModify:'15/10/2021',
    //     Location:'San Sebastion',
    //     Country:'Guatemala',
    //     ResponsableName:'Ivan Sen',
    //     ClientName:'Sin Xaio Hel',
    //     TransportType:'Sea',
    //     ProductType:'Oil',
    //   },
    //   {
    //     Reference:'3224312',
    //     lastModify:'15/10/2021',
    //     Location:'San Sebastion',
    //     Country:'Guatemala',
    //     ResponsableName:'Ivan Sen',
    //     ClientName:'Sin Xaio Hel',
    //     TransportType:'Sea',
    //     ProductType:'Oil',
    //   }

    // ],
    }
  },
  computed:{
    ...mapWritableState(useCounterStore, ['tab', 'isLoading']),
    ...mapState(useCounterStore, ['BASE_URL']),

  },
  methods:{
    async ajaxCallEmployes(){
      this.isLoading = true
      await axios.get(this.BASE_URL + 'user/all',
        {
          headers: {
            'Authorization':'Bearer ' + localStorage.getItem('access_token'),
            'Accept': 'application/json'
          }
        })
        .then(response => {
          console.log('this are all users.', response);
          
          this.list = response.data  
          // console.log(this.list)

          this.headers = Object.keys(response.data[0]);
          this.headers.push('View')
          this.headers.push('Action')
          
        })
        .catch(error => {
          console.error('There was an error:', error.response.data);
          if(error.response.data.detail == 'Could not validate credentials'){
            this.logout()          
          }
        });
        this.isLoading = false
    },
    async ajaxCallContainers(){
      this.isLoading = true

      await axios.get(this.BASE_URL + 'container/all',
        {
          headers: {
            'Authorization':'Bearer ' + localStorage.getItem('access_token'),
            'Accept': 'application/json'
          }
        })
        .then(response => {
          console.log('this are all containers.', response);
          
          this.list = response.data  
          // console.log(this.list)
          if(this.list.length == 0){
            this.headers = []
          }
          this.headers = Object.keys(response.data[0]);
          this.headers.push('View')
          this.headers.push('Action')
          
        })
        .catch(error => {
          // console.error('There was an error:', error.response.data);
          if(error.response != undefined && error.response.data != undefined){
          if(error.response.data.detail == 'Could not validate credentials'){
            this.logout()          
          }
          }
        });
        this.isLoading = false
    }
  },
  watch: {
    '$route.path': {
      immediate: true, // Trigger the watcher immediately on component creation
      handler(newPath, oldPath) {
        // Perform actions based on the new URL path
        if (newPath === '/database/employes') {
          this.ajaxCallEmployes();
        } else if (newPath === '/database/containers') {
          this.ajaxCallContainers();
        }
      }
    }
  },
  async created(){
    // this.$watch('$route.params', (newParams, oldParams) => {
    //   // Handle the parameter changes
    //   console.log('New params:', newParams);
    //   console.log('Old params:', oldParams);

    //   // Perform any necessary actions based on the parameter changes
    //   // For example, update data or fetch new data from an API
    // }, { deep: true });

    
    }
}
</script>