<template>
  <v-row justify="center">
      <v-dialog
        v-model="dialogValue"
        persistent
        width="1024"
      >
        <v-card>
          <v-card-title>
            <span class="text-h5">{{type}}</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <div v-if="type == 'CONTAINERS'">
                <InsertOrUpdateContainersForm 
                    :insertOrUpdateDialogItem='insertOrUpdateDialogItem'
                    @update:insertOrUpdateItem="insertOrUpdateDialogItem = $event"
                    @enter-in-db="insertOrUpdateItemInDB"
                />
              </div>
              <div v-else-if="type == 'EMPLOYES'">
                <InsertOrUpdateEmployesForm 
                    :insertOrUpdateDialogItem='insertOrUpdateDialogItem'
                    @update:insertOrUpdateItem="insertOrUpdateDialogItem = $event"
                    @enter-in-db="insertOrUpdateItemInDB"
                />
              </div>
              <div v-else-if="type == 'POSTS'">
                <InsertOrUpdatePostsForm 
                    :insertOrUpdateDialogItem='insertOrUpdateDialogItem'
                    @update:insertOrUpdateItem="insertOrUpdateDialogItem = $event"
                    @enter-in-db="insertOrUpdateItemInDB"
                />
              </div>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="blue-darken-1"
              variant="text"
              @click="closeDialog"
            >
              Close
            </v-btn>
          </v-card-actions>
          
        </v-card>
      </v-dialog>
    </v-row>
</template>

<script>
import InsertOrUpdateContainersForm from '@/components/InsertOrUpdateContainersForm.vue'
import InsertOrUpdateEmployesForm from '@/components/InsertOrUpdateEmployesForm.vue'
import InsertOrUpdatePostsForm from '@/components/InsertOrUpdatePostsForm.vue'
export default {
  components:{
    InsertOrUpdateContainersForm,
    InsertOrUpdateEmployesForm,
    InsertOrUpdatePostsForm
  },
  props:{
    insertOrUpdateDialog: {
      type: Boolean,
      required: true,
    },
    insertOrUpdateDialogItem: {
      type: Object,
      required: true,
    },
    type: {
      type: String,
      required: true,
    }
  },
  data() {
    return{
      login_in_submission: false,
      login_show_alert: false,
      login_alert_variant: 'color: #c7c7c7;   box-shadow:0 0 5px rgba(52, 152, 219, .7), 0 0 10px rgba(52, 152, 219, .7); padding:10px;',
      login_alert_msg: 'Please wait! We are logging you in.',


      error:false,
      Position:null,
      Age:null,
      Password:null,
      Email:null,
      legalLastName:null,
      middleNameInsert:null,
      firstNameInsert:null,


    }
  },
  computed: {
    dialogValue: {
      get() {
        return this.insertOrUpdateDialog;
      },
      set(value) {
        this.$emit('update:insertOrUpdateDialog', value);
      },
    },
    
  },
  methods: {
    closeDialog() {
      //OVO SAM MAKNUO MISLIM DA MI JE TO REFRESHALO STRANICU KAD SAM ISAO NA CLOSE BUTTON
      // this.$emit('insertOrUpdateItem', this.insertOrUpdateDialogItem);
      this.dialogValue = false;
    },
    insertOrUpdateItemInDB(InsertedOrUpdatedItem){
      console.log(InsertedOrUpdatedItem)
      

      this.$emit('insertOrUpdateItem', this.insertOrUpdateDialogItem);
      this.dialogValue = false;
    }
  },
  created(){
    // console.log(this.type)
    // console.log(this.insertOrUpdateDialogItem)
  }
}
</script>


<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');

.text{
  font-size: 30px;
  color: white;
  font-weight: 600;
  letter-spacing: 2px;
  // text-align:center;
}
// .veeform{
//   margin-top: 10px;
// }
.veeform .field{
  margin-top: 20px;
  display: flex;
}
.field .fas{
  height: 50px;
  width: 60px;
  color: #868686;
  font-size: 20px;
  line-height: 50px;
  border-bottom: 1px solid #444;
  border-right: none;
  border-radius: 5px 0 0 5px;
  background: linear-gradient(#333,#222);
}
.field .veeinput,.veeform button{
  height: 50px;
  width: 100%;
  outline: none;
  font-size: 16px;
  color: #bbb;
  padding: 0 15px;
  border-radius: 0 5px 5px 0;
  border-bottom: 1px solid #bbb;
  caret-color: #3399cc;
  // background: linear-gradient(#333,#222);
  // background: linear-gradient(#bbb, #ddd);
  background: linear-gradient(#F8F8F8	, #F8F8F8);
  // background: linear-gradient(#DDD, #BBB);
  // background: linear-gradient(hsl(0, 0%, 50%), hsl(0, 0%, 30%));




}
.veeinput:focus {
  color: #3399cc;
  box-shadow: 0 0 5px rgba(0, 191, 255, 0.2),
              inset 0 0 5px rgba(0, 191, 255, 0.1);
  // background: linear-gradient(#333933, #222922);
  animation: glow .8s ease-out infinite alternate;
}

@keyframes glow {
  0% {
    border-color: #3399cc;
    // box-shadow: 0 0 5px rgba(0, 191, 255, 0.2),
    //             inset 0 0 5px rgba(0, 0, 0, 0.1);
  }
  100% {
    border-color: #99ccff;
    // box-shadow: 0 0 20px rgba(0, 191, 255, 0.6),
    //             inset 0 0 10px rgba(0, 191, 255, 0.4);
  }
}

.submit{
  margin-top: 30px;
  border-radius: 5px!important;
  font-weight: 600;
  letter-spacing: 1px;
  cursor: pointer;
}
.submit:hover{
  color: #3399cc;
  border: 1px solid #3399cc;
  box-shadow: 0 0 5px rgba(0, 191, 255, 0.3),
              0 0 10px rgba(0, 191, 255, 0.2),
              0 0 15px rgba(0, 191, 255, 0.1);
}

</style>