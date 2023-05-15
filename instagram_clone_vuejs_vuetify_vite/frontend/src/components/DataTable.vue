<template>
<div>
  
  <v-card border density="compact" :title="name" variant="text">
    <tr style="width:100%;">
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
              @click:append-inner="onClick"
              style="min-width:230px; margin: 0 10px 0 15px;"
              v-model="search"
            >
          </v-text-field>
        </div>
        <v-menu>
          <template v-slot:activator="{ props }">
            <v-btn
              color="primary"
              v-bind="props"
              style="margin-bottom:0px;"
              height="42"
            >
              Filter
            </v-btn>
          </template>
          <v-card border
            density="compact"
            variant="text"
          >
            <!-- <v-list-tile v-for="checkbox in cvc" :key="checkbox.option.name">
              <v-list-tile-content >
                
                  <v-checkbox :value="checkbox.option.name" 
                              :key="checkbox.option.name"
                              :label="checkbox.option.name"
                              v-model="checkbox.option.checked"
                              style="background-color:white; height:50px;">
                  </v-checkbox>
                  
              </v-list-tile-content>
            </v-list-tile> -->
          </v-card>
        </v-menu> 
        <v-btn
          color="primary"
          v-bind="props"
          style="margin-bottom:0px;"
          class="ml-2"
          height="42"
          @click="this.exportExcel(paginatedItems)"
        >
          Download
        </v-btn>         
        <v-btn
          
          
          color="primary"
          v-bind="props"
          height="42"
          class="ml-2"
        >
          INSERT
        </v-btn>
    </div>
  </tr>

  <!-- <br> -->
 

  <!-- height je sada 63.5vh ali treba viit kako to nastimati korektno -->
  <v-table
    fixed-header
    height="63.5vh"
    density="compact"
    class="mt-2"
  >
  <thead>
    <tr>
      <th class="text-left"
        v-for="(title, index) in dataItemsHeaders"
        :key="index"
      >
        {{ title }}
      </th>
    </tr>
  </thead>
    <tbody>
      <tr v-for="(item, index) in paginatedItems" :key="index">
        <td v-for="(value, key) in item" :key="key" :style="`color: ${key=='lastModify' && isOlderThan30Days(item.lastModify) ? 'red' : 'black'}`">{{ value }}</td>
        <td>
          <router-link :to="name == 'Containers' ? '/post/'+item.tankRef : 'Containers' ? '/user/'+item.id : item.url" class="routerLink" style="color:black;">
            View
          </router-link>
        </td>
        <td>
          <v-btn icon size="small" class="mr-1 my-1" @click="this.showDeleteDialog(item)">
            <v-icon>mdi-delete</v-icon>
          </v-btn>
          <v-btn icon  @click="this.showInsertOrUpdateDialog(item, 'update')" size="small" class="my-1">
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
        </td>
      </tr>           
    </tbody>
  </v-table>

  <div class="text-center">
    <v-pagination
      size="small"
      v-model="currentPage"
      :length="totalPages"
      rounded="circle"
    ></v-pagination>
  </div>

  </v-card>
  </div>

    <DeleteDialog 
      :deleteDialog="deleteDialog"
      @update:deleteDialog="deleteDialog = $event"
      :deleteDialogItem="deleteDialogItem"
      @deleteItem="handleDeleteItem"
    />
                    
    <InsertOrUpdateDialog 
      :insertOrUpdateDialog="insertOrUpdateDialog"
      @update:insertOrUpdateDialog="insertOrUpdateDialog = $event"
      :insertOrUpdateDialogItem="insertOrUpdateDialogItem"
      @insertOrUpdateItem="handleInsertOrUpdateItem"
      :type="name" :typeOfDialog="typeOfDialog"
    />


</template>

<script>

import moment from 'moment';
import InsertOrUpdateDialog from '@/components/InsertOrUpdateDialog.vue'
import DeleteDialog from '@/components/DeleteItemDialog.vue'

import xlsx from 'xlsx/dist/xlsx.full.min';


export default {
  components:{
    InsertOrUpdateDialog,
    DeleteDialog,
  },
  props: {
    dataItems: {
      type: Array,
      required: true,
    },
    dataItemsHeaders: {
      type: Array,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
  },
  data() {
    return{
      checkboxes: [],
      search: '',
      list: this.dataItems,
      currentPage: 1,
      itemsPerPage: 10,
      insertOrUpdateDialog: false,
      insertOrUpdateDialogItem:{},
      deleteDialog: false,
      deleteDialogItem:{},
      typeOfDialog:'insert',

    }
  },
  computed: {
    filteredItems(){
      return this.list.filter((data) => {
        const values = Object.values(data)
        return values.some((value) => {
          return String(value).toLowerCase().includes(this.search.toLowerCase())
        })
      })
    },
    totalPages() {
      return Math.ceil(this.filteredItems.length / this.itemsPerPage);
    },
    paginatedItems() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      return this.filteredItems.slice(startIndex, endIndex);
    },
  },
  methods:{
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage -= 1;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage += 1;
      }
    },
    isOlderThan30Days(dateStr) {
      const today = moment();
      const date = moment(dateStr, 'DD/MM/YYYY');
      const daysDifference = today.diff(date, 'days');
      return daysDifference > 30;
    },
    showInsertOrUpdateDialog(item,typeOfDialog){
      this.typeOfDialog = typeOfDialog;
      this.insertOrUpdateDialogItem = item;
      this.insertOrUpdateDialog = true;
    },
    handleInsertOrUpdateItem(item) {
      // Do something with item here
      console.log(this.typeOfDialog);
      console.log(this.insertOrUpdateDialogItem);
      console.log(item);
      window.location.reload();

    },
    showDeleteDialog(item) {
      this.deleteDialogItem = item;
      this.deleteDialog = true;
    },
    handleDeleteItem(item) {
      // Do something with item here
      console.log('delete');
      console.log(item);
    },
    exportExcel(data){
      const XLSX = xlsx
      const workbook = XLSX.utils.book_new();
      const worksheet = XLSX.utils.json_to_sheet(data);
      XLSX.utils.book_append_sheet(workbook, worksheet, "framework")
      XLSX.writeFile(workbook, this.name + '.xlsx')
    }
    
  }
}
</script>


<style scoped>

</style>