<template>
<v-main>
  <v-container fluid class="pa-1">
    <!-- <v-card elevation="2" style="background-image: url('../src/assets/images/background2.jpg');  background-size: cover;"> -->
<v-card class="pa-1" elevation="2" style="background-image: linear-gradient(to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)), url('../src/assets/images/background3.jpg'); background-size: cover;">

    <v-card color="grey-lighten-5"
                    border
                    class="mb-2"
                    density="compact">
    <DataTable :dataItems="containersList" :dataItemsHeaders="containersListHeaders" name="CONTAINERS"/>
    <br>
    </v-card>
    <br><br>
    <v-card color="grey-lighten-5"
                    border
                    class="mb-2"
                    density="compact">
    <DataTable :dataItems="employesList" :dataItemsHeaders="employesListHeaders" name="EMPLOYES"/>
    <br>
    </v-card>
    <br><br>
    <v-card color="grey-lighten-5"
                    border
                    density="compact">
    <DataTable :dataItems="dataItems" :dataItemsHeaders="dataItemsHeaders" name="Somethign third"/>
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
        Country:'Peru',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      },
      {
        Reference:'3224302',
        lastModify:'15/10/2021',
        Location:'San Sebastion',
        Country:'Peru',
        ResponsableName:'Ivan Sen',
        ClientName:'Sin Xaio Hel',
        TransportType:'Sea',
        ProductType:'Oil',
      },
      {
        Reference:'3224303',
        lastModify:'15/10/2021',
        Location:'Peuona',
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
    employesListHeaders:['id','legalFirstName','legalMiddleName','legalLastName','email','password','age','Position','View','Action'],
    employesList: [
      {
        id:'4',
        legalFirstName:'Matija',
        legalMiddleName:'Marin',
        legalLastName:'Corak',
        email:'matija@gmail.com',
        password:'*****',
        age:'30-54',
        Position:'Driver',
      },
      {
        id:'5',
        legalFirstName:'Pero',
        legalMiddleName:'Marin',
        legalLastName:'Corak',
        email:'matija@gmail.com',
        password:'*****',
        age:'30-54',
        Position:'Driver',
      },
      {
        id:'6',
        legalFirstName:'Sandro',
        legalMiddleName:'Marin',
        legalLastName:'Corak',
        email:'matija@gmail.com',
        password:'*****',
        age:'30-54',
        Position:'Driver',
      },
      {
        id:'7',
        legalFirstName:'Juro',
        legalMiddleName:'Marin',
        legalLastName:'Corak',
        email:'matija@gmail.com',
        password:'*****',
        age:'30-54',
        Position:'Driver',
      },
     

    ],
      dataItemsHeaders:['name','surname','country','lastModify','url','View','Action'],
      dataItems: [
        {
          name: 'Frozen Yogurt',
          surname: 'Krazy',
          country: 'Croatia',
          lastModify: '15/10/2023',
          url:'/post/Ref34856'
        },
        {
          name: 'Ice cream sandwich',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2023', 
          url:'/user/1'
        },
        {
          name: 'Eclair',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/post/3'
        },
        {
          name: 'Cupcake',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/post/4'
        },
        {
          name: 'Gingerbread',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/post/5'
        },
        {
          name: 'Jelly bean',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/6'
        },
        {
          name: 'Lollipop',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/7'
        },
        {
          name: 'Honeycomb',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/8'
        },
        {
          name: 'Donut',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/9'
        },
        {
          name: 'KitKat',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/10'
        },
        {
          name: 'Frozen Yogurt',
          surname: 'Krazy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/Ref34856'
        },
        {
          name: 'Ice cream sandwich',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021', 
          url:'/user/1'
        },
        {
          name: 'Eclair',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/3'
        },
        {
          name: 'Cupcakssse',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/4'
        },
        {
          name: 'Gingerbread',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/5'
        },
        {
          name: 'Jelly bean',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/6'
        },
        {
          name: 'Lollipop',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/7'
        },
        {
          name: 'Honeycomb',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/8'
        },
        {
          name: 'Donut',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/9'
        },
        {
          name: 'KitKat',
          surname: 'Frozy',
          country: 'Croatia',
          lastModify: '15/10/2021',
          url:'/object/10'
        },
      ],
    }
  },
}
</script>


<style scoped>

</style>