<template>
  <v-app-bar
    app
    color="teal-darken-4"
    image="https://picsum.photos/1920/1080?random"
    fixed
  >
    <template v-slot:image>
      <v-img gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"></v-img>
    </template>
      
    <template v-slot:prepend v-if="smAndDown" >
      <v-app-bar-nav-icon variant="text" @click.stop="openNavBar = !openNavBar; searchBarVisible=false;"></v-app-bar-nav-icon>  
    </template>

    <v-avatar image="../src/assets/images/antaresWebp.webp" size="41" style="margin-left:10px;"></v-avatar>

    <v-app-bar-title>ANTARES PROGRAMMING</v-app-bar-title>

    <v-tabs
      v-model="tab"
      color="deep-purple-accent-4"
      align-tabs="end"
      v-if="mdAndUp"
    >
      <router-link to="/" class="routerLink">
        <v-tab :value="1">
              Home
        </v-tab>
      </router-link>
      <router-link to="/PostsList" class="routerLink">
        <v-tab :value="2">
              Posts
        </v-tab>
      </router-link>
      <v-tab :value="3"  id="menu-activator">
        Data
        <v-menu activator="#menu-activator" > 
          <v-list style="border-top-left-radius: 0; border-top-right-radius: 0;">
            <v-list-item
              v-for="item in navBarData"
              :key="item.title"
              :value="item.title"
              :to="item.value"
            >
              <v-list-item-title style="font-size:13px;">{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-tab>
    </v-tabs>
          

    <v-spacer v-if="mdAndUp"></v-spacer>    
          
          
    <v-btn icon v-if="smAndDown" @click="searchBarVisible = !searchBarVisible">
      <v-icon @click=onItemClick(1)>mdi-magnify</v-icon>
    </v-btn>
    <!-- <v-text-field v-if="mdAndUp"  variant="solo" style="margin-top:10px; padding-top:12px; " ></v-text-field> -->
    <v-text-field
    v-if="mdAndUp" 
      :loading="loading"
      density="compact"
      variant="solo"
      label="Search by reference number"
      append-inner-icon="mdi-magnify"
      single-line
      hide-details
      @click:append-inner="onClick"
    ></v-text-field>
          
  

    <div class="overflow-y-visible">
      <v-menu>
        <template v-slot:activator="{ props }">
          <v-btn icon v-bind="props" @click.stop="drawer = !drawer; searchBarVisible=false;">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
  
        <v-list>
          <v-list-item
            prepend-avatar="../src/assets/images/matija.jpg"
            title="Matija Corak"
            to="/user/1?part=info"
          ></v-list-item>

          <v-divider></v-divider>
  
          <v-list density="compact" nav>
            <v-list-item to="/user/1?part=info" prepend-icon="mdi-view-dashboard" title="User Info" value="User Info"></v-list-item>
            <v-list-item to="/user/1?part=posts" prepend-icon="mdi-forum" title="User Posts" value="User Posts"></v-list-item>
            <v-list-item title="Language" value="Language">
              <template v-slot:prepend>
                <v-avatar image="../src/assets/images/ES.png" size="24" class="mr-8"></v-avatar>
              </template>
            </v-list-item>
          </v-list>
        </v-list>
      </v-menu>
    </div>
  </v-app-bar>


        
  <v-text-field
  v-if="smAndDown && searchBarVisible" 
    :loading="loading"
    density="compact"
    variant="solo"
    label="Search"
    append-inner-icon="mdi-magnify"
    class="search-bar"
    single-line
    hide-details
    @click:append-inner="onClick"
  ></v-text-field>



  <v-navigation-drawer
    v-model="openNavBar"
    location="left"
    temporary
    width="300"
  >
    <v-list v-model:opened="open">
      <v-list-item prepend-icon="mdi-home" title="Home" to="/"></v-list-item>
      <v-list-item prepend-icon="mdi-account-multiple-outline" title="Posts" to="/postsList"></v-list-item>
      <v-list-group value="Data">
        <template v-slot:activator="{ props }">
          <v-list-item
            v-bind="props"
            prepend-icon="mdi-folder"
            title="Data"
          ></v-list-item>
        </template>

        <v-list-group value="All">
          <template v-slot:activator="{ props }">
            <v-list-item
              v-bind="props"
              title="All"
            ></v-list-item>
          </template>

          <v-list-item
            v-for="([title, icon, url], i) in data"
            :key="i"
            :title="title"
            :prepend-icon="icon"
            :value="title"
            :to="url"
          ></v-list-item>
        </v-list-group>
        <v-list-item title="Latest" to="/DataList"/>


      </v-list-group>
    </v-list>  
  </v-navigation-drawer>
</template>

<script>
import { useDisplay } from 'vuetify'
import { defineComponent } from 'vue'


import { useCounterStore } from '@/stores/counter';
import { mapWritableState } from 'pinia'

export default defineComponent({
  data() {
    const { xs, mdAndUp, smAndDown } = useDisplay()
    return {
      searchBarVisible: false,
      drawer: null,
      openNavBar: null,
      // tab: null,
      loaded: false,
      loading: false,
      open: ['Users'],
      data: [
        ['Containers', 'mdi-file-outline', '/database/containers'],
        ['Employes', 'mdi-plus-outline', '/database/employes'],
      ],
      // cruds: [
      //   ['Show All', 'mdi-account-multiple-outline'],
      //   ['Insert', 'mdi-cog-outline'],
      //   ['Create', 'mdi-plus-outline'],
      //   ['Read', 'mdi-file-outline'],
      //   ['Update', 'mdi-update'],
      //   ['Delete', 'mdi-delete'],
      // ],      
      navBarMain: [
        {
          title: 'Home',
          value: '/',
          icon: 'mdi-home'
        },
        {
          title: 'Posts',
          value: '/PostsList',
          icon: 'mdi-account-multiple-outline'
        },
        {
          title: 'Data',
          value: '/DataList',
          icon: 'mdi-folder'
        },
      ],
      navBarData: [
        {
          title: 'LATEST',
          value: '/DataList',
          icon: 'mdi-home'
        },
        {
          title: 'CONTAINERS',
          value: '/database/containers',
          icon: 'mdi-account-multiple-outline'
        },
        {
          title: 'EMPLOYES',
          value: '/database/employes',
          icon: 'mdi-folder'
        },
      ],
      xs, mdAndUp, smAndDown
    }
  },
  methods: {
    onItemClick(item) {
      // Handle the click event on the dropdown menu item
      console.log(`Clicked ${this.searchBarVisible}${this.smAndDown}`);
    },
    onClick () {
      this.loading = true

      setTimeout(() => {
        this.loading = false
        this.loaded = true
      }, 2000)
    }
  },
  computed:{
    ...mapWritableState(useCounterStore, ['tab']),
  }
})
</script>


<style scoped>
.search-bar {
  position: fixed;
  top: 66px;
  left: 0px;
  right: 0;
  margin: 0 auto;
  z-index: 9999;
  width:300px;
  /* height: 56px; */
  border-radius: 10px;
  /* background:white; */
}
/* .routerLink{
     text-decoration: none;
 } */


</style>
