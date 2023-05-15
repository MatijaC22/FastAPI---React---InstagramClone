<template>
<v-main>
  <v-container fluid class="pa-1">
    <v-card class="pa-1" elevation="2" style="background-image: linear-gradient(to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)), url('../src/assets/images/background3.jpg'); background-size: cover;">

  <v-card color="grey-lighten-5"
                    border
                    density="compact">
    <DataTable :dataItems="containersList" :dataItemsHeaders="containersListHeaders" name="HERE GOES DATABASE TITLE"/>
    <br>
    </v-card>
    </v-card>

  </v-container>
</v-main>

</template>


<script>
import DataTable from '@/components/DataTable.vue'

export default {
  components:{
    DataTable
  },
  data() {
    return{
      containersListHeaders:['Reference','lastModify','Location','Country','ResponsableName','ClientName','TransportType','ProductType','View','Action'],
    containersList: [
      {
        Reference:'3224301',
        lastModify:'15/10/2023',
        Location:'San Sebastion',
        Country:'Guatemala',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      },
      {
        Reference:'3224302',
        lastModify:'15/10/2021',
        Location:'San Sebastion',
        Country:'Guatemala',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      },
      {
        Reference:'3224303',
        lastModify:'15/10/2021',
        Location:'San Sebastion',
        Country:'Guatemala',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      },
      {
        Reference:'3224304',
        lastModify:'15/10/2021',
        Location:'San Sebastion',
        Country:'Guatemala',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      },
      {
        Reference:'3224305',
        lastModify:'15/10/2021',
        Location:'San Sebastion',
        Country:'Guatemala',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      },
      {
        Reference:'3224306',
        lastModify:'15/10/2021',
        Location:'San Sebastion',
        Country:'Guatemala',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      },
      {
        Reference:'3224307',
        lastModify:'15/10/2021',
        Location:'San Sebastion',
        Country:'Guatemala',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      },
      {
        Reference:'3224308',
        lastModify:'15/10/2021',
        Location:'San Sebastion',
        Country:'Guatemala',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      },
      {
        Reference:'3224309',
        lastModify:'15/10/2021',
        Location:'San Sebastion',
        Country:'Guatemala',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      },
      {
        Reference:'3224310',
        lastModify:'15/10/2021',
        Location:'San Sebastion',
        Country:'Guatemala',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      },
      {
        Reference:'3224311',
        lastModify:'15/10/2021',
        Location:'San Sebastion',
        Country:'Guatemala',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      },
      {
        Reference:'3224312',
        lastModify:'15/10/2021',
        Location:'San Sebastion',
        Country:'Guatemala',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      }

    ],
    }
  },
  async created(){

      // OVO NIJE GOTOVO SAMO IDEJA KAKO CE SE POKUPITI INFO ZA SADA HARDCODED INFO U DATA/RETURN

      // this.username=localStorage.getItem('username')
    
      // const url = window.location.href;
      // const parts = url.split('/');
      // const typeOfDatabase = parts.pop()

      // await axios.get(this.BASE_URL + 'database/' + typeOfDatabase)
      // .then(response => {
      //   console.log('this is post.', response);
        
      //   this.post = response.data  
      //   this.post.caption = this.post.caption.toUpperCase()  
      // })
      // .catch(error => {
      //   console.error('There was an error:', error.response.data);
      // });
  }
}
</script>