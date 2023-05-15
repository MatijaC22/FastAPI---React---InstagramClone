<template>
  <v-row justify="center" style="padding-top:12px;">
    <v-card
      v-for="post in postList"
      :key="post.id"
      border
      class="mb-4"
      density="compact"
      variant="text"
      style="background-color:white;"
      :width="800"
      
    >
      <v-list-item :title="post.caption.toUpperCase()" :subtitle="'Ref: ' + post.id" value="Card details">
        <template v-slot:prepend>
          <router-link :to="'/user/' + post.user.id + '?part=info'" @click="tab=0">
            <v-avatar image="https://randomuser.me/api/portraits/women/10.jpg" size="38" class="mr-4"></v-avatar>
          </router-link>
        </template>
      </v-list-item>

      <v-img 
        v-if="post.image_url_type == 'relative'" 
        :src="'http://localhost:8000/'+post.image_url" 
        height="328"
        style="object-fit: contain; object-position: center; border: 1px solid gray; background-color:black;"
        ></v-img>
      <v-img 
        v-else 
        :src="post.image_url" 
        height="328"
        style="object-fit: contain; object-position: center; border: 1px solid gray; background-color:black;"
      ></v-img>

      <v-card-text>
        {{post.caption}}
      </v-card-text>

      <template v-slot:actions>
        <v-btn color="primary" variant="text" :to="'/post/' + post.id" @click="tab=0">View More</v-btn>

        <v-btn color="primary" variant="text" @click="this.showInsertOrUpdateDialog(post, 'update')">Update</v-btn>

        <!-- OVDJE STAVI ITEM DA BUDE SVE OD OVOG POSTA -->
        <v-btn color="primary" variant="text" @click="this.showDeleteDialog(item)">Delete</v-btn>
        
        <v-btn color="primary" variant="text">See in Map</v-btn>
      </template>
    </v-card>
  </v-row>

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
    type="Posts" typeOfDialog="update"
  />
</template>


<script>
import DeleteDialog from '@/components/DeleteItemDialog.vue'
import InsertOrUpdateDialog from '@/components/InsertOrUpdateDialog.vue'

import { useCounterStore } from '@/stores/counter';
import { mapWritableState } from 'pinia'

export default {
  components:{
    InsertOrUpdateDialog,
    DeleteDialog,
  },
  props:{
    postList: {
      type: Array,
      required: true,
    },
  },
  data() {
    return{
      deleteDialog: false,
      deleteDialogItem:{},
      insertOrUpdateDialog: false,
      insertOrUpdateDialogItem:{},
    }
  },
  computed:{
    ...mapWritableState(useCounterStore, ['tab']),
  },
  methods:{
    showDeleteDialog(item) {
      console.log('ssad')
      this.deleteDialogItem = item;
      this.deleteDialog = true;
      console.log(this.deleteDialog)
    },
    handleDeleteItem(item) {
      // Do something with item here
      console.log('delete');
      console.log(item);
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
  }
}
</script>

<style scoped>

</style>